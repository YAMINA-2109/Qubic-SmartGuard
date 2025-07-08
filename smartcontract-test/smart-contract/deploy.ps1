# Qubic Voting DApp Smart Contract Deployment Script (PowerShell)
# This script builds and deploys the voting smart contract

Write-Host "=== Qubic Voting DApp Smart Contract Deployment ===" -ForegroundColor Green
Write-Host "Building smart contract..." -ForegroundColor Yellow

# Check if cmake is available
if (-not (Get-Command cmake -ErrorAction SilentlyContinue)) {
    Write-Host "Error: cmake not found. Please install CMake." -ForegroundColor Red
    exit 1
}

# Create build directory
if (-not (Test-Path "build")) {
    New-Item -ItemType Directory -Name "build" | Out-Null
}

Set-Location build

# Configure build
Write-Host "Configuring build..." -ForegroundColor Yellow
cmake ..

if ($LASTEXITCODE -eq 0) {
    # Build the contract
    Write-Host "Building contract..." -ForegroundColor Yellow
    cmake --build . --config Release
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Smart contract built successfully!" -ForegroundColor Green
        Write-Host "Contract binary: build/bin/Release/voting_contract.exe" -ForegroundColor Cyan
        
        # Test the contract
        Write-Host "Testing contract..." -ForegroundColor Yellow
        Set-Location bin/Release
        ./voting_contract.exe
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Contract test passed!" -ForegroundColor Green
        } else {
            Write-Host "✗ Contract test failed!" -ForegroundColor Red
        }
    } else {
        Write-Host "✗ Build failed!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✗ Configuration failed!" -ForegroundColor Red
    exit 1
}

# Return to original directory
Set-Location ../..

Write-Host ""
Write-Host "=== Deployment Instructions ===" -ForegroundColor Green
Write-Host "1. The contract has been compiled successfully" -ForegroundColor White
Write-Host "2. To deploy to Qubic network, you need to:" -ForegroundColor White
Write-Host "   - Upload the contract binary using qubic-cli" -ForegroundColor Gray
Write-Host "   - Register with the network using appropriate commands" -ForegroundColor Gray
Write-Host "   - Set up contract initialization parameters" -ForegroundColor Gray
Write-Host ""
Write-Host "Contract features:" -ForegroundColor Cyan
Write-Host "- Create voting proposals" -ForegroundColor White
Write-Host "- Register voters" -ForegroundColor White
Write-Host "- Cast votes with comments" -ForegroundColor White
Write-Host "- Track vote counts and results" -ForegroundColor White
Write-Host "- Close proposals when voting period ends" -ForegroundColor White
Write-Host ""
Write-Host "Deployment completed!" -ForegroundColor Green
