import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
from similarity_webapp_viewer_helper import show_annotation

def page3():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Relationship of Attributes</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    hues_to_select = ['pair_type', 'similar']
    relationships = ["Introduction", "Relationship between tanimoto_cdk_Extended and TanimotoCombo", "Relationship between tanimoto_cdk_Extended and pchembl_distance", "Relationship between tanimoto_cdk_Extended and frac_similar", 
                     "Relationship between TanimotoCombo and pchembl_distance", "Relationship between TanimotoCombo and frac_similar", "Relationship between pchembl_distance and frac_similar"]
    relationship_select = st.selectbox('Select a Relationship to Explore:', relationships)

    def attribute_relationship(attribute1, attribute2, hue):
        # Initialize the session state variable for switch_axes if it doesn't exist
        if 'switch_axes' not in st.session_state:
            st.session_state['switch_axes'] = False

        # Button to switch axes
        if st.button('Switch X and Y Axes'):
            st.session_state['switch_axes'] = not st.session_state['switch_axes']

        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>You can drag to select the area you want to specify on the graph.</h1>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        brush = alt.selection_interval()
        base = alt.Chart(df).add_params(brush)

        unique_hues = df[hue].nunique()
        soft_colors = sns.color_palette("muted", unique_hues).as_hex()

        # Use the session state variable for switch_axes
        x_attr = attribute1 if not st.session_state['switch_axes'] else attribute2
        y_attr = attribute2 if not st.session_state['switch_axes'] else attribute1

        points = base.mark_circle().encode(
            x=alt.X(x_attr, axis=alt.Axis(title='')),
            y=alt.Y(y_attr, axis=alt.Axis(title='')),
            color=alt.condition(brush, alt.Color(f"{hue}:N", scale=alt.Scale(range=soft_colors)), alt.value('grey'))
        ).properties(
            title={
                "text": f"Scatter Plot of {x_attr} and {y_attr} Grouped by {hue}"
            }
        )

        tick_axis = alt.Axis(labels=False, domain=False, ticks=False)
        x_ticks = base.mark_tick().encode(
            alt.X(x_attr, axis=tick_axis),
            alt.Y(hue, title='', axis=tick_axis),
            color=alt.condition(brush, alt.Color(f"{hue}:N", scale=alt.Scale(range=soft_colors)), alt.value('lightgrey'))
        )
        y_ticks = base.mark_tick().encode(
            alt.X(hue, title='', axis=tick_axis),
            alt.Y(y_attr, axis=tick_axis),
            color=alt.condition(brush, alt.Color(f"{hue}:N", scale=alt.Scale(range=soft_colors)), alt.value('lightgrey'))
        )

        final_chart = y_ticks | (points & x_ticks)
        st.altair_chart(final_chart, use_container_width=True)


    if relationship_select == "Introduction":
        st.markdown("<p style='font-size: 18px;'>In this section, you will explore relationships between tanimoto_cdk_Extended, TanimotoCombo, pchembl_distance and frac_similar.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For each visualization presented here, hover your cursor over the plot to view detailed information, "
                    "click on the 'Switch X and Y Axes' to change the axes of the plot, and click on the 'Annotation' button to access an interpretation of the findings.</p>", unsafe_allow_html=True)

        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Heatmap of Attributes</h1>", unsafe_allow_html=True)
        numeric_attributes = df[['tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'frac_similar']].select_dtypes(include=['float64', 'int64'])
        corr = numeric_attributes.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        fig = sns.mpl.pyplot.gcf()
        st.pyplot(fig)
        st.markdown("<p style='font-size: 18px;'>There is a strong positive correlation exists between tanimoto_cdk_Extended, TanimotoCombo, and frac_similar, with coefficients of 0.83 and 0.8, respectively. "
                    "This relationship suggests that as 2D and 3D similarity scores increase, so does the consensus among chemists.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Conversely, pchembl_distance has a moderate negative correlation with frac_similar, "
                    "reinforcing the distribution analysis findings that molecule pairs with a pchembl_distance greater than 1.5 are uniformly classified as dissimilar by chemists.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The heatmap suggests that tanimoto_cdk_Extended and TanimotoCombo will be good indicators for determining molecular similarity. "
                    "Additionally, pchembl_distance emerges as a potential predictor in certain models.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Choose a relationship to examine in detail.</p>", unsafe_allow_html=True)

    
    elif relationship_select == "Relationship between tanimoto_cdk_Extended and TanimotoCombo":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='relationship1')
        attribute_relationship("tanimoto_cdk_Extended", "TanimotoCombo", hue)
        annotation1 = ("The scatter plot, organized by 'pair_type' and 'similar', distinctly illustrates that pairs labeled as sim2D, sim3D are consistently identified as similar, while dis2D, dis3D pairs are recognized as dissimilar. "
                       "Within the grey area that encompasses sim2D, dis3D and dis2D, sim3D pairs, a greater number of sim2D, dis3D pairs are classified as similar. "
                       "Additionally, it's noteworthy that a positive correlation exists between tanimoto_cdk_Extended and TanimotoCombo.")
        show_annotation(annotation1,1)
    
    elif relationship_select == "Relationship between tanimoto_cdk_Extended and pchembl_distance":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='relationship2')
        attribute_relationship("tanimoto_cdk_Extended", "pchembl_distance", hue)
        annotation2 = ("The scatter plot reveals a distinct absence of high pchembl_distance values coinciding with high tanimoto_cdk_Extended scores. "
                       "Additionally, within the range of low pchembl_distance values, the relationship between the two attributes does not exhibit a clear pattern.")
        show_annotation(annotation2,2)
    
    elif relationship_select == "Relationship between tanimoto_cdk_Extended and frac_similar":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='relationship3')
        attribute_relationship("tanimoto_cdk_Extended", "frac_similar", hue)
        annotation3 = ("The plot shows a positive trend, suggesting that generally, as tanimoto_cdk_Extended increases, frac_similar will also increase."
                       " The sim2D,dis3D and'dis2D,sim3D pairs are spread across the plot, highlighting the complexity of similarity assessments when 2D and 3D analyses are in conflict.")
        show_annotation(annotation3,3)
    
    elif relationship_select == "Relationship between TanimotoCombo and pchembl_distance":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='relationship4')
        attribute_relationship("TanimotoCombo", "pchembl_distance", hue)
        annotation4 = ("The scatter plot demonstrates that, unlike tanimoto_cdk_Extended, high TanimotoCombo scores are present even in regions of high pchembl_distance values. No clear trend between these two attributes is evident.")
        show_annotation(annotation4,4)

    elif relationship_select == "Relationship between TanimotoCombo and frac_similar":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='relationship5')
        attribute_relationship("TanimotoCombo", "frac_similar", hue)
        annotation5 = ("The plot indicates a positive correlation, generally suggesting that as TanimotoCombo increases, frac_similar tends to rise as well. "
                       "However, when specifically examining the 'dis2D, sim3D' pairs, their distribution appears to be random.")
        show_annotation(annotation5,5)
    
    elif relationship_select == "Relationship between pchembl_distance and frac_similar":
        hue = st.selectbox('Select a Hue:', hues_to_select, key='relationship6')
        attribute_relationship("pchembl_distance", "frac_similar", hue)
        annotation6 = ("As previously mentioned, a distinct pattern emerges where pairs with a pchembl_distance value greater than 1.5 will be classified as dissimilar, "
                       "suggesting the potential of this attribute as a predictive factor in certain models.")
        show_annotation(annotation6,6)