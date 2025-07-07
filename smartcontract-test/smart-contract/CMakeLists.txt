cmake_minimum_required(VERSION 3.16)
project(QubicVotingContract)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
include_directories(.)

# Add executable
add_executable(voting_contract main.cpp)

# Set compiler flags for optimization
if(MSVC)
    target_compile_options(voting_contract PRIVATE /O2 /W4)
    target_compile_definitions(voting_contract PRIVATE _CRT_SECURE_NO_WARNINGS)
else()
    target_compile_options(voting_contract PRIVATE -O3 -Wall -Wextra)
endif()

# Set output directory
set_target_properties(voting_contract PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)
