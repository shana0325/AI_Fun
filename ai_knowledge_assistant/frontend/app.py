import streamlit as st
import requests

# 后端 FastAPI 地址。
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("AI Knowledge Assistant")

# 初始化聊天记录状态。
if "messages" not in st.session_state:
    st.session_state.messages = []

# 初始化已加载文档列表状态。
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

        # 避免重复上传同名文件。
        if uploaded_file.name not in st.session_state.documents:

            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue())
            }

            # 调用后端上传接口。
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

    # 展示当前会话中已上传的文档。
    for doc in st.session_state.documents:
        st.write("📄", doc)

# -----------------------
# Chat area
# -----------------------

# 回放历史消息。
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question")

if prompt:

    # 记录并展示用户消息。
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # 调用后端问答接口。
    with st.spinner("Thinking..."):

        response = requests.post(
            f"{API_URL}/ask",
            json={"question": prompt}
        )

        answer = response.json()["answer"]

    # 展示并记录 AI 回答。
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )