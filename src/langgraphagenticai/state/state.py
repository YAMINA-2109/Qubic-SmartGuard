from pydantic import BaseModel

class SmartContractState(BaseModel):
    """
    The shared state object for the LangGraph workflow.
    Holds all intermediate and final results for the Qubic SmartGuard pipeline.
    """

    # === INPUTS ===
    input_code: str = None              # Original C++ smart contract
    language: str = "english"           # Language for prompts/responses

    # === PARSING ===
    parsed: str = None                  # Preprocessed / linted code

    # === COMMENTING & REVIEW ===
    commented: str = None               # Code with generated comments
    status: str = "Valid"               # Review status: Valid / Needs Fix
    message: str = None                 # Reviewer feedback
    reviewed: bool = False              # Flag if reviewed at least once
    review_attempts: int = 0            # Counter for loop limit

    # === SEMANTIC ANALYSIS ===
    semantic_report: str = None         # Static analysis of smart contract

    # === AUDIT ===
    audit_report: str = None            # Security & optimization audit

    # === FUNCTIONAL SPECIFICATION ===
    functional_spec: str = None         # Introductory functional spec section

    # === FLOW DIAGRAM ===
    flow_diagram: str = None            # Mermaid.js diagram text

    # === DETAILED DOCUMENTATION ===
    detailed_doc: str = None            # Section 3 detailed technical doc

    # === SUMMARY REPORT ===
    business_summary: str = None        # Combined final documentation report

    # === STRICT VALIDATION ===
    strict_validation_report: str = None # Result of static validation rules

    # === SIMULATION ===
    simulation_scenario: str = None     # User-defined or default simulation scenario
    simulation_result: str = None       # VM simulation JSON result

    # === TEST PLAN ===
    test_plan: str = None               # Generated test plan markdown

    # === DEV KIT EXECUTION ===
    qubic_logs: str = None              # Compilation / execution logs
    compilation_success: bool = None    # Compilation success flag

    # === EXPORT ===
    output_json: str = None             # Path to exported JSON file
