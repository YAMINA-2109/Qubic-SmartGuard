import logging
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Set up API keys
groq_api_key = os.getenv("GROQ_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key
    logger.info("✅ Groq API key loaded successfully")
else:
    logger.warning("⚠️ GROQ_API_KEY not found. Using fallback mode.")

if langchain_api_key:
    os.environ["LANGSMITH_API_KEY"] = langchain_api_key
    logger.info("✅ LangChain API key loaded successfully")

# Configuration flags
enable_llm = os.getenv("ENABLE_LLM_ANALYSIS", "true").lower() == "true"
ENABLE_DEBUG_MODE = os.getenv("ENABLE_DEBUG_MODE", "false").lower() == "true"


def create_llm_with_fallback(model_name: str, fallback_model: str = None):
    """Create LLM instance with fallback handling"""
    try:
        if not groq_api_key:
            logger.warning(f"⚠️ No API key available for {model_name}")
            return None

        llm = ChatGroq(model=model_name, temperature=0.1)

        # Test the connection
        if ENABLE_DEBUG_MODE:
            logger.info(f"✅ {model_name} initialized successfully")

        return llm

    except Exception as e:
        logger.error(f"❌ Failed to initialize {model_name}: {str(e)}")

        if fallback_model:
            try:
                logger.info(f"🔄 Trying fallback model: {fallback_model}")
                return ChatGroq(model=fallback_model, temperature=0.1)
            except Exception as fallback_error:
                logger.error(f"❌ Fallback model failed: {str(fallback_error)}")

        return None


# Initialize LLMs with fallbacks
llm_vision = create_llm_with_fallback("llama3-70b-8192",
                                      "llama-3.1-8b-instant")
llm_reviewer = create_llm_with_fallback("llama-3.1-8b-instant",
                                        "llama3-8b-8192")
llm_doc = create_llm_with_fallback("deepseek-r1-distill-llama-70b",
                                   "llama3-70b-8192")

# Check if any LLMs are available
available_llms = sum(1 for llm in [llm_vision, llm_reviewer, llm_doc]
                     if llm is not None)

if available_llms == 0:
    logger.warning("⚠️ No LLMs available. Using fallback mode only.")
elif available_llms < 3:
    logger.warning(f"⚠️ Only {available_llms}/3 LLMs available. "
                   "Some features may be limited.")
else:
    logger.info("✅ All LLMs initialized successfully")


def get_available_llm():
    """Get the first available LLM for analysis"""
    for llm in [llm_vision, llm_reviewer, llm_doc]:
        if llm is not None:
            return llm
    return None


def is_llm_available():
    """Check if any LLM is available"""
    return available_llms > 0
