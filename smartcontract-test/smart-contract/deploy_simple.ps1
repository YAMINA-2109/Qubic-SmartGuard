# Qubic Voting DApp Smart Contract Deployment Script (PowerShell)
Write-Host "=== Qubic Voting DApp Smart Contract Deployment ===" -ForegroundColor Green

# Check if cmake is available
if (-not (Get-Command cmake -ErrorAction SilentlyContinue)) {
    Write-Host "Error: cmake not found. Please install CMake." -ForegroundColor Red
    exit 1
}

# Create and enter build directory
if (-not (Test-Path "build")) {
    New-Item -ItemType Directory -Name "build" | Out-Null
}
Set-Location build

# Configure and build
Write-Host "Configuring and building..." -ForegroundColor Yellow
cmake ..
cmake --build . --config Release

# Check if build succeeded
if (Test-Path "bin/Release/voting_contract.exe") {
    Write-Host "✓ Smart contract built successfully!" -ForegroundColor Green
    
    # Test the contract
    Write-Host "Testing contract..." -ForegroundColor Yellow
    Set-Location bin/Release
    ./voting_contract.exe
    Write-Host "✓ Contract test completed!" -ForegroundColor Green
    
    # Return to original directory
    Set-Location ../..
    
    Write-Host ""
    Write-Host "=== Deployment Complete ===" -ForegroundColor Green
    Write-Host "Contract binary: build/bin/Release/voting_contract.exe" -ForegroundColor Cyan
    Write-Host "Next steps: Use qubic-cli to deploy to Qubic network" -ForegroundColor White
} else {
    Write-Host "✗ Build failed!" -ForegroundColor Red
    exit 1
}

# Return to original directory
Set-Location ..
