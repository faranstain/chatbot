# streamlit_app.py
import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Gemini AI Chat Interface",
    page_icon="🤖",
    layout="wide"
)

def get_ai_response(user_query: str) -> str:
    """Make API call to FastAPI endpoint"""
    try:
        response = requests.post(
            "http://localhost:8008/generate",
            json={"user_query": user_query},
            timeout=30
        )
        response.raise_for_status()
        return response.json()["llm_response"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def main():
    st.title("🤖 Gemini AI Assistant")
    st.markdown("---")

    # Session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's your question?"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get and display AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ai_response(prompt)
                st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Sidebar
    with st.sidebar:
        st.title("About")
        st.markdown("""
        This is a Gemini AI chat interface that helps you:
        - Get answers to your questions
        - Generate creative content
        - Solve problems
        
        Simply type your question in the chat box and press Enter!
        """)

        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()

    