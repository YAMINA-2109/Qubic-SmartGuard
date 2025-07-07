#!/bin/bash

# Qubic Voting DApp Smart Contract Deployment Script
# This script builds and deploys the voting smart contract

echo "=== Qubic Voting DApp Smart Contract Deployment ==="
echo "Building smart contract..."

# Check if cmake is available
if ! command -v cmake &> /dev/null; then
    echo "Error: cmake not found. Please install CMake."
    exit 1
fi

# Create build directory
mkdir -p build
cd build

# Configure build
echo "Configuring build..."
cmake ..

# Build the contract
echo "Building contract..."
cmake --build . --config Release

if [ $? -eq 0 ]; then
    echo "✓ Smart contract built successfully!"
    echo "Contract binary: build/voting_contract"
else
    echo "✗ Build failed!"
    exit 1
fi

# In a real deployment, you would:
# 1. Upload the contract to Qubic network
# 2. Get a contract ID
# 3. Register the contract with the network

echo ""
echo "=== Deployment Instructions ==="
echo "1. The contract has been compiled successfully"
echo "2. To deploy to Qubic network, you need to:"
echo "   - Upload the contract binary using qubic-cli"
echo "   - Register with the network using appropriate commands"
echo "   - Set up contract initialization parameters"
echo ""
echo "Contract features:"
echo "- Create voting proposals"
echo "- Register voters"
echo "- Cast votes with comments"
echo "- Track vote counts and results"
echo "- Close proposals when voting period ends"
echo ""
echo "Deployment completed!"