import os
import json
from PIL import Image

import google.generativeai as genai

# working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# path of config_data file
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open("config.json"))

# loading the GOOGLE_API_KEY
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# configuring google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

# System prompt for Oracle agent
ORACLE_SYSTEM = (
    "You are an Oracle expert agent. "
    "Use the provided Oracle docs online and online info to answer. "
    "Prefer Oracle Database 23ai, OCI, Fusion Apps, and MySQL HeatWave. "
    "If unsure, say you don’t know."
)

def oracle_agent_response(user_prompt):
    gemini_model = genai.GenerativeModel("gemini-2.0-flash-001")
    full_prompt = f"{ORACLE_SYSTEM}\n\nQuestion:\n{user_prompt}"
    response = gemini_model.generate_content(full_prompt)
    return response.text


# get response from Gemini-Pro-Vision model - image/text to text
def gemini_flash_vision_response(prompt, image):
    gemini_flash_vision_model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = gemini_flash_vision_model.generate_content([prompt, image])
    result = response.text
    return result


# get response from Gemini-Pro model - text to text
ORACLE_TROUBLESHOOT_PROMPT = ("""
You are an Oracle troubleshooting assistant. 
When I describe an error, performance problem, or configuration issue, 
analyze it as an Oracle support engineer would. 

1. Identify the probable causes.
2. Suggest step-by-step troubleshooting actions.
3. Provide Oracle best practices to prevent it in the future.
4. If it's a known Oracle error code (ORA-XXXX), explain it clearly.
""")

def oracle_troubleshooter_response(user_prompt):
    gemini_model = genai.GenerativeModel("gemini-2.0-flash-001")
    full_prompt = f"{ORACLE_TROUBLESHOOT_PROMPT}\n\nQuestion:\n{user_prompt}"
    response = gemini_model.generate_content(full_prompt)

    return response.text








