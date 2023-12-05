import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
from similarity_webapp_viewer_helper import show_annotation


def page2():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Distribution of Attributes</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")

    df['similar'] = df['similar'].astype(str)
    attributes_to_select = ['Introduction', 'tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'frac_similar']
    hues_to_select = ['pair_type', 'similar']
    attribute = st.selectbox('Select an Attribute to Explore:', attributes_to_select)
    
    def attribute_statistic(attribute):
        st.markdown(f"<h1 style='color: black; font-size: 18px;'>Statistics of {attribute}</h1>", unsafe_allow_html=True)
        stats_df = df[attribute].describe().reset_index()
        stats_df.columns = ['Statistic', 'Value']
        st.table(stats_df)


    def attribute_boxplot(attribute, hue):
        chart_without_hue = alt.Chart(df).mark_boxplot().encode(
            y=attribute
        ).properties(
            title=f'Boxplot of {attribute}'
        )
        
        chart_with_hue = alt.Chart(df).mark_boxplot().encode(
            x=hue,
            y=attribute
        ).properties(
            title=f'Boxplot of {attribute} Grouped by {hue}'
        )
        
        combined_chart = alt.hconcat(chart_without_hue, chart_with_hue)
        st.altair_chart(combined_chart, use_container_width=True)
    

    def attribute_histogram(attribute, hue):
        unique_hues = df[hue].nunique()
        soft_colors = sns.color_palette("pastel", unique_hues).as_hex()
        
        attr_min = df[attribute].min()
        attr_max = df[attribute].max()

        base = alt.Chart(df).transform_bin(
            'binned_attr', attribute, bin=alt.Bin(maxbins=20, extent=[attr_min, attr_max])
        ).transform_aggregate(
            count='count()',
            groupby=['binned_attr', hue]
        ).transform_calculate(
            bin_range="round(datum.binned_attr * 100) / 100 + '-' + round((datum.binned_attr + 1/20) * 100) / 100"
        )

        bars = base.mark_bar().encode(
            x=alt.X('bin_range:N', axis=alt.Axis(title=attribute)),
            y='count:Q',
            color=alt.Color(hue, scale=alt.Scale(range=soft_colors)),  
            order=alt.Order(
                hue,
                sort='ascending'
            )
        ).properties(
            title={
                "text": f"Histogram of {attribute} Grouped by {hue}"
            }
        )

        st.altair_chart(bars, use_container_width=True)


    if attribute == "Introduction":
        st.markdown("<p style='font-size: 18px;'>In this section, you will dive deeper into the distribution of attributes in this dataset to uncover their potentail usage to predict molecule similaritys. "
                    'For each visualization presented here, hover your cursor over the plot to view detailed information, and click on the "Annotation" button to access an interpretation of the findings.</p>', unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended represents the 2D similarity of molecule pairs. We involved statistical information, the boxplot and histogram based on different hues in this section. "
                    " The focus is on understanding the 2D similarity scores of molecule pairs, examining how these scores vary across different pair types, and potential areas for further investigation.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>TanimotoCombo represents the 3D similarity of molecule pairs. We involved statistical information and the histogram based on different hues in this section. "
                    "  The primary focus here is on areas exhibiting discrepancies between the assessed 3D similarity of molecule pairs and the evaluations made by chemists.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For pchembl_distance,  we includes the creation of boxplots and histograms that are categorized according to selected hues. "
                    "Although this attribute was not initially factored into the original paper's model, our analysis reveals its significant role. "
                    "We observe that molecule pairs with a 'pchembl_distance' greater than 1.5 often correlate with classifications of dissimilarity by chemists, highlighting the attribute's potential importance in assessing molecular similarity.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>We also explored the histogram of frac_similar cayegorized by pair_type,  focusing on how chemists agree on molecular pairs that are consistently similar or dissimilar in both 2D and 3D structures. "
                    "Additionally, we identify specific areas where there is a notable reduction in consensus among chemists in their molecular assessments.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Select an attribute to get started.</p>", unsafe_allow_html=True)

    elif attribute == "tanimoto_cdk_Extended":
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended defines the 2D similarity part in the attribute: pair_type. "
                    "If tanimoto_cdk_Extended is lower than 0.65, this molecule pair will be identified as 2D similar, otherwise it will be identified as 2D dissimilar.</p>", unsafe_allow_html=True)
        attribute_statistic(attribute)
        tanimoto_cdk_Extended_annotation1 = ("There is no missing value in this attribute. Both mean and median of tanimoto_cdk_Extended are close to the threshold: 0.65. "
        "The value of standard deviation: 0.2593 is relatively high, indicating that the 2D similarity scores vary widely across the molecule pairs.")
        show_annotation(tanimoto_cdk_Extended_annotation1,1)

        hue = st.selectbox('Select a Hue:', hues_to_select, key='tanimoto_cdk_Extended')
        if hue:
            attribute_boxplot(attribute, hue)
            tanimoto_cdk_Extended_annotation2 = ("When grouping by pair_type, the boxplot shows that there are distinct distributions for each pair type. Generally  molecule pairs that are dis-similar in 2D also tend to dis-similar in 3D."
            "When grouping by similar, the boxplot suggests that pairs considered similar have a higher median Tanimoto coefficient, which is expected since a higher Tanimoto score generally indicates greater 2D similarity.")
            show_annotation(tanimoto_cdk_Extended_annotation2,2)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)
            tanimoto_cdk_Extended_annotation3 = (
                'For the histogram, it will be more interesting to group the data by "similar". The area between 0.45-0.85 '
                'demonstrate a disparity between 2D similarity and chemist assessments. '
                'Investigating these molecule pair cases could provide valuable information on which characteristics contribute to the mismatch in similarity judgments.'
            )
            show_annotation(tanimoto_cdk_Extended_annotation3, 3)

    
    elif attribute == "TanimotoCombo":
        st.markdown("<p style='font-size: 18px;'>TanimotoCombo defines the 3D similarity part in the attribute: pair_type. "
                    "If TanimotoCombo is lower than 1.3, this molecule pair will be identified as 3D similar, otherwise it will be identified as 3D dissimilar.</p>", unsafe_allow_html=True)
        attribute_statistic(attribute)
        TanimotoCombo_annotation1 = ("There is no missing value in this attribute. Similar to tanimoto_cdk_Extended, both mean and median of TanimotoCombo are close to the threshold: 1.3. "
        "The value of standard deviation: 0.4397 is relatively high, indicating that the 3D similarity scores vary widely across the molecule pairs.")
        show_annotation(TanimotoCombo_annotation1,4)
        hue = st.selectbox('Select a Hue:', hues_to_select, key='TanimotoCombo')
        if hue:
            attribute_histogram(attribute, hue)
            TanimotoCombo_annotation2 = (
                "The TanimotoCombo appears to be less effective than tanimoto_cdk_Extended at discerning the similarity among molecular pairs. "
                "This observation aligns with the typical practices of chemists who often rely on 2D structural visualizations to assess molecular similarity. "
                "Notably, molecular pairs with a TanimotoCombo score ranging from 1 to 1.75 demonstrate a disparity between 3D similarity and chemist assessments. "
                "Focusing on these particular pairs could yield insights into the features that are leading to discrepancies in similarity evaluations."
            )
            show_annotation(TanimotoCombo_annotation2, 5)

    elif attribute == "pchembl_distance":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='pchembl_distance')
        if hue:
            attribute_boxplot(attribute, hue)
            attribute_histogram(attribute, hue)
            pchembl_distance_annotation1 = (
                "The authors of the original study did not include pchembl_distance in their model. However, a closer look at the distribution reveals that "
                "the vast majority of molecule pairs with a significant pchembl_distance fall under the dis2D, dis3D pair type. Moreover, any molecule pair with a "
                "pchembl_distance greater than 1.5 is consistently classified as dissimilar by chemists. This pattern suggests that pchembl_distance could be a valuable "
                "predictor in model development for assessing molecular similarity."
            )
            show_annotation(pchembl_distance_annotation1,6)

    elif attribute == "frac_similar":
        attribute_histogram(attribute, hue="pair_type")
        frac_similar_annotation1 = (
            "The frac_similar distribution, categorized by pair_type, reveals a strong consensus among chemists on pairs that are either consistently similar or dissimilar across both 2D and 3D structures. "
            "In the intermediate frac_similar range of 0.25 to 0.85, the agreement diminishes, highlighting a grey zone in the assessment of molecular similarity. Within this range, "
            "it's apparent that chemists tend to concur more on 2D similarities. This suggests that 2D structural features might play a more decisive role in their evaluations of molecular similarity."
        )
        show_annotation(frac_similar_annotation1,7)
