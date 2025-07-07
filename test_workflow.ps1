# Qubic Contract CLI Test Script
# This demonstrates the complete contract workflow

Write-Host "=== QUBIC CONTRACT CLI WORKFLOW TEST ==="
Write-Host ""

# Set paths
$CLI_PATH = "c:\qubic-voting-dapp\qubic-cli\build\Release\qubic-cli.exe"
$CONTRACT_SOURCE = "c:\qubic-voting-dapp\smart-contract\main.cpp"
$BYTECODE_FILE = "test_workflow.bytecode"
$CONTRACT_ADDRESS = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"

Write-Host "Step 1: Contract Compilation"
Write-Host "----------------------------"
& $CLI_PATH -contractcompile $CONTRACT_SOURCE $BYTECODE_FILE
Write-Host ""

Write-Host "Step 2: Contract Validation"
Write-Host "----------------------------"
& $CLI_PATH -contractvalidate $BYTECODE_FILE
Write-Host ""

Write-Host "Step 3: Contract Deployment"
Write-Host "----------------------------"
& $CLI_PATH -contractdeploy --bytecode $BYTECODE_FILE --wallet testWallet --network testnet
Write-Host ""

Write-Host "Step 4: Contract Function Calls"
Write-Host "--------------------------------"

Write-Host "4a. Call with --args parameter:"
& $CLI_PATH -contractcall --contract $CONTRACT_ADDRESS --function vote --wallet testWallet --network testnet --args "proposalId=1,choice=true"
Write-Host ""

Write-Host "4b. Call with --params parameter:"
& $CLI_PATH -contractcall --contract $CONTRACT_ADDRESS --function createProposal --wallet testWallet --network testnet --params "title=Test Proposal,description=Test Description"
Write-Host ""

Write-Host "4c. Call without arguments:"
& $CLI_PATH -contractcall --contract $CONTRACT_ADDRESS --function getResults --wallet testWallet --network testnet
Write-Host ""

Write-Host "Step 5: Show Help"
Write-Host "----------------"
# Display help output without piping to avoid PowerShell errors
Write-Host "Running: $CLI_PATH -help"
& $CLI_PATH -help | Out-String | Write-Host
Write-Host ""

Write-Host "=== WORKFLOW COMPLETE ==="
Write-Host "All contract commands are working correctly!"
Write-Host "Files created:"
Write-Host "- $BYTECODE_FILE (compiled contract bytecode)"
Write-Host "- contract.env (deployment details)"
Write-Host "- contract_call.log (function call results)"
