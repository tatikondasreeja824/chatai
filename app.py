
import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

/* Main title */
h1 {
    color: #00e5ff;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

/* Description */
p {
    color: #e0e0e0;
    text-align: center;
    font-size: 18px;
}

/* Input box */
.stTextInput input {
    background-color: #ffffff;
    color: #222222;
    border-radius: 12px;
    padding: 12px;
    border: 2px solid #00e5ff;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
}

/* Button hover effect */
.stButton > button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    transform: scale(1.03);
    color: white;
    border: none;
}

/* Response box */
.response-box {
    background-color: #ffffff;
    color: #222222;
    padding: 22px;
    border-radius: 15px;
    border-left: 6px solid #00e5ff;
    margin-top: 20px;
    font-size: 17px;
    line-height: 1.6;
}

/* Footer */
.footer {
    text-align: center;
    color: #bbbbbb;
    font-size: 14px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# App UI
st.title("🤖 Friendly AI Bot")
st.write("✨ Your friendly AI assistant — Ask me anything!")

question = st.text_input("💬 Enter your question")

if st.button("🚀 Ask AI"):
    if question.strip():
        with st.spinner("🤔 Thinking..."):
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a friendly and funny AI assistant.
                        Explain things in simple language.
                        Be helpful and encouraging.
                        """
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]

        st.markdown("### 💡 AI Response")
        st.markdown(
            f'<div class="response-box">{answer}</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a question first!")

st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit and Ollama</div>',
    unsafe_allow_html=True
)