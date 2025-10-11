#!/usr/bin/env python3
"""
SmartGuard Production Validation Script
=====================================

This script validates the real Qubic integration for the SmartGuard audit platform.
Run this to ensure your installation is working correctly before deploying to production.

Usage: python smartguard_production_validation.py
"""

import sys
import os
from pathlib import Path
import time

def print_header(title):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def print_step(step_num, description):
    """Print a formatted step."""
    print(f"\n[Step {step_num}] {description}")
    print("-" * 40)

def validate_files():
    """Validate that required files exist."""
    print_step(1, "Validating Required Files")
    
    required_files = [
        "qubic_real_execution.py",
        "README_QUBIC_INTEGRATION.md",
        "SMARTGUARD_PRODUCTION_PACKAGE.md"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        return False
    
    print("\n✅ All required files present")
    return True

def test_import():
    """Test importing the integration module."""
    print_step(2, "Testing Module Import")
    
    try:
        from qubic_real_execution import RealQubicDevKit, compile_and_run_qubic_real
        print("✅ Successfully imported RealQubicDevKit")
        print("✅ Successfully imported compile_and_run_qubic_real")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_qubic_cli():
    """Test qubic-cli availability."""
    print_step(3, "Testing Qubic CLI Availability")
    
    try:
        from qubic_real_execution import RealQubicDevKit
        qdk = RealQubicDevKit()
        print(f"✅ Qubic CLI found at: {qdk.qubic_cli_path}")
        return True
    except Exception as e:
        print(f"❌ Qubic CLI test failed: {e}")
        return False

def test_compilation():
    """Test real contract compilation."""
    print_step(4, "Testing Real Contract Compilation")
    
    try:
        from qubic_real_execution import RealQubicDevKit
        
        # Simple test contract
        test_contract = '''
        struct TestContract {
            long value;
            
            void setValue(long newValue) {
                value = newValue;
            }
            
            long getValue() {
                return value;
            }
        };
        '''
        
        qdk = RealQubicDevKit()
        print("🔄 Compiling test contract...")
        
        result = qdk.compile_contract(test_contract)
        
        if result['success']:
            print("✅ Compilation successful!")
            print(f"📄 Bytecode length: {len(result.get('bytecode', ''))} bytes")
            return True
        else:
            print(f"❌ Compilation failed: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Compilation test failed: {e}")
        return False

def test_smartguard_integration():
    """Test SmartGuard-style integration."""
    print_step(5, "Testing SmartGuard Integration Pattern")
    
    try:
        from qubic_real_execution import compile_and_run_qubic_real
        
        # Mock SmartGuard state object
        class MockSmartContractState:
            def __init__(self):
                self.contract_code = '''
                struct VotingContract {
                    long voteCount;
                    
                    void vote() {
                        voteCount++;
                    }
                    
                    long getVotes() {
                        return voteCount;
                    }
                };
                '''
                self.messages = []
        
        print("🔄 Testing SmartGuard integration pattern...")
        
        mock_state = MockSmartContractState()
        result_state = compile_and_run_qubic_real(mock_state)
        
        print("✅ SmartGuard integration pattern works!")
        print(f"📝 Generated {len(result_state.messages)} status messages")
        
        # Show some messages
        for i, msg in enumerate(result_state.messages[-3:]):
            print(f"   💬 {msg}")
            
        return True
        
    except Exception as e:
        print(f"❌ SmartGuard integration test failed: {e}")
        return False

def print_summary(results):
    """Print validation summary."""
    print_header("VALIDATION SUMMARY")
    
    passed = sum(results.values())
    total = len(results)
    
    print(f"\nTests Passed: {passed}/{total}")
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {test_name}")
    
    if passed == total:
        print(f"\n🎉 ALL TESTS PASSED!")
        print("✅ Your SmartGuard integration is ready for production!")
        print("\n📋 Next Steps:")
        print("   1. Copy qubic_real_execution.py to your SmartGuard project")
        print("   2. Update your import in the QuBIC node file")
        print("   3. Test in your SmartGuard environment")
        print("   4. Deploy to production")
    else:
        print(f"\n⚠️  Some tests failed. Please check the errors above.")
        print("📖 See README_QUBIC_INTEGRATION.md for troubleshooting.")

def main():
    """Run all validation tests."""
    print_header("SmartGuard Production Validation")
    print("Validating Qubic real execution integration for SmartGuard...")
    
    results = {}
    
    # Run all validation tests
    results["File Validation"] = validate_files()
    results["Module Import"] = test_import()
    results["Qubic CLI"] = test_qubic_cli()
    results["Contract Compilation"] = test_compilation()
    results["SmartGuard Integration"] = test_smartguard_integration()
    
    # Print summary
    print_summary(results)

if __name__ == "__main__":
    main()
