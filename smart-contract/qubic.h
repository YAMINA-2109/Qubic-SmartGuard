#pragma once

// Qubic SDK Header Stub
// This is a minimal implementation for development purposes

#include <stdint.h>

// Qubic 256-bit integer type (placeholder)
struct m256i {
    uint64_t data[4];
};

// Basic Qubic types
typedef uint64_t QubicTick;
typedef m256i QubicAddress;

// Contract execution context (placeholder)
struct QubicContext {
    QubicTick currentTick;
    QubicAddress caller;
    uint64_t value;
};

// Global context (would be provided by Qubic runtime)
extern QubicContext qubicContext;

// Placeholder for Qubic runtime functions
inline QubicTick getCurrentTick() {
    return qubicContext.currentTick;
}

inline QubicAddress getCaller() {
    return qubicContext.caller;
}

inline uint64_t getValue() {
    return qubicContext.value;
}

// Initialize context for testing
inline void initQubicContext() {
    qubicContext.currentTick = 1000000;
    qubicContext.value = 0;
    for (int i = 0; i < 4; i++) {
        qubicContext.caller.data[i] = 0;
    }
}
