from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


# set up api keys
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# LLMs
# llm_vision=ChatGroq(model="llama-3.2-90b-vision-preview")
llm_vision=ChatGroq(model="llama3-70b-8192")
llm_reviewer = ChatGroq(model="llama-3.1-8b-instant")
llm_doc = ChatGroq(model="deepseek-r1-distill-llama-70b")
