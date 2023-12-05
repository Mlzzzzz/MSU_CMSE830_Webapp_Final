import streamlit as st
from similarity_webapp_start_page import start_page
from similarity_webapp_page1 import page1
from similarity_webapp_page2 import page2
from similarity_webapp_page3 import page3
from similarity_webapp_page4 import page4
from similarity_webapp_page5 import page5
from similarity_webapp_page6 import page6

if 'current_page' not in st.session_state:
    st.session_state.current_page = start_page
    st.session_state.on_start_page = True

def show_sidebar():
    if st.sidebar.button("Introduction of the Dataset"):
        st.session_state.current_page = page1
        st.session_state.on_start_page = False

    if st.sidebar.button("Distribution of Attributes"):
        st.session_state.current_page = page2
        st.session_state.on_start_page = False

    if st.sidebar.button("Relationships of Attributes"):
        st.session_state.current_page = page3
        st.session_state.on_start_page = False

    if st.sidebar.button("Misclassified Molecular Pairs in the Original Work"):
        st.session_state.current_page = page4
        st.session_state.on_start_page = False

    if st.sidebar.button("Model Analysis"):
        st.session_state.current_page = page5
        st.session_state.on_start_page = False

    if st.sidebar.button("About Me"):
        st.session_state.current_page = page6
        st.session_state.on_start_page = False

    if st.sidebar.button("Back to the Start Page"):
        st.session_state.current_page = start_page
        st.session_state.on_start_page = False

# Show the sidebar only if not on the start page
if not st.session_state.on_start_page:
    show_sidebar()

# Call the function to draw the current page
st.session_state.current_page()


