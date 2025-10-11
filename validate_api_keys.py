#!/usr/bin/env python3
"""
API Key Validation Script for Qubic SmartGuard
Tests all configured API keys to ensure they're working properly
"""

import os
import sys

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def test_groq_api():
    """Test GROQ API connectivity"""
    try:
        from langchain_groq import ChatGroq

        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            return False, "GROQ_API_KEY not found in environment"

        # Initialize GROQ client
        llm = ChatGroq(
            model="llama3-70b-8192",
            api_key=api_key,
            temperature=0
        )

        # Test simple query
        response = llm.invoke("Hello, respond with 'GROQ API Working'")

        if "GROQ API Working" in response.content:
            return True, f"✅ GROQ API Working - Response: " + \
                f"{response.content[:50]}..."
        else:
            return True, f"✅ GROQ API Connected - Response: " + \
                f"{response.content[:50]}..."

    except Exception as e:
        return False, f"❌ GROQ API Error: {str(e)}"


def test_openai_api():
    """Test OpenAI API connectivity"""
    try:
        from openai import OpenAI

        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return False, "OPENAI_API_KEY not found in environment"

        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)

        # Test simple query
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Respond with 'OpenAI API Working'"}],
            max_tokens=10
        )

        content = response.choices[0].message.content
        if "OpenAI API Working" in content:
            return True, f"✅ OpenAI API Working - Response: {content}"
        else:
            return True, f"✅ OpenAI API Connected - Response: {content}"

    except Exception as e:
        return False, f"❌ OpenAI API Error: {str(e)}"


def test_langchain_tracing():
    """Test LangChain tracing setup"""
    try:
        api_key = os.getenv('LANGCHAIN_API_KEY')
        if not api_key:
            return False, "LANGCHAIN_API_KEY not found in environment"

        # Set LangChain environment variables
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "qubic-smartguard"

        return True, "✅ LangChain tracing configured"

    except Exception as e:
        return False, f"❌ LangChain setup error: {str(e)}"


def main():
    """Run all API validation tests"""
    print("🔑 Qubic SmartGuard - API Key Validation")
    print("=" * 50)

    tests = [
        ("GROQ API", test_groq_api),
        ("OpenAI API", test_openai_api),
        ("LangChain Tracing", test_langchain_tracing)
    ]

    results = []

    for test_name, test_func in tests:
        print(f"\n🧪 Testing {test_name}...")
        success, message = test_func()
        results.append((test_name, success, message))
        print(f"   {message}")

    print("\n" + "=" * 50)
    print("📋 VALIDATION SUMMARY:")
    print("=" * 50)

    all_passed = True
    for test_name, success, message in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if not success:
            all_passed = False

    print(
        f"\n🎯 Overall Status: {'✅ ALL SYSTEMS GO!' if all_passed else '⚠️ SOME ISSUES DETECTED'}")

    if all_passed:
        print("\n🚀 Ready to test enhanced LLM functionality!")
        print("   Run: python test_enhanced_security.py")
        print("   Or start the web interface: streamlit run app.py")
    else:
        print("\n🔧 Please check the failed API keys and try again.")

    return all_passed


if __name__ == "__main__":
    main()
