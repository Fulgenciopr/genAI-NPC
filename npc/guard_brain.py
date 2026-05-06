from groq import Groq
import os
import json 
from dotenv import load_dotenv
import npc_prompts.prompts

load_dotenv()

ai_model = "openai/gpt-oss-20b"
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)

chat_completion = client.chat.completions.create(
    model = ai_model,

    messages = [
        {"role": "system", "content": "test"},
        {"role": "user", "content": "test"}
    ], 

    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "guard_brain",
            "schema": {
                "type": "object",
                "properties": {
                    "response": {"type": "string"},
                    "trust": {"type": "number"},
                    "sentiment" :{"type": "string",
                                  "enum": ["very positive", "positive", "neutral", "negative", "very negative"]},
                },
                "required": ["response", "trust", "sentiment"],
            }
        }
    },

    
)