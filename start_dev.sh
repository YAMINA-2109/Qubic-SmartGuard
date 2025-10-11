#!/bin/bash

# Qubic SmartGuard Development Setup Script

echo "🧠 Setting up Qubic SmartGuard Development Environment..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables
export PYTHONPATH="${PWD}:${PWD}/src"
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS="0.0.0.0"

# Create necessary directories
mkdir -p files/.streamlit src/__pycache__

echo "✅ Environment setup complete!"
echo ""
echo "🚀 Starting Qubic SmartGuard..."
echo "📡 App will be available at: http://localhost:8501"
echo ""

# Start the Streamlit app
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
