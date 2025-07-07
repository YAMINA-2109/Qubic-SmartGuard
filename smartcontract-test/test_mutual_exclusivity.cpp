#include <iostream>
#include <cstring>
#include <cstdlib>

// Simulate the LOG macro
#define LOG(x) std::cout << x

// Test the mutual exclusivity logic
int test_mutual_exclusivity(int argc, char* argv[]) {
    int i = 0; // Start at the beginning of arguments
    
    // Parse optional --args or --params parameter (mutually exclusive)
    bool found_args = false;
    bool found_params = false;
    
    // First pass: check for mutual exclusivity
    for (int j = i + 1; j < argc; j++) {
        if (strcmp(argv[j], "--args") == 0) {
            if (found_params) {
                LOG("Error: Cannot use both --args and --params. Use only one.\n");
                return 1;
            }
            found_args = true;
        } else if (strcmp(argv[j], "--params") == 0) {
            if (found_args) {
                LOG("Error: Cannot use both --args and --params. Use only one.\n");
                return 1;
            }
            found_params = true;
        }
    }
    
    LOG("Mutual exclusivity check passed!\n");
    
    // Second pass: parse the arguments
    if (i + 1 < argc && (strcmp(argv[i + 1], "--args") == 0 || strcmp(argv[i + 1], "--params") == 0)) {
        std::string args_value = argv[i + 2];
        LOG("Arguments: " << args_value << "\n");
        i += 2;
    }
    
    return 0;
}

int main(int argc, char* argv[]) {
    std::cout << "Testing mutual exclusivity logic with " << argc << " arguments:\n";
    for (int i = 0; i < argc; i++) {
        std::cout << "  argv[" << i << "] = " << argv[i] << "\n";
    }
    std::cout << "\n";
    
    return test_mutual_exclusivity(argc, argv);
}
