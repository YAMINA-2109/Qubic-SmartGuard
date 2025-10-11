#!/bin/bash

# Qubic SmartGuard Platform Launcher
# Professional bridge between Smart Contract Auditing and Voting dApp

echo "🛡️ Qubic SmartGuard Platform Launcher"
echo "======================================"
echo ""

# Function to check if port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null ; then
        return 0
    else
        return 1
    fi
}

# Stop any existing Streamlit processes
echo "🔄 Stopping existing processes..."
pkill -f streamlit 2>/dev/null
sleep 2

echo "🚀 Starting Qubic SmartGuard Platform..."
echo ""

# Start the unified interface
streamlit run main_app.py --server.address 0.0.0.0 --server.port 8501 &
MAIN_PID=$!

# Wait a moment for startup
sleep 3

if check_port 8501; then
    echo "✅ Unified Platform: http://localhost:8501"
    echo ""
    echo "🎯 Available Applications:"
    echo "  🏠 Platform Overview - Main dashboard"
    echo "  🔍 Smart Contract Auditor - Security analysis"
    echo "  🗳️ Voting dApp - Decentralized governance"
    echo ""
    echo "📱 Access Methods:"
    echo "  1. Use the sidebar navigation"
    echo "  2. Click application cards on homepage"
    echo "  3. Use quick action buttons"
    echo ""
    echo "⌨️  Controls:"
    echo "  Ctrl+C - Stop the platform"
    echo "  Refresh browser - Reload interface"
    echo ""
    echo "🌐 Open: http://localhost:8501"
else
    echo "❌ Failed to start platform on port 8501"
    exit 1
fi

# Keep the script running
wait $MAIN_PID
