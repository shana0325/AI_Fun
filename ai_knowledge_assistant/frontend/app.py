import streamlit as st
import requests

# 后端 FastAPI 地址
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("AI Knowledge Assistant")

# 初始化聊天记录状态
if "messages" not in st.session_state:
    st.session_state.messages = []

# 初始化已加载文档列表状态
if "documents" not in st.session_state:
    st.session_state.documents = []

# -----------------------
# Sidebar (知识库管理)
# -----------------------

with st.sidebar:

    st.header("📁 Knowledge Base")

    # 文件上传组件
    uploaded_file = st.file_uploader(
        "Upload document",
        type=["txt", "pdf"],
        key="upload_file"
    )

    # 如果用户上传文件
    if uploaded_file is not None:

        # 防止重复上传同一个文件
        if uploaded_file.name not in st.session_state.documents:

            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue())
            }

            with st.spinner("Uploading document..."):

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

            # 上传成功
            if response.ok:

                st.session_state.documents.append(uploaded_file.name)

                st.success("Document indexed!")

    st.divider()

    st.subheader("Documents")

    # 如果没有文档
    if len(st.session_state.documents) == 0:

        st.write("No documents uploaded")

    # 显示文档列表
    else:

        for doc in st.session_state.documents:

            col1, col2 = st.columns([4, 1])

            with col1:
                st.write("📄", doc)

            with col2:

                # 删除文档按钮（目前只删除 UI 中的记录）
                if st.button("❌", key=f"delete_{doc}"):

                    st.session_state.documents.remove(doc)

                    st.rerun()

# -----------------------
# Chat area
# -----------------------

# 回放历史聊天记录
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 用户输入问题
prompt = st.chat_input("Ask a question")

if prompt:

    # 记录用户消息
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)

    # 调用后端问答接口
    with st.spinner("Thinking..."):

        response = requests.post(
            f"{API_URL}/ask",
            json={"question": prompt}
        )

        # 解析 API 返回
        data = response.json()

        answer = data["answer"]
        sources = data["sources"]

    # 显示 AI 回复
    with st.chat_message("assistant"):

        st.markdown(answer)

        # -----------------------
        # 显示 Sources
        # -----------------------

        if len(sources) > 0:

            st.markdown("**Sources:**")

            # 用 set 防止同一个文档重复显示
            sources_seen = set()

            for src in sources:

                # 提取文件名
                source_name = src["source"].split("/")[-1]

                if source_name not in sources_seen:

                    st.markdown(f"- 📄 {source_name}")

                    sources_seen.add(source_name)

    # 记录 AI 回复
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )