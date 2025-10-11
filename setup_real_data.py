#!/usr/bin/env python3
"""
Configuration Setup Guide for Real Qubic Data
Run this to check your configuration and get setup instructions
"""

import os

from dotenv import load_dotenv

load_dotenv()


def print_header(title):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def check_api_config(name, env_var, status_emoji):
    value = os.getenv(env_var)
    if value:
        masked = value[:10] + "..." if len(value) > 10 else value
        print(f"  {status_emoji} {name:30s} = {masked}")
        return True
    else:
        print(f"  ❌ {name:30s} = NOT SET")
        return False


def main():
    print_header("🛡️  QUBIC SMARTGUARD - CONFIGURATION CHECK")

    # Check LLM APIs (Working)
    print_header("✅ AI ANALYSIS APIs (Currently Working)")
    groq = check_api_config("GROQ API Key", "GROQ_API_KEY", "✅")
    langchain = check_api_config("LangChain API Key", "LANGCHAIN_API_KEY", "✅")
    openai = check_api_config("OpenAI API Key", "OPENAI_API_KEY", "⚠️")

    # Check Qubic Network APIs (Needed)
    print_header("❌ QUBIC NETWORK APIs (REQUIRED FOR REAL DATA)")
    qubic_rpc = check_api_config(
        "Qubic RPC Endpoint", "QUBIC_RPC_ENDPOINT", "❌")
    qubic_explorer = check_api_config(
        "Qubic Explorer API", "QUBIC_EXPLORER_API", "❌")
    qubic_archive = check_api_config(
        "Qubic Archive API", "QUBIC_ARCHIVE_API", "❌")
    qubic_key = check_api_config("Qubic API Key", "QUBIC_API_KEY", "ℹ️")

    # Check Database (Needed)
    print_header("❌ DATABASE CONFIGURATION (NEEDED FOR ACTIVITY TRACKING)")
    database = check_api_config("PostgreSQL URL", "DATABASE_URL", "❌")
    redis = check_api_config("Redis URL", "REDIS_URL", "❌")

    # Check Market Data APIs (Optional)
    print_header("ℹ️  MARKET DATA APIs (Optional)")
    coingecko = check_api_config("CoinGecko API", "COINGECKO_API_KEY", "ℹ️")
    cmc = check_api_config("CoinMarketCap API", "COINMARKETCAP_API_KEY", "ℹ️")

    # Summary
    print_header("📊 CONFIGURATION SUMMARY")

    ai_working = groq or langchain
    qubic_working = qubic_rpc or qubic_explorer
    db_working = database

    print(
        f"\n  AI Security Analysis:  {'🟢 WORKING' if ai_working else '🔴 NOT WORKING'}")
    print(
        f"  Qubic Real Data:       {'🟢 CONFIGURED' if qubic_working else '🔴 NOT CONFIGURED'}")
    print(
        f"  Database Tracking:     {'🟢 CONFIGURED' if db_working else '🔴 NOT CONFIGURED'}")

    # Instructions
    print_header("📋 WHAT'S WORKING vs WHAT'S FAKE")

    print("\n  ✅ REAL (Currently Working):")
    print("     • Smart Contract AI Security Analysis (GROQ API)")
    print("     • Vulnerability Pattern Detection")
    print("     • LLM-powered Code Review")

    print("\n  ❌ FAKE/AI-GENERATED (Needs Configuration):")
    print("     • Activity Feed - Random generated, not from real events")
    print("     • Burn Transaction Data - AI-generated numbers")
    print("     • High-Value Transactions - Fake random data")
    print("     • Production Status - Fake holder count & market cap")
    print("     • Voting Results - Simulated votes, not on blockchain")

    print_header("🔧 HOW TO FIX - GET REAL DATA")

    if not qubic_working:
        print("\n  STEP 1: Get Qubic Network Access")
        print("  " + "-" * 76)
        print("  You need to configure Qubic blockchain endpoints in .env file:")
        print()
        print("  Option A: Use Qubic.li (Recommended)")
        print("     QUBIC_RPC_ENDPOINT=https://api.qubic.li")
        print("     QUBIC_EXPLORER_API=https://api.qubic.li/v1")
        print()
        print("  Option B: Use Official Qubic RPC")
        print("     QUBIC_RPC_ENDPOINT=https://rpc.qubic.org")
        print("     # Check Qubic documentation for correct endpoints")
        print()
        print("  Option C: Run Your Own Node")
        print("     QUBIC_RPC_ENDPOINT=http://localhost:21841")
        print()
        print("  📚 Resources:")
        print("     • Qubic Documentation: https://docs.qubic.org")
        print("     • Qubic.li API: https://doc.qubic.li")
        print("     • Qubic Explorer: https://explorer.qubic.org")

    if not db_working:
        print("\n  STEP 2: Set Up Database for Activity Tracking")
        print("  " + "-" * 76)
        print("  Install PostgreSQL:")
        print("     sudo apt install postgresql postgresql-contrib")
        print("     pip install psycopg2-binary sqlalchemy")
        print()
        print("  Create database:")
        print("     sudo -u postgres createdb smartguard")
        print("     sudo -u postgres createuser smartguard -P")
        print()
        print("  Add to .env:")
        print(
            "     DATABASE_URL=postgresql://smartguard:password@localhost:5432/smartguard")
        print()
        print("  Optional - Redis for caching:")
        print("     sudo apt install redis-server")
        print("     REDIS_URL=redis://localhost:6379/0")

    print("\n  STEP 3: Restart Application")
    print("  " + "-" * 76)
    print("  After configuring .env, restart Streamlit:")
    print("     streamlit run main_app.py")
    print()

    print_header("🎯 CURRENT STATUS")

    if ai_working and qubic_working and db_working:
        print("\n  🎉 PERFECT! All systems configured for real data!")
        print("     Your app will show 100% real blockchain data.")
    elif ai_working and qubic_working:
        print("\n  🟡 PARTIAL: AI + Network working, but missing database")
        print("     You'll get real network data but no activity tracking.")
    elif ai_working:
        print("\n  🔴 DEMO MODE: Only AI analysis working")
        print("     Everything else is fake AI-generated data.")
        print("     Configure Qubic endpoints to get real blockchain data!")
    else:
        print("\n  ⚠️  WARNING: No APIs configured!")
        print("     Application running in full demo mode.")

    print("\n" + "=" * 80)
    print("  💡 Tip: Uncomment the API lines in .env and add your credentials")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
