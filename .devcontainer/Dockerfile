# Use Python 3.11 as base image
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    wget \
    vim \
    nano \
    htop \
    tree \
    jq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js for additional tooling
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs

# Set working directory
WORKDIR /workspace

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# Create necessary directories
RUN mkdir -p /workspace/files /workspace/src /workspace/.streamlit

# Set environment variables
ENV PYTHONPATH=/workspace:/workspace/src
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose ports
EXPOSE 8501 3000 5000

# Set default user
USER vscode

# Default command
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
