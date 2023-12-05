import streamlit as st
import pandas as pd
from similarity_webapp_viewer_helper import structure_viewer

def input_id():
    id_pair = st.text_input('Enter id_pair:')
    if id_pair:
        try:
            id_pair = int(id_pair)
            if 1 <= id_pair <= 100:
                st.success(f"Valid id_pair: {id_pair}")
                return id_pair
            else:
                st.error("Please enter a valid id_pair (1-100)")
        except ValueError:
            st.error("Please enter a valid id_pair (1-100)")

def page1():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Introduction of the Dataset</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    columns_to_select = [col for col in df.columns if col != 'id_pair']
    columns_to_select.insert(0, 'Dataset Preview')
    attribute = st.selectbox('Select an Attribute to Explore:', columns_to_select)

    def attribute_introduction(attribute):
        st.write("")
        st.write("")
        st.markdown(f"<p style='font-size: 18px;'>Type in an id_pair(1-100) to get an example of {attribute}.</p>", unsafe_allow_html=True)
        id_pair = input_id()
        if id_pair is not None:
            attribute_value = df.loc[df["id_pair"] == id_pair, attribute].values[0]
            if isinstance(attribute_value, float):
                formatted_value = f"{attribute_value:.4f}"
            else:
                formatted_value = attribute_value
            st.markdown(f"<p style='font-size: 18px;'>{attribute} of this selected molecule pair is {formatted_value}</p>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 18px;'>2D pictures of this selected molecule pair:</p>", unsafe_allow_html=True)
            structure_viewer(id_pair)

    if attribute == 'Dataset Preview':
        st.markdown("<p style='font-size: 18px;'>In this section, you will be provided an overview of the dataset and a detailed explanation of each attribute.</p>", unsafe_allow_html=True)
        st.write(df)
        st.markdown("<p style='font-size: 18px;'>This dataset comprises 100 pairs of bioactive molecules, categorized based on both 2D and 3D similarity. There are four distinct pair types: sim2D-sim3D, sim2D-dis3D, dis2D-sim3D, and dis2D-dis3D. Each type contains 25 molecule pairs.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size: 18px;'>Select an attibute to get the details.</p>", unsafe_allow_html=True)

    elif attribute == "tanimoto_cdk_Extended":
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended is an index approximated by the Tanimoto coefficient, calculated with CDK Extended fingerprints. It represents the <span style='color: blue; font-weight: bold;'>2D similarity</span> of molecular pairs.</p>", unsafe_allow_html=True)
        attribute_introduction(attribute)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended is measured based on: Franco, P.; Porta, N.; Holliday, J.D.; Willett, P. The use of 2D fingerprint methods to support the assessment of structural similarity in orphan drug legislation. <i>J. Cheminform</i> <b>2014</b>, 6, 5.</p>", unsafe_allow_html=True)
    
    elif attribute == "TanimotoCombo":
        st.markdown("<p style='font-size: 18px;'>TanimotoCombo is an index assessed as a TanimotoCombo metric, calculated with the ROCS tool of OpenEye, utilized to represent the <span style='color: blue; font-weight: bold;'>3D similarity</span> of molecular pairs.</p>", unsafe_allow_html=True)
        attribute_introduction(attribute)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<p style='font-size: 18px;'>TanimotoCombo is measured based on: ROCS. Santa Fe, NM: OpenEye Scientific Software. Available online: https://www.eyesopen.com/rocs", unsafe_allow_html=True)

    elif attribute == "pchembl_distance":
        st.markdown("<p style='font-size: 18px;'>pChEMBL_distance encompasses the pChEMBL values, used to filter compounds for which an inhibition constant was measured.</p>", unsafe_allow_html=True)
        attribute_introduction(attribute)
    
    elif attribute == "target_name":
        st.markdown("<p style='font-size: 18px;'>target_name identifies the targeted three well-known biological targets: HERG, 5HT2B, and CYP2D6. All molecule pairs in this dataset are targeting one of these three biological targets.</p>", unsafe_allow_html=True)
        attribute_introduction(attribute)

    elif attribute == "pair_type":
        st.markdown("<p style='font-size: 18px;'>pair_type is generated from tanimoto_cdk_Extended and TanimotoCombo. The threshold of tanimoto_cdk_Extended is 0.65. If tanimoto_cdk_Extended is lower than 0.65, this molecule pair will be identified as 2D similar, otherwise it will be identified as 2D dissimilar. 3D similarity of molecule pair is determined by TanimotoCombo, with a threshold of 1.3.</p>", unsafe_allow_html=True)
        attribute_introduction(attribute)
    
    elif attribute == "frac_similar":
        st.markdown('<p style=\'font-size: 18px;\'>frac_similar is collected from web-survey of professional chemists, representing the fraction of the \"similar\" answers.</p>', unsafe_allow_html=True)
        attribute_introduction(attribute)
    
    elif attribute == "similar":
        st.markdown('<p style=\'font-size: 18px;\'>similar is the label of molecule pair similarity generated from frac_similar with a threshold of 0.5. Molecule pair with frac_similar lower than 0.5 will be labeled as 0, otherwise will be labeled as 1.</p>', unsafe_allow_html=True)
        attribute_introduction(attribute)

        