# 🛡️ Qubic SmartGuard Platform

**Professional Smart Contract Security & Decentralized Governance Suite**

## 🎯 Overview

The Qubic SmartGuard Platform is a unified interface that bridges two powerful applications:

1. **🔍 Smart Contract Auditor** - AI-powered security analysis and vulnerability detection
2. **🗳️ Voting dApp** - Decentralized governance platform for community proposals

## 🚀 Quick Start

### Option 1: Unified Platform (Recommended)

```bash
# Start the complete platform
streamlit run main_app.py --server.address 0.0.0.0 --server.port 8501

# Or use the launcher script
./start_unified_platform.sh
```

### Option 2: Individual Applications

```bash
# Smart Contract Auditor only
streamlit run app.py --server.port 8501

# Voting dApp only
streamlit run voting_app.py --server.port 8502
```

## 🌐 Access URLs

- **Unified Platform**: http://localhost:8501
- **Individual Audit App**: http://localhost:8501 (when run separately)
- **Individual Voting App**: http://localhost:8502 (when run separately)

## 🎛️ Navigation Methods

### 1. Sidebar Navigation

- Use the radio buttons in the sidebar to switch between:
  - 🏠 Platform Overview
  - 🔍 Smart Contract Auditor
  - 🗳️ Voting dApp

### 2. Quick Actions

- **🚀 New Audit** - Start a new smart contract analysis
- **📝 Create Proposal** - Create a new governance proposal
- **📊 View Analytics** - Access platform analytics

### 3. Application Cards

- Click the application launcher buttons on the homepage

## 🔍 Smart Contract Auditor Features

- **📤 File Upload**: Upload C++ smart contracts
- **💬 Code Commentary**: AI-generated code explanations
- **📊 Analysis & Validation**: Comprehensive security analysis
- **🔍 Security Audit**: Vulnerability detection and reporting
- **📘 Documentation**: Automatic technical documentation
- **🧪 Testing**: Test plan generation
- **🤖 Simulation**: Contract behavior simulation
- **⚙️ Qubic Integration**: Dev kit execution logs

## 🗳️ Voting dApp Features

- **📋 Proposal Management**: Create and view governance proposals
- **🗳️ Voting System**: Cast votes (YES/NO/ABSTAIN)
- **📊 Real-time Results**: Live vote tracking and analytics
- **👤 User Management**: Track individual voting history
- **📈 Analytics**: Participation rates and vote distribution
- **💾 Export**: Download voting data and reports

## 📁 File Structure

```
/workspace/
├── main_app.py                 # 🎯 Unified platform interface
├── app.py                      # 🔍 Smart contract auditor
├── voting_app.py              # 🗳️ Voting dApp
├── real_qubic_integration.py  # 🔗 Qubic network integration
├── start_unified_platform.sh  # 🚀 Platform launcher script
├── platform_config.conf       # ⚙️ Configuration settings
├── requirements.txt           # 📦 Python dependencies
└── src/                       # 📂 Source modules
    └── langgraphagenticai/    # 🤖 AI analysis engine
```

## 🎨 Platform Features

### Professional Interface

- **Dark Theme**: Modern, professional appearance
- **Gradient Styling**: Attractive visual design
- **Responsive Layout**: Works on desktop and tablet
- **Status Indicators**: Real-time system status
- **Progress Tracking**: Visual progress for audits

### System Status Monitoring

- **Audit System**: Online/Offline status
- **Voting System**: Demo/Live mode indicator
- **Network Status**: Qubic network connectivity

### Analytics Dashboard

- **Platform Statistics**: Usage metrics and activity
- **Performance Monitoring**: System health tracking
- **User Activity**: Engagement analytics (when enabled)

## ⚙️ Configuration

Edit `platform_config.conf` to customize:

- **Network Settings**: Testnet/Mainnet configuration
- **Security Options**: File size limits, allowed types
- **UI Preferences**: Theme, animations, layout
- **Feature Toggles**: Enable/disable components

## 🔧 Advanced Usage

### Custom Integration

The platform supports integration with real Qubic networks:

1. Compile the Qubic C++ library
2. Set `REAL_INTEGRATION=true` in config
3. Provide contract addresses and private keys
4. Enable live network connectivity

### Export Capabilities

- **Audit Reports**: Complete markdown reports
- **Voting Data**: JSON export of proposals and votes
- **Analytics**: Performance and usage statistics

## 🛡️ Security Features

- **Input Validation**: Safe file upload handling
- **Session Management**: Secure state management
- **Demo Mode**: Safe testing environment
- **Data Privacy**: No sensitive data storage

## 📊 Platform Statistics

The unified interface displays:

- **Contracts Audited**: Total audit count
- **Active Proposals**: Current governance items
- **Total Votes Cast**: Community participation
- **Security Score**: Overall platform security

## 🎯 Use Cases

### For Developers

- Audit smart contracts before deployment
- Get detailed security analysis and documentation
- Generate comprehensive test plans

### For Communities

- Create and vote on governance proposals
- Track proposal outcomes and participation
- Export voting records for transparency

### For Organizations

- Professional smart contract security auditing
- Decentralized decision-making processes
- Comprehensive reporting and analytics

## 🔄 Updates and Maintenance

### Restart Platform

```bash
pkill -f streamlit
./start_unified_platform.sh
```

### Check Status

```bash
ps aux | grep streamlit
netstat -tlnp | grep :8501
```

### View Logs

Monitor the terminal output for real-time logs and error messages.

## 🆘 Troubleshooting

### Common Issues

1. **Port Already in Use**

   ```bash
   pkill -f streamlit
   ./start_unified_platform.sh
   ```

2. **Module Import Errors**

   ```bash
   pip install -r requirements.txt
   ```

3. **Navigation Issues**
   - Refresh the browser
   - Clear browser cache
   - Use the sidebar navigation

### Support

- Check the terminal output for detailed error messages
- Verify all dependencies are installed
- Ensure proper file permissions

## 🎉 Success!

Your unified Qubic SmartGuard Platform is now ready! Access it at:
**http://localhost:8501**

Switch seamlessly between smart contract auditing and decentralized voting using the professional interface.
