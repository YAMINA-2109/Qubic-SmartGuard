#include <iostream>
#include <cstring>
#include <cstdlib>

// Simple test for mutual exclusivity logic
bool testMutualExclusivity(int argc, char* argv[]) {
    bool found_args = false;
    bool found_params = false;
    
    // Scan all arguments for --args and --params
    for (int j = 1; j < argc; j++) {
        if (strcmp(argv[j], "--args") == 0) {
            found_args = true;
        } else if (strcmp(argv[j], "--params") == 0) {
            found_params = true;
        }
    }
    
    // Check mutual exclusivity after scanning all arguments
    if (found_args && found_params) {
        std::cout << "Error: Cannot use both --args and --params. Use only one." << std::endl;
        return false;
    }
    
    return true;
}

int main(int argc, char* argv[]) {
    std::cout << "Testing mutual exclusivity logic..." << std::endl;
    
    // Test 1: Only --args
    char* test1[] = {"program", "--args", "value1"};
    if (testMutualExclusivity(3, test1)) {
        std::cout << "✓ Test 1 passed: Only --args" << std::endl;
    } else {
        std::cout << "✗ Test 1 failed: Only --args" << std::endl;
    }
    
    // Test 2: Only --params
    char* test2[] = {"program", "--params", "value2"};
    if (testMutualExclusivity(3, test2)) {
        std::cout << "✓ Test 2 passed: Only --params" << std::endl;
    } else {
        std::cout << "✗ Test 2 failed: Only --params" << std::endl;
    }
    
    // Test 3: Both --args and --params (should fail)
    char* test3[] = {"program", "--args", "value1", "--params", "value2"};
    if (!testMutualExclusivity(5, test3)) {
        std::cout << "✓ Test 3 passed: Both --args and --params correctly rejected" << std::endl;
    } else {
        std::cout << "✗ Test 3 failed: Both --args and --params should be rejected" << std::endl;
    }
    
    // Test 4: Neither --args nor --params
    char* test4[] = {"program", "--other", "value"};
    if (testMutualExclusivity(3, test4)) {
        std::cout << "✓ Test 4 passed: Neither --args nor --params" << std::endl;
    } else {
        std::cout << "✗ Test 4 failed: Neither --args nor --params" << std::endl;
    }
    
    std::cout << "Testing completed." << std::endl;
    return 0;
}
