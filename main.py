import os
import requests

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


from gemini_utility import (oracle_agent_response,
                            gemini_flash_vision_response,
                            oracle_troubleshooter_response)

# -------------------- Setup --------------------
working_dir = os.path.dirname(os.path.abspath(__file__))

# -------------------- Lottie Function --------------------
def load_lottie_url(url: str):
    response = requests.get(url)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ Failed to parse JSON from URL.")
        print("Response content:", response.text[:200])
        return None

# -------------------- Lottie Animations --------------------
chat_json = load_lottie_url("https://lottie.host/efaed900-e918-4778-af6c-359ec067e84e/dqIieJEJzJ.json")
cloud_json = load_lottie_url("https://lottie.host/798bb927-01a8-4f9a-bc23-8d50b166a170/V3b2YcztwS.json")
ERD_json = load_lottie_url("https://lottie.host/50d2d893-14c1-405a-84b0-686c359942a1/nhDWk8fppg.json")
trouble_json = load_lottie_url("https://lottie.host/7344898f-9d17-4873-b74a-3c14ef8f4dad/LJUpqUrLtf.json")
# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="OracAI",
    page_icon="⭕",
    layout="centered",
)

# -------------------- Sidebar --------------------
with st.sidebar:
    selected = option_menu(
        'OracAI',
        [
            'ChatBot',
            'ERD Diagram Interpreter',
            'Cloud Architecture Diagram Assistant',
            'Oracle Troubleshooter'
        ],
        menu_icon='cpu',  # main sidebar icon
        icons=[
            'chat-dots-fill',       # ChatBot → 💬
            'diagram-3-fill',       # ERD Interpreter → database diagram
            'cloud-arrow-up-fill',  # Cloud Architecture Assistant → cloud infra
            'question-circle-fill'  # Ask me anything → ❓
        ],
        default_index=0
    )


# -------------------- ChatBot Page --------------------
if selected == 'ChatBot':
    st.title("⭕Oracle ChatBot")

    if chat_json:
        st_lottie(chat_json, speed=1, loop=True, height=400)
    else:
        st.error("❌ Failed to load animation.")

    # Function to translate roles between Gemini-flash and Streamlit terminology
    def translate_role_for_streamlit(user_role):
        if user_role == "model":
            return "assistant"
        else:
            return user_role

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    # Input field
    user_prompt = st.chat_input("Ask the Oracle Assistant...")
    if user_prompt:
        st.session_state.chat_history.append(("user", user_prompt))
        with st.chat_message("user"):
            st.markdown(user_prompt)

        ans = oracle_agent_response(user_prompt)

        st.session_state.chat_history.append(("assistant", ans))
        with st.chat_message("assistant"):
            st.markdown(ans)


# -------------------- ERD Diagram Interpreter Page --------------------
if selected == "ERD Diagram Interpreter":

    st.title("🛢️ ERD Diagram Interpreter")


    if ERD_json:
        st_lottie(ERD_json, speed=1, loop=True, height=250)
    else:
        st.error("❌ Failed to load animation.")

    uploaded_image = st.file_uploader("Upload an ERD image to get a clear explanation of its entities, keys, and relationships for Oracle Database", type=["jpg", "jpeg", "png"])


    if st.button("Explain the ERD"):
        image = Image.open(uploaded_image)

        st.image(image)

        default_prompt = """
                You are an Oracle Database expert specializing in Entity-Relationship Diagrams (ERDs). 
                When I give you an ERD image, carefully analyze it and:
                1. Identify the entities (tables).
                2. List their attributes (columns).
                3. Explain the primary keys and foreign keys.
                4. Describe the relationships (one-to-one, one-to-many, many-to-many).
                5. Suggest how this ERD could be implemented in Oracle Database using CREATE TABLE statements.
                6. Give practical insights on normalization, data integrity, and how this schema could support business use cases.
                
                Be detailed, clear, and explain as if you are teaching a junior Oracle DBA.
                If parts of the image are unclear, state your assumptions explicitly.
                """


        Explanation = gemini_flash_vision_response(default_prompt, image)

        st.info(Explanation)

# -------------------- Cloud Architecture Diagram Assistant Page --------------------
if selected == "Cloud Architecture Diagram Assistant":


    st.title("☁️️ Cloud Architecture Diagram Assistant")

    if cloud_json:
        st_lottie(cloud_json, speed=1, loop=True, height=250)
    else:
        st.error("❌ Failed to load animation.")

    uploaded_image = st.file_uploader("Upload a cloud diagram to see its components, data flow, and deployment best practices on Oracle Cloud", type=["jpg", "jpeg", "png"])

    if st.button("Explain the Diagram"):
        image = Image.open(uploaded_image)

        st.image(image, use_container_width=False, caption=" ", output_format="PNG")

        default_prompt = """
            You are an Oracle Cloud Infrastructure (OCI) expert specializing in Cloud Architecture Diagrams. 
            When I give you a cloud architecture diagram, carefully analyze it and:
            
            1. Identify the main components (compute instances, databases, networking, storage, load balancers, etc.).
            2. Explain how these components are connected and how data flows between them.
            3. Highlight best practices for security, scalability, and high availability in OCI.
            4. Suggest improvements if the architecture has weaknesses (e.g., missing redundancy, security gaps).
            5. Map each component to the proper OCI service (e.g., Autonomous Database, Exadata, Block Storage, VCN, Load Balancer, Identity & Access Management).
            6. Provide a step-by-step explanation of how this architecture could be deployed on OCI.
            7. Give practical insights about cost efficiency, performance tuning, and region/availability domain considerations.
            
            Be detailed, clear, and explain as if you are teaching a junior Oracle Cloud Architect.  
            If parts of the diagram are unclear, state your assumptions explicitly.
            """

        Explanation_C = gemini_flash_vision_response(default_prompt, image)

        st.info(Explanation_C)


# -------------------- Oracle Troubleshooter Page --------------------
if selected == "Oracle Troubleshooter":

    st.title("❓ Oracle Troubleshooter")

    if trouble_json:
        st_lottie(trouble_json, speed=1, loop=True, height=300)
    else:
        st.error("❌ Failed to load animation.")

    # text box to enter prompt

    user_prompt = st.text_area(label='Describe your Oracle issue, and the assistant will analyze possible causes and suggest step-by-step solutions', placeholder="Ask me anything...")

    if st.button("Get Response"):
        response = oracle_troubleshooter_response(user_prompt)
        st.markdown(response)




