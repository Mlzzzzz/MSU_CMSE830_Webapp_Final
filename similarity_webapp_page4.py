import streamlit as st
import pandas as pd
from similarity_webapp_viewer_helper import twod_viewer

def page4():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Analysis of Misclassified Data</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/misclassified_dataset.csv")
    df = df.rename(columns={"pred_frac_simi": "pred_frac_similar"})
    st.markdown("<h1 style='color: black; font-size: 18px;'>In the original work, a Logistic Regression (LogReg) model was built to predict the similarity of molecule pair following the equation below:</h1>", unsafe_allow_html=True)
    st.markdown(r"""
                $$
                \hat{p} = \frac{e^{w_0 + w_1 t_{xt} + w_2 t_{cs}}}{1 + e^{w_0 + w_1 t_{xt} + w_2 t_{cs}}}
                $$
                """, unsafe_allow_html=True)
    st.markdown(r"""
                $$
                w_0 = -5.605, w_1 = 5.214, w_2 = 2.009
                $$
                """, unsafe_allow_html=True)
    st.markdown("<h1 style='color: black; font-size: 18px;'>The LogReg model(Tanimoto CDK Extended, t<sub>xt</sub>)(TanimotoCombo, t<sub>cs</sub>) was built using scikit-learn using L1 regularization with the default value for the regularization parameter (𝜆=1).</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: black; font-size: 18px;'>Applying this model to the dataset and find the misclassified data(molecule pair with pred_frac_similar lower than 0.5 will be labeled as 0 in pred_similar, otherwise will be labeled as 1.):</h1>", unsafe_allow_html=True)
    
    df["pred_difference"] = abs(df["frac_similar"] - df["pred_frac_similar"])
    df.set_index('id_pair', inplace=True)
    st.write(df)

    jsonstr = df.to_json(orient='records')
    HTML_TEMPLATE = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>
        <link rel="import" href="https://raw.githubusercontent.com/PAIR-code/facets/master/facets-dist/facets-jupyter.html">
        <facets-dive id="elem" width="1000" height="650"></facets-dive>
        <script>
            var data = {jsonstr};
            document.querySelector("#elem").data = data;
        </script>
    """.format(jsonstr=jsonstr)
    
    st.components.v1.html(HTML_TEMPLATE, width=1000, height=650)

    st.markdown("<p style='font-size: 18px;'>The majority of misclassified molecule pairs exhibit a frac_similar value around 0.5, "
                "indicating that there is a considerable degree of disagreement among chemists regarding the similarity of these pairs.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>However, a small number of misclassified pairs have a frac_similar that is notably high or low. We will concentrate on these outliers to determine the underlying reasons for their misclassification.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Molecule pairs with IDs 32 and 50 exhibit high predicted similarity based on their 2D similarity scores, yet they have low actual agreement among chemists, as reflected in their frac_similar values.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>2D structure of pair 32: </p>", unsafe_allow_html=True)
    twod_viewer(32)
    st.markdown("<p style='font-size: 18px;'>2D structure of pair 50: </p>", unsafe_allow_html=True)
    twod_viewer(50)
    st.markdown("<p style='font-size: 18px;'>Both structures feature a sizable similar aromatic chain as their skeleton and a distinctive functional group. "
                "The prominent skeleton could account for the high 2D similarity scores. However, from a chemist's perspective, "
                "the functional group carries more weight in drug development.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Molecule pairs with IDs 3 and 6 demonstrate high predicted similarity based on their 3D similarity scores, yet they show low agreement among chemists. "
                "Both pairs are characterized by complex spatial structures and distinctive functional groups, which might contribute to the discrepancy in perceived similarity.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>In the following section, we will delve into various models to further investigate these misclassified pairs.</p>", unsafe_allow_html=True)


    





    

    




