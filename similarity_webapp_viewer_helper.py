import streamlit as st

def format_number(n):
    if n < 10:
        return "00" + str(n)
    elif n < 100:
        return "0" + str(n)
    else:
        return str(n)

def structure_viewer(n):
    n_str = format_number(n)

    twod_urla = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_{n_str}a.svg"
    twod_urlb = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_{n_str}b.svg"

    col1, col2 = st.columns(2)
    col1.markdown(f"<img src={twod_urla} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown(f"<img src={twod_urlb} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: black; font-size: 18px;'>For 3D structure, please access <a href='https://github.com/Mlzzzzz/MSU_CMSE830_Webapp/tree/main/Picture/3dc_conformer' target='_blank'>My GitHub Repository</a> to download the conformer file and submit it to <a href='https://www.rcsb.org/3d-view' target='_blank'>RCSB 3D-View</a>.</h1>", unsafe_allow_html=True)

def show_annotation(annotation, key):
    state_key = f'show_annotation_{key}'
    
    if state_key not in st.session_state:
        st.session_state[state_key] = False

    if st.button('Annotation', key=key):
        st.session_state[state_key] = not st.session_state[state_key]

    if st.session_state[state_key]:
        st.markdown(f"<h1 style='color: black; font-size: 18px;'>{annotation}</h1>", unsafe_allow_html=True)

def twod_viewer(n):
    n_str = format_number(n)

    twod_urla = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_{n_str}a.svg"
    twod_urlb = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_{n_str}b.svg"

    col1, col2 = st.columns(2)
    col1.markdown(f"<img src={twod_urla} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown(f"<img src={twod_urlb} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
