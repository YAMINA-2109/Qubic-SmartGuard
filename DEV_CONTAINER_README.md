# 🐳 Qubic SmartGuard Dev Container Setup

This guide helps you set up the Qubic SmartGuard project with VS Code Dev Containers for a consistent development environment.

## 🚀 Quick Start

### Prerequisites
- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Option 1: Using Dev Container (Recommended)

1. **Open in Dev Container**
   ```bash
   # Clone the repository (if not already done)
   git clone https://github.com/YAMINA-2109/Qubic-SmartGuard.git
   cd Qubic-SmartGuard
   
   # Open in VS Code
   code .
   ```

2. **Start Dev Container**
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Dev Containers: Reopen in Container"
   - Select the option and wait for the container to build

3. **Access the Application**
   - The container will automatically install dependencies and start
   - Open your browser to `http://localhost:8501`
   - The Streamlit app should be running!

### Option 2: Using Docker Compose

```bash
# Build and start the services
docker-compose up --build

# Access the app at http://localhost:8501
```

### Option 3: Local Development (Windows)

```powershell
# Run the PowerShell setup script
.\start_dev.ps1
```

```bash
# Or use the bash script (if you have WSL/Git Bash)
./start_dev.sh
```

## 🔧 Development Environment Features

### Included Tools & Extensions
- **Python 3.11** with all required packages
- **VS Code Extensions:**
  - Python support with linting and formatting
  - Jupyter notebook support
  - C++ tools (for smart contract analysis)
  - YAML, JSON, and Markdown support
  - Code spell checker
  - Auto-formatting on save

### Port Forwarding
- **8501**: Streamlit application
- **3000**: Development server (if needed)
- **5000**: Flask/FastAPI (if needed)

### Environment Variables
```bash
PYTHONPATH=/workspace:/workspace/src
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## 📁 Project Structure

```
Qubic-SmartGuard/
├── .devcontainer/
│   ├── devcontainer.json    # Dev container configuration
│   └── Dockerfile          # Custom container image
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── src/
│   └── langgraphagenticai/ # AI agents and graph logic
├── files/                  # Uploaded files and screenshots
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Docker Compose setup
├── start_dev.ps1          # Windows setup script
└── start_dev.sh           # Linux/Mac setup script
```

## 🛠️ Troubleshooting

### Container Won't Start
1. Ensure Docker Desktop is running
2. Check if ports 8501, 3000, 5000 are available
3. Try rebuilding the container:
   ```bash
   # In VS Code Command Palette
   Dev Containers: Rebuild Container
   ```

### Python Import Errors
1. Check if `PYTHONPATH` is set correctly
2. Verify all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

### Streamlit App Won't Load
1. Check if the app is running on the correct port:
   ```bash
   streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```
2. Verify firewall/antivirus isn't blocking the connection
3. Try accessing via `http://127.0.0.1:8501` instead

### Permission Issues (Windows)
```powershell
# If you get execution policy errors, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🔄 Development Workflow

1. **Start Development**
   - Open project in Dev Container
   - Wait for automatic setup to complete

2. **Make Changes**
   - Edit code with full IntelliSense support
   - Auto-formatting and linting on save

3. **Test Changes**
   - Streamlit auto-reloads on file changes
   - View changes instantly in browser

4. **Debug Issues**
   - Use VS Code's integrated debugger
   - View logs in the integrated terminal

## 🎯 Next Steps

1. **Configure API Keys**: Set up your LLM API keys in environment variables
2. **Upload Contracts**: Use the Streamlit interface to upload C++ smart contracts
3. **Run Analysis**: Follow the app's workflow for complete smart contract auditing
4. **Customize**: Modify the AI agents in `src/langgraphagenticai/` for your needs

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the main [README.md](README.md) for project details
3. Open an issue on GitHub with your error details

---

**Happy coding! 🧠✨**
