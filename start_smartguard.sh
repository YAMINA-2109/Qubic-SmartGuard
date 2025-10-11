#!/bin/bash

# Qubic SmartGuard Startup Script
# This script launches the SmartGuard application with proper configuration

echo "🧠 Starting Qubic SmartGuard..."
echo "======================================"

# Navigate to the SmartGuard directory
cd /workspaces/qubic-voting-dapp/Qubic-SmartGuard

# Check if required packages are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "⚠️  Installing Streamlit..."
    pip3 install --user streamlit
fi

if ! python3 -c "import langchain" 2>/dev/null; then
    echo "⚠️  Installing LangChain..."
    pip3 install --user langchain
fi

# Create logs directory if it doesn't exist
mkdir -p logs

# Launch options
echo ""
echo "🚀 SmartGuard Launch Options:"
echo "1. Full SmartGuard App (recommended)"
echo "2. Functional SmartGuard App"  
echo "3. Test App (minimal)"
echo "4. Proof of Concept"
echo ""

read -p "Select option (1-4) [default: 2]: " choice
choice=${choice:-2}

case $choice in
    1)
        echo "🧠 Launching Full SmartGuard Application..."
        echo "📍 URL: http://localhost:8501"
        streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
        ;;
    2)
        echo "🧠 Launching Functional SmartGuard Application..."
        echo "📍 URL: http://localhost:8502"
        streamlit run app_functional.py --server.port 8502 --server.address 0.0.0.0 --server.headless true
        ;;
    3)
        echo "🧪 Launching Test Application..."
        echo "📍 URL: http://localhost:8503"
        streamlit run ultra_minimal.py --server.port 8503 --server.address 0.0.0.0 --server.headless true
        ;;
    4)
        echo "✅ Launching Proof of Concept..."
        echo "📍 URL: http://localhost:8508"
        streamlit run proof_working.py --server.port 8508 --server.address 0.0.0.0 --server.headless true
        ;;
    *)
        echo "❌ Invalid option. Starting functional app..."
        echo "� URL: http://localhost:8502"
        streamlit run app_functional.py --server.port 8502 --server.address 0.0.0.0 --server.headless true
        ;;
esac
