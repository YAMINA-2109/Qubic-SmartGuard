# Production Deployment Guide

## 🚀 Quick Production Deployment

### Option 1: Streamlit Community Cloud (Recommended)

1. **Fork/Clone Repository**

   ```bash
   git clone https://github.com/YAMINA-2109/Qubic-SmartGuard.git
   ```

2. **Deploy to Streamlit Cloud**

   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set main file: `main_app.py`
   - Deploy automatically

3. **Configure Environment**
   - No additional environment variables needed
   - Uses default Qubic RPC endpoints

### Option 2: Docker Production Deployment

1. **Build Production Image**

   ```bash
   docker build -t qubic-smartguard:latest .
   ```

2. **Run Production Container**

   ```bash
   docker run -d \
     --name smartguard-prod \
     -p 8501:8501 \
     --restart unless-stopped \
     qubic-smartguard:latest
   ```

3. **With Docker Compose**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Option 3: VPS/Server Deployment

1. **Server Requirements**

   - Ubuntu 20.04+ / CentOS 8+
   - Python 3.11+
   - 2GB RAM minimum
   - 10GB storage

2. **Install Dependencies**

   ```bash
   sudo apt update
   sudo apt install python3.11 python3-pip nginx
   pip3 install -r requirements.txt
   ```

3. **Setup Service**

   ```bash
   # Create systemd service
   sudo nano /etc/systemd/system/smartguard.service
   ```

   ```ini
   [Unit]
   Description=Qubic SmartGuard
   After=network.target

   [Service]
   Type=simple
   User=www-data
   WorkingDirectory=/opt/smartguard
   ExecStart=/usr/bin/python3 -m streamlit run main_app.py --server.address 0.0.0.0 --server.port 8501
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

4. **Enable and Start**

   ```bash
   sudo systemctl enable smartguard
   sudo systemctl start smartguard
   ```

5. **Configure Nginx (Optional)**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 🔧 Production Configuration

### Environment Variables

Create `.env` file:

```bash
# Production settings
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true

# Qubic RPC settings
QUBIC_RPC_ENDPOINT=https://rpc.qubic.org
RPC_TIMEOUT=30
MAX_RETRIES=3

# Logging
LOG_LEVEL=INFO
```

### Performance Optimization

1. **Streamlit Configuration**

   ```toml
   # .streamlit/config.toml
   [server]
   maxUploadSize = 200
   maxMessageSize = 200
   enableCORS = false
   enableXsrfProtection = true

   [browser]
   gatherUsageStats = false
   ```

2. **Memory Optimization**
   ```python
   # Add to main_app.py
   import gc
   gc.collect()  # Force garbage collection
   ```

## 📊 Monitoring & Health Checks

### Health Check Endpoint

Add to your deployment:

```python
# health_check.py
import requests
import sys

def check_health():
    try:
        response = requests.get("http://localhost:8501/healthz", timeout=10)
        return response.status_code == 200
    except:
        return False

if __name__ == "__main__":
    if check_health():
        print("✅ SmartGuard is healthy")
        sys.exit(0)
    else:
        print("❌ SmartGuard is unhealthy")
        sys.exit(1)
```

### Log Monitoring

```bash
# View logs
journalctl -u smartguard -f

# Log rotation
sudo nano /etc/logrotate.d/smartguard
```

## 🔒 Security Checklist

- ✅ HTTPS enabled (use Let's Encrypt)
- ✅ Firewall configured (only ports 80, 443, 22)
- ✅ Regular security updates
- ✅ Monitoring and alerting
- ✅ Backup strategy
- ✅ Rate limiting (via nginx)

## 🚦 Load Testing

```bash
# Install ab (Apache Bench)
sudo apt install apache2-utils

# Test with 100 concurrent users
ab -n 1000 -c 100 http://your-domain.com/

# Expected results:
# - Response time: <500ms
# - Success rate: 100%
# - Concurrent users: 100+
```

## 📈 Scaling

### Horizontal Scaling

```yaml
# docker-compose.scale.yml
version: "3.8"
services:
  smartguard:
    image: qubic-smartguard:latest
    deploy:
      replicas: 3
    ports:
      - "8501-8503:8501"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    depends_on:
      - smartguard
```

### Load Balancer Configuration

```nginx
upstream smartguard_backend {
    server localhost:8501;
    server localhost:8502;
    server localhost:8503;
}

server {
    listen 80;
    location / {
        proxy_pass http://smartguard_backend;
    }
}
```

## 🔄 CI/CD Pipeline

### GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python verify_live_connection.py

      - name: Deploy to production
        run: |
          # Your deployment script
          ./deploy.sh
```

## 📱 Mobile Optimization

The platform is mobile-responsive by default, but for optimal mobile experience:

1. **PWA Support** (Add to main_app.py):

   ```python
   st.markdown('''
   <link rel="manifest" href="manifest.json">
   <meta name="theme-color" content="#0f172a">
   ''', unsafe_allow_html=True)
   ```

2. **Mobile-First CSS**:
   ```css
   @media (max-width: 768px) {
     .stSidebar > div:first-child {
       margin-left: -21rem;
     }
   }
   ```

## 🎯 Performance Benchmarks

Target performance metrics:

- **Page Load**: <2 seconds
- **API Response**: <500ms
- **Live Data Update**: <1 second
- **Memory Usage**: <512MB
- **CPU Usage**: <25%

Monitor these with your preferred monitoring solution (DataDog, New Relic, etc.).

---

**Your SmartGuard platform is now production-ready! 🚀**
