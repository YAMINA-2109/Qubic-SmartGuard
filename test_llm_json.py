#!/usr/bin/env python3
"""
Test LLM response parsing to fix JSON issues
"""

from langgraphagenticai.LLMS.groqllm import llm_vision
from langchain.schema import HumanMessage
import os
import sys

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def test_llm_json_parsing():
    """Test LLM JSON response parsing"""

    print("🧪 Testing LLM JSON Response Parsing")
    print("=" * 50)

    simple_prompt = """
Analyze this simple code for vulnerabilities and respond in JSON:

```cpp
struct { uint8 balance; } state;
PUBLIC_PROCEDURE(test) { state.balance = 5; }
```

Respond only with valid JSON in this format:
{
    "critical_vulnerabilities": [],
    "high_risk_issues": [
        {
            "type": "Integer Overflow Risk",
            "severity": "HIGH", 
            "description": "Uses uint8 type"
        }
    ],
    "medium_risk_issues": [],
    "low_risk_issues": []
}
"""

    try:
        message = HumanMessage(content=simple_prompt)
        response = llm_vision.invoke([message])

        print("📝 Raw LLM Response:")
        print("-" * 30)
        print(response.content)
        print("-" * 30)

        # Try to extract JSON
        response_text = response.content
        if '```json' in response_text:
            json_part = response_text.split('```json')[1].split('```')[0]
            print("\n🔍 Extracted JSON Part:")
            print(json_part)
        elif '{' in response_text and '}' in response_text:
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            json_part = response_text[start:end]
            print("\n🔍 Extracted JSON Part:")
            print(json_part)
        else:
            print("\n❌ No JSON structure found in response")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    test_llm_json_parsing()
