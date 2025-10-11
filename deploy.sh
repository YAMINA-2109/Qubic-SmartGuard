#!/bin/bash

# 🚀 Qubic SmartGuard - Production Deployment Script

set -e  # Exit on any error

echo "🛡️ Starting Qubic SmartGuard Production Deployment"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
APP_NAME="qubic-smartguard"
APP_DIR="/opt/smartguard"
SERVICE_NAME="smartguard"
DOMAIN=${DOMAIN:-"localhost"}
USER="smartguard"

# Functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   log_error "This script should not be run as root for security reasons"
   exit 1
fi

# Create application user if it doesn't exist
create_user() {
    log_info "Creating application user..."
    if ! id "$USER" &>/dev/null; then
        sudo useradd -m -s /bin/bash $USER
        log_success "User $USER created"
    else
        log_info "User $USER already exists"
    fi
}

# Install system dependencies
install_dependencies() {
    log_info "Installing system dependencies..."
    
    # Update package list
    sudo apt update
    
    # Install required packages
    sudo apt install -y \
        python3.11 \
        python3.11-pip \
        python3.11-venv \
        nginx \
        git \
        curl \
        htop \
        ufw \
        certbot \
        python3-certbot-nginx
    
    log_success "System dependencies installed"
}

# Setup application directory
setup_app_directory() {
    log_info "Setting up application directory..."
    
    # Create application directory
    sudo mkdir -p $APP_DIR
    sudo chown $USER:$USER $APP_DIR
    
    # Copy application files
    if [ -d "$(pwd)" ]; then
        sudo cp -r . $APP_DIR/
        sudo chown -R $USER:$USER $APP_DIR
        log_success "Application files copied to $APP_DIR"
    else
        log_error "Current directory not found"
        exit 1
    fi
}

# Setup Python virtual environment
setup_python_environment() {
    log_info "Setting up Python virtual environment..."
    
    cd $APP_DIR
    
    # Create virtual environment
    sudo -u $USER python3.11 -m venv venv
    
    # Install Python dependencies
    sudo -u $USER ./venv/bin/pip install --upgrade pip
    sudo -u $USER ./venv/bin/pip install -r requirements.txt
    
    log_success "Python environment setup complete"
}

# Create systemd service
create_systemd_service() {
    log_info "Creating systemd service..."
    
    sudo tee /etc/systemd/system/${SERVICE_NAME}.service > /dev/null <<EOF
[Unit]
Description=Qubic SmartGuard Application
After=network.target

[Service]
Type=simple
User=$USER
Group=$USER
WorkingDirectory=$APP_DIR
Environment=PATH=$APP_DIR/venv/bin
ExecStart=$APP_DIR/venv/bin/streamlit run main_app.py --server.address 0.0.0.0 --server.port 8501
Restart=always
RestartSec=10

# Output to syslog
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=$SERVICE_NAME

[Install]
WantedBy=multi-user.target
EOF

    # Reload systemd and enable service
    sudo systemctl daemon-reload
    sudo systemctl enable $SERVICE_NAME
    
    log_success "Systemd service created and enabled"
}

# Configure nginx
configure_nginx() {
    log_info "Configuring nginx..."
    
    sudo tee /etc/nginx/sites-available/$APP_NAME > /dev/null <<EOF
server {
    listen 80;
    server_name $DOMAIN;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_cache_bypass \$http_upgrade;
        
        # Increase timeout for long-running requests
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # Static files (if any)
    location /static {
        alias $APP_DIR/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

    # Enable site
    sudo ln -sf /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled/
    sudo rm -f /etc/nginx/sites-enabled/default
    
    # Test nginx configuration
    sudo nginx -t
    
    log_success "Nginx configured"
}

# Configure firewall
configure_firewall() {
    log_info "Configuring firewall..."
    
    # Enable UFW
    sudo ufw --force enable
    
    # Allow SSH, HTTP, and HTTPS
    sudo ufw allow ssh
    sudo ufw allow 'Nginx Full'
    
    # Allow specific port for development (optional)
    # sudo ufw allow 8501
    
    log_success "Firewall configured"
}

# Setup SSL with Let's Encrypt
setup_ssl() {
    if [ "$DOMAIN" != "localhost" ]; then
        log_info "Setting up SSL certificate..."
        
        # Stop nginx temporarily
        sudo systemctl stop nginx
        
        # Get SSL certificate
        sudo certbot certonly --standalone -d $DOMAIN --non-interactive --agree-tos --email admin@$DOMAIN
        
        # Update nginx config for SSL
        sudo tee /etc/nginx/sites-available/$APP_NAME > /dev/null <<EOF
server {
    listen 80;
    server_name $DOMAIN;
    return 301 https://\$server_name\$request_uri;
}

server {
    listen 443 ssl http2;
    server_name $DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;

    # SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384;
    ssl_prefer_server_ciphers off;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_cache_bypass \$http_upgrade;
    }
}
EOF
        
        log_success "SSL certificate configured"
    else
        log_warning "Skipping SSL setup for localhost"
    fi
}

# Start services
start_services() {
    log_info "Starting services..."
    
    # Start SmartGuard service
    sudo systemctl start $SERVICE_NAME
    sudo systemctl status $SERVICE_NAME --no-pager
    
    # Start nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx
    
    log_success "Services started"
}

# Verify deployment
verify_deployment() {
    log_info "Verifying deployment..."
    
    # Check if SmartGuard service is running
    if sudo systemctl is-active --quiet $SERVICE_NAME; then
        log_success "SmartGuard service is running"
    else
        log_error "SmartGuard service failed to start"
        sudo systemctl status $SERVICE_NAME --no-pager
        exit 1
    fi
    
    # Check if nginx is running
    if sudo systemctl is-active --quiet nginx; then
        log_success "Nginx is running"
    else
        log_error "Nginx failed to start"
        sudo systemctl status nginx --no-pager
        exit 1
    fi
    
    # Test HTTP response
    sleep 10  # Give services time to start
    if curl -f -s "http://localhost" > /dev/null; then
        log_success "HTTP response test passed"
    else
        log_warning "HTTP response test failed (this might be normal for first startup)"
    fi
}

# Main deployment process
main() {
    echo "🚀 Starting deployment process..."
    echo "Domain: $DOMAIN"
    echo "App Directory: $APP_DIR"
    echo "User: $USER"
    echo ""
    
    create_user
    install_dependencies
    setup_app_directory
    setup_python_environment
    create_systemd_service
    configure_nginx
    configure_firewall
    
    if [ "$DOMAIN" != "localhost" ]; then
        setup_ssl
    fi
    
    start_services
    verify_deployment
    
    echo ""
    echo "🎉 Deployment completed successfully!"
    echo "=================================================="
    echo "✅ SmartGuard is running at:"
    if [ "$DOMAIN" != "localhost" ]; then
        echo "   🌐 https://$DOMAIN"
        echo "   🌐 http://$DOMAIN (redirects to HTTPS)"
    else
        echo "   🌐 http://localhost"
    fi
    echo ""
    echo "📋 Useful commands:"
    echo "   sudo systemctl status $SERVICE_NAME    # Check service status"
    echo "   sudo systemctl restart $SERVICE_NAME   # Restart service"
    echo "   sudo systemctl stop $SERVICE_NAME      # Stop service"
    echo "   sudo journalctl -u $SERVICE_NAME -f    # View logs"
    echo "   sudo systemctl status nginx            # Check nginx status"
    echo ""
    echo "🔧 Configuration files:"
    echo "   Service: /etc/systemd/system/${SERVICE_NAME}.service"
    echo "   Nginx: /etc/nginx/sites-available/$APP_NAME"
    echo "   App: $APP_DIR"
    echo ""
    log_success "Your Qubic SmartGuard platform is now live! 🛡️"
}

# Run main function
main "$@"
