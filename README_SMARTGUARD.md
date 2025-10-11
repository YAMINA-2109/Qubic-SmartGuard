# 🧠 Qubic SmartGuard

Advanced AI-powered smart contract analysis and validation system for the Qubic blockchain.

## Features

- **Automated Code Analysis**: AI-driven code review and commenting
- **Security Auditing**: Comprehensive security vulnerability assessment  
- **Performance Validation**: Optimization recommendations
- **Functional Specification**: Auto-generated documentation
- **Test Plan Generation**: Comprehensive testing strategies
- **Local Simulation**: Safe contract testing environment
- **Qubic Integration**: DevKit execution simulation

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

3. Upload your C++ smart contract and follow the guided analysis workflow.

## Architecture

The system uses a LangGraph-based workflow with 8 analysis steps:
- Code Commenting
- Semantic Analysis  
- Strict Validation
- Security Audit
- Functional Specification
- Documentation Generation
- Test Planning
- Simulation & Execution

## Configuration

Copy `.env.example` to `.env` and configure your settings.

## Project Structure

```
Qubic-SmartGuard/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment configuration template
├── README.md             # This file
└── src/
    └── langgraphagenticai/
        ├── state/
        │   └── state.py      # State management
        ├── nodes/
        │   └── analysis_nodes.py  # Analysis functions
        └── graph/
            ├── graph_builder.py  # Graph construction
            └── mock_graph.py     # Mock implementation
```

## Usage

1. **Upload Contract**: Upload your C++ smart contract file
2. **Review Analysis**: View AI-generated comments and analysis
3. **Security Audit**: Review security findings and recommendations
4. **Documentation**: Get comprehensive technical documentation
5. **Testing**: Review generated test plans
6. **Simulation**: Run contract simulations
7. **Export**: Download complete analysis report

## Development

This is a demo/proof-of-concept implementation. For production use:
- Replace mock implementations with real AI models
- Add actual Qubic network integration
- Implement real smart contract compilation
- Add user authentication and data persistence

## License

MIT License - see LICENSE file for details.
