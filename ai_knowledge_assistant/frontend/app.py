import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")
st.title("AI Knowledge Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = []


with st.sidebar:
    st.header("📚 Knowledge Base")

    uploaded_file = st.file_uploader(
        "Upload document",
        type=["txt", "pdf"],
        key="upload_file",
    )

    if uploaded_file is not None:
        if uploaded_file.name not in st.session_state.documents:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}

            with st.spinner("Uploading document..."):
                response = requests.post(f"{API_URL}/upload", files=files)

            if response.ok:
                st.session_state.documents.append(uploaded_file.name)
                st.success("Document indexed!")

    st.divider()
    st.subheader("Documents")

    if len(st.session_state.documents) == 0:
        st.write("No documents uploaded")
    else:
        for doc in st.session_state.documents:
            col1, col2 = st.columns([4, 1])

            with col1:
                st.write("📄", doc)

            with col2:
                if st.button("❌", key=f"delete_{doc}"):
                    st.session_state.documents.remove(doc)
                    st.rerun()


def render_sources(sources):
    if len(sources) > 0:
        st.markdown("**Sources:**")

        for i, src in enumerate(sources):
            source_name = str(src.get("source", "unknown")).split("/")[-1].split("\\")[-1]

            with st.expander(f"📄 {source_name} (chunk {i + 1})"):
                st.write(src.get("text", ""))


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        if msg["role"] == "assistant":
            render_sources(msg.get("sources", []))


prompt = st.chat_input("Ask a question")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        response = requests.post(f"{API_URL}/ask", json={"question": prompt})
        data = response.json()

        answer = data["answer"]
        sources = data["sources"]

    with st.chat_message("assistant"):
        st.markdown(answer)
        render_sources(sources)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )