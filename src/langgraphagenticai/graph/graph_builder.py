"""
Graph builder for Qubic SmartGuard
Uses enhanced LLM-powered security analysis
"""

from .enhanced_graph_builder import enhanced_graph


def graph_builder():
    """
    Returns an enhanced graph with LLM-powered security analysis.
    Falls back to improved mock analysis if LLM is unavailable.
    """
    return enhanced_graph


# === Compiled graph ready for use ===
generated_graph = graph_builder()
