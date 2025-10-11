# Qubic SmartGuard Development Setup Script for Windows

Write-Host "🧠 Setting up Qubic SmartGuard Development Environment..." -ForegroundColor Cyan

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.11+" -ForegroundColor Red
    exit 1
}

# Install Python dependencies
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Yellow
pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables
$env:PYTHONPATH = "$PWD;$PWD\src"
$env:STREAMLIT_SERVER_PORT = "8501"
$env:STREAMLIT_SERVER_ADDRESS = "0.0.0.0"

# Create necessary directories
if (-not (Test-Path "files")) { New-Item -ItemType Directory -Path "files" }
if (-not (Test-Path ".streamlit")) { New-Item -ItemType Directory -Path ".streamlit" }
if (-not (Test-Path "src\__pycache__")) { New-Item -ItemType Directory -Path "src\__pycache__" -Force }

Write-Host "✅ Environment setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Starting Qubic SmartGuard..." -ForegroundColor Cyan
Write-Host "📡 App will be available at: http://localhost:8501" -ForegroundColor Yellow
Write-Host ""

# Start the Streamlit app
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
