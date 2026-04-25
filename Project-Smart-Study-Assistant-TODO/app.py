"""Smart Study Assistant — Streamlit UI
Phase 7: Add a web interface to your CLI project.

Run with: streamlit run app.py
"""
import streamlit as st
import os

# Page config (this one's free — it just sets the browser tab title)
st.set_page_config(
    page_title="Smart Study Assistant",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# TODO 22: Create the sidebar
# ============================================================
# Build a sidebar with:
#   - A title: st.sidebar.title(...)
#   - A mode selector: st.sidebar.radio("Select Mode:", [...options...])
#     Options: "💬 Ask (RAG)", "🤖 Agent Mode", "📝 Summarize", "🃏 Flashcards", "❓ Quiz"
#   - A file uploader: st.sidebar.file_uploader("Upload notes", type=["txt"])
#   - A re-index button: st.sidebar.button("🔄 Re-index Notes")
#
# Store each in a variable: mode, uploaded_file, reindex_button
#
# Antigravity prompt: "Add a Streamlit sidebar with a title, a radio
#   button for mode selection with 5 options, a txt file uploader,
#   and a re-index button. Store each widget's return value in a variable."

mode = None           # Replace with st.sidebar.radio(...)
uploaded_file = None  # Replace with st.sidebar.file_uploader(...)
reindex_button = None # Replace with st.sidebar.button(...)


# ============================================================
# TODO 23: Initialize session state
# ============================================================
# Streamlit re-runs the script on every interaction. Without session
# state, your chat history and loaded models would vanish each time.
#
# Initialize these variables (only if they don't exist yet):
#   st.session_state.messages     = []     (chat history)
#   st.session_state.vectorstore  = None
#   st.session_state.rag_chain    = None
#   st.session_state.agent        = None
#   st.session_state.ready        = False
#
# Pattern:
#   if "messages" not in st.session_state:
#       st.session_state.messages = []
#
# Antigravity prompt: "Initialize 5 Streamlit session state variables
#   if they don't already exist: messages (empty list), vectorstore (None),
#   rag_chain (None), agent (None), ready (False)."

pass  # Replace with session state initialization


# ============================================================
# TODO 24: Load the study assistant on first run
# ============================================================
# When st.session_state.ready is False:
#   1. Show a loading message with st.info("Loading...")
#   2. Import your modules: loader, vectorstore, retriever, agent
#   3. Load or create vectorstore (check if ./chroma_db exists)
#   4. Build RAG chain: retriever.build_rag_chain(vs)
#   5. Create agent: agent.create_study_agent()
#   6. Save everything to session_state
#   7. Set ready = True, show st.success("Ready!")
#
# Wrap it in try/except — show errors with st.error()
#
# Antigravity prompt: "Write a startup block that runs when
#   st.session_state.ready is False. It should import loader,
#   vectorstore, retriever, and agent modules. Check if ./chroma_db
#   exists — if yes call load_vectorstore(), if no call load_and_chunk
#   then create_vectorstore. Build the RAG chain and create the agent.
#   Store everything in session_state and set ready=True. Use try/except."

pass  # Replace with loading logic


# ============================================================
# Main Chat Area
# ============================================================
st.title("📚 Smart Study Assistant")


# ============================================================
# TODO 25: Display chat history
# ============================================================
# Loop through st.session_state.messages and show each one.
#
# Pattern:
#   for msg in st.session_state.messages:
#       with st.chat_message(msg["role"]):
#           st.markdown(msg["content"])
#
# Antigravity prompt: "Display all messages from
#   st.session_state.messages using st.chat_message for each one."

pass  # Replace with chat history display


# ============================================================
# TODO 26: Handle user input (THE BIG ONE)
# ============================================================
# This is where everything comes together.
#
# 1. Create chat input: user_input = st.chat_input("Ask me anything...")
# 2. If user typed something AND st.session_state.ready:
#    a. Append {"role": "user", "content": user_input} to messages
#    b. Display user message with st.chat_message("user")
#    c. Use st.spinner("Thinking...") while processing
#    d. Based on the 'mode' variable from TODO 22:
#       - "Ask (RAG)":    answer = st.session_state.rag_chain.invoke(user_input)
#       - "Agent Mode":   from agent import chat_with_agent; answer = chat_with_agent(...)
#       - "Summarize":    from tools import summarize_topic; answer = summarize_topic.invoke(...)
#       - "Flashcards":   from tools import generate_flashcards; answer = generate_flashcards.invoke(...)
#       - "Quiz":         from tools import quiz_me; answer = quiz_me.invoke(...)
#    e. Display assistant response with st.chat_message("assistant")
#    f. Append {"role": "assistant", "content": answer} to messages
#
# Antigravity prompt: "Create a st.chat_input handler. When the user
#   types something, add it to session_state.messages, display it,
#   then based on a 'mode' variable route to different handlers:
#   RAG mode calls rag_chain.invoke, Agent mode calls chat_with_agent,
#   Summarize calls summarize_topic.invoke, Flashcards calls
#   generate_flashcards.invoke, Quiz calls quiz_me.invoke. Show a
#   spinner while processing. Add the response to messages and display it.
#   Use try/except for error handling."

pass  # Replace with chat input handler


# ============================================================
# TODO 27: Show retrieved sources (RAG mode only)
# ============================================================
# When in RAG mode, show an expander with the source chunks.
#
# Pattern:
#   if mode has "RAG" and st.session_state.ready:
#       with st.expander("📄 Retrieved Sources"):
#           docs = st.session_state.vectorstore.similarity_search(last_question, k=3)
#           for doc in docs: st.markdown(doc.page_content[:200])
#
# Antigravity prompt: "Add a Streamlit expander that shows retrieved
#   source documents. Only show it when in RAG mode. Get the last user
#   message from session_state.messages, run similarity_search on the
#   vectorstore, and display each chunk's first 200 characters."

pass  # Replace with sources expander


# ============================================================
# TODO 28: Handle re-index button
# ============================================================
# When reindex_button is clicked:
#   1. Delete ./chroma_db folder (import shutil; shutil.rmtree(...))
#   2. Reset all session_state variables to None/empty
#   3. Call st.rerun() to restart the script
#
# Antigravity prompt: "Handle a reindex button click. Delete the
#   ./chroma_db directory with shutil.rmtree, reset all session state
#   variables (vectorstore, rag_chain, agent, ready, messages) to their
#   defaults, show a success message, and call st.rerun()."

pass  # Replace with re-index handler


# --- Footer ---
st.markdown("---")
st.caption("Smart Study Assistant • Built with Streamlit + LangChain + Gemini")
