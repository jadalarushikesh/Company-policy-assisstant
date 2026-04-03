import streamlit as st
from src.rag_chat import rag_graph

# Page config
st.set_page_config(page_title="Company Policy Assistant")

# Title
st.title("📄 Company Policy Assistant")

# -------------------
# Chat history
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------
# Input
# -------------------
question = st.chat_input("Ask your policy question...")

if question:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    # Get response
    result = rag_graph.invoke({
        "question": question
    })

    answer = result["answer"]

    # Show assistant response
    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )