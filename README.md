````markdown
# 🧠 Qubic SmartGuard

Qubic SmartGuard is an AI-powered assistant for auditing and documenting Qubic Smart Contracts written in C++.  
It performs static analysis, semantic validation, commenting, security auditing, functional specification generation, test planning, simulation, and final reporting—all in an easy-to-use Streamlit interface.

---

## 🚀 Key Features

✅ Upload and analyze C++ smart contracts (QPI)  
✅ Automatic code commenting and review  
✅ Semantic and strict validation checks  
✅ Security audit report generation  
✅ Functional specification and flow diagram generation (Mermaid.js)  
✅ Detailed technical documentation  
✅ Test plan creation for functions and procedures  
✅ Editable simulation of onTransaction/onTick scenarios  
✅ (Future) RPC integration for real on-chain Qubic Dev Kit execution  

---

## 🎯 Project Goal

> **Qubic SmartGuard** aims to **democratize** smart contract auditing on the Qubic platform by providing an **accessible**, **AI-assisted**, and **complete** audit pipeline that turns raw C++ code into a fully documented and validated smart contract report.  

This tool is designed to help both **developers** and **auditors** save time while improving security and transparency.

---

## 📸 Screenshots

### 1️⃣ Upload and Language Selection
![Upload](images/1_upload.PNG)

### 2️⃣ Automatic Commenting
![Commented Example](images/3-example_commente.PNG)

### 3️⃣ Semantic Analysis and Validation
![Analysis](images/4-analyse_validation.PNG)

### 4️⃣ Security Audit Report
![Security Report](images/5-security_report.PNG)

### 5️⃣ Detailed Documentation
![Documentation 1](images/6-details_docs.PNG)
![Documentation 2](images/7-details_docs.PNG)

### 6️⃣ Test Plan
![Test Plan](images/9-test_plan.PNG)

### 7️⃣ Simulation
![Simulation](images/10-simulation.PNG)

### 8️⃣ Qubic Dev Kit Execution (Static Demo)
![Qubic Dev](images/11-qubic_dev.PNG)

---

## 🧩 How It Works

1️⃣ **Upload** your C++ Smart Contract file (QPI)  
2️⃣ **AI Commenting**: The model explains and documents your code.  
3️⃣ **Analysis & Validation**: Semantic error detection and strict validation.  
4️⃣ **Security Audit**: AI-generated audit with recommendations.  
5️⃣ **Functional Specification**: Objectives, context, core principles, and flow diagram.  
6️⃣ **Detailed Documentation**: Technical narrative with diagrams.  
7️⃣ **Test Plan**: Structured, clear testing strategy for your contract.  
8️⃣ **Simulation**: Edit and run sample scenarios.  
9️⃣ **Qubic Dev Kit Execution**: (Currently static) Shows expected deployment logs.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/qubic-smartguard.git
cd qubic-smartguard
````
(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

Install dependencies (recommended: Python 3.10+):

```bash
pip install -r requirements.txt
```

---

## ⚠️ Environment Variables
Before running the app, you must create a .env file in the project root with your own API keys.

These environment variables are required:
```bash
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

## ⚙️ Running the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
QUBIC_SMARTGUARD/
│
├── files/
│   ├── qubic_logo.png
│   └── qubiclogo.jiff
│
├── src/
│   ├── langgraphagenticai/
│   │   ├── graph/
│   │   │   ├── graph_builder.py
│   │   │   └── __init__.py
│   │   ├── LLMS/
│   │   │   ├── groqllm.py
│   │   │   └── __init__.py
│   │   ├── nodes/
│   │   │   ├── qubicdocs_nodes.py
│   │   │   └── __init__.py
│   │   ├── state/
│   │   │   ├── state.py
│   │   │   └── __init__.py
│   │   └── utils/
│   │       ├── validators.py
│   │       └── __init__.py
│   └── __init__.py
│
├── app.py
├── requirements.txt
└── .gitignore
```

---

## 🌟 Features in Detail

### ✅ AI Commenting

Improves code readability with inline comments and docstrings.

### ✅ Validation

* **Semantic Analysis**: Highlights missing functions and struct fields.
* **Strict Validation**: Ensures syntax correctness.

### ✅ Security Audit

* Detects vulnerabilities.
* Suggests improvements.

### ✅ Functional Spec

* Markdown spec.
* Mermaid.js flow diagrams.

### ✅ Detailed Docs

* Technical explanation.
* Step-by-step flow.

### ✅ Test Plan

* Clear test cases.
* Expected results.

### ✅ Simulation

* Manual scenario entry.
* AI-generated result based on scenario.

### ✅ Qubic Dev Kit Execution (Static)

* Placeholder for real RPC integration.
* AI-generated sample logs.

---

## ⚠️ Limitations

* RPC integration not yet implemented (Qubic testnet node deployment).
* Simulation scenarios are manually defined.
* AI-generated logs in the last step are **static**.

---

## 🛡️ Roadmap

* ✅ Local simulation with manual scenarios
* 🔜 Automatic scenario generation from code
* 🔜 RPC-based live testnet deployment
* 🔜 Full end-to-end Qubic Dev Kit integration

---

## 🤝 Contributing

We welcome contributions!
Please open an issue or PR for:

* Feature requests
* Bug reports
* Enhancements

---

## 📜 License

[MIT](LICENSE)

---

## 🙏 Acknowledgements

Thanks to the Qubic team for providing the QPI platform and the inspiration to build this auditing tool.

---

## ⭐ Authors

* YAMINA ATMAOUI – AI Engineer, Web Developer
* Hackathon Team – \[SmartGuard _ Qubic Track]

---

> This project was built as part of \[**Lablab.ai Hackathon**] to help secure and democratize Qubic Smart Contract development.

```
