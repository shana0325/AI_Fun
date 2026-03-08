import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("AI Knowledge Assistant")

# 初始化聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = []

# -----------------------
# Sidebar (文档管理)
# -----------------------

with st.sidebar:

    st.header("Documents")

    uploaded_file = st.file_uploader(
        "Upload a document",
        type=["txt", "pdf"],
        key="upload_file"
    )

    if uploaded_file is not None:

        if uploaded_file.name not in st.session_state.documents:

            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue())
            }

            with st.spinner("Uploading document..."):

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

            if response.ok:
                st.session_state.documents.append(uploaded_file.name)

                st.success("Document uploaded!")


    st.divider()

    st.subheader("Loaded documents")

    for doc in st.session_state.documents:
        st.write("📄", doc)

# -----------------------
# Chat area
# -----------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question")

if prompt:

    # 用户消息
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # 调用API
    with st.spinner("Thinking..."):

        response = requests.post(
            f"{API_URL}/ask",
            json={"question": prompt}
        )

        answer = response.json()["answer"]

    # AI回答
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )