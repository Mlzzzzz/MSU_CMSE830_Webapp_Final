import streamlit as st
from similarity_webapp_page1 import page1

def start_page():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 36px;'>Welcome to the Molecular Similarity Analysis Web App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>This web app offers an in-depth exploration of the Molecular Similarity Perception dataset.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Within the app, you will visualize the distribution of individual features in the dataset, explore the interconnections between various features," 
                "and compare different models for predicting whether experienced chemists will perceive a pair of molecules as similar.</p>", unsafe_allow_html=True)


    st.markdown("<h2 style='font-size: 24px;'>Why do we care about Molecular Similarity?</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.markdown("""
        <p style='text-align: center; font-size: 14px;'>Statins</p>
        <img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/Lovastatin.svg' width='200' height='100' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>
        <p style='text-align: center; font-size: 16px;'>Familial hypercholesterolemia</p>
    """, unsafe_allow_html=True)

    col2.markdown("""
        <p style='text-align: center; font-size: 14px;'>Cuprimine</p>
        <img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/Penicillamine_structure.svg' width='120' height='100' alt='Cuprimine' style='display: block; margin-left: auto; margin-right: auto;'>
        <p style='text-align: center; font-size: 16px;'>Wilson's disease</p>
    """, unsafe_allow_html=True)

    col3.markdown("""
        <p style='text-align: center; font-size: 14px;'>Nebcin</p>
        <img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/Tobramycin.svg' width='200' height='100' alt='Nebcin' style='display: block; margin-left: auto; margin-right: auto;'>
        <p style='text-align: center; font-size: 16px;'>Cystic fibrosis</p>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size: 18px;'>An  <span style='color: blue; font-weight: bold;'>orphan drug</span> is a pharmaceutical agent that is developed to treat certain rare medical conditions. "
                "An orphan drug would not be profitable to produce without government assistance, due to the small population of patients affected by the conditions. </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>One of the most important government intervention is Exclusivity (enhanced patent protection and marketing rights).</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>When developing a new orphan drug, the first thing to do is to compare it's similarity with other orphan drugs in the Exclusivity period.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_003a.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_003b.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Are they similar?</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_005a.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_005b.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Or, are they similar?</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size: 18px;'>Even experienced chemists often make mistakes!</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Conventionally, specialists make majority votes for government to determine if two molecules are similar.</p>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("""
    <p style='font-size: 18px;'>
    In this web app, you are invited to navigate through a series of sections crafted to help you understand how to predict the simialrity of drug molecule pairs.
    </p>
    <p style='font-size: 18px;'>
    <strong>Introduction to the Dataset:</strong> Engage with the foundational structure of the dataset, which provides an overview of the dataset and a detailed explanation of each attribute.
    </p>
    <p style='font-size: 18px;'>
    <strong>Distribution of Attributes:</strong> Dive deeper into the dataset's attributes to uncover their statistics, distributions, and outliers.
    </p>
    <p style='font-size: 18px;'>
    <strong>Relationships of Attributes:</strong> Investigate correlations between the attributes and uncover how they influence one another.
    </p>
    <p style='font-size: 18px;'>
    <strong>Misclassified Molecular Pairs in the Original Work:</strong>  Examine the pairs of molecules that were misclassified in the original paper. A closer look at their structures and chemical properties could reveal new, noteworthy features for consideration.
    </p>
    <p style='font-size: 18px;'>
    <strong>Model Analysis:</strong> Assess and compare a variety of machine learning models, evaluating their effectiveness in predicting molecular similarity.
    </p>
    <p style='font-size: 18px;'>
    Ready to begin? Click the 'Start Exploration' button below to launch your journey into molecular similarity analysis.
    </p>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    if st.button('Start Exploration'):
        st.session_state.current_page = page1
        st.session_state.on_start_page = False
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 18px;'>The original dataset is collected and built based on: Gandini, E.; Marcou, G.; Bonachera, F.; Varnek, A.; Pieraccini, S.; Sironi, M. "
                "Molecular Similarity Perception Based on Machine-Learning Models. <i>Int. J. Mol. Sci.</i> <b>2022</b>, 23, 6114.</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 18px;'>Developed by Linqing Mo, Michigan State University</p>", unsafe_allow_html=True)