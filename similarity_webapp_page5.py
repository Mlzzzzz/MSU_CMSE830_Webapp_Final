import streamlit as st
import pandas as pd
from similarity_webapp_viewer_helper import threed_model_visualization, twod_viewer
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import plotly.graph_objects as go

def page5():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Model Analysis</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/preprocessing/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    df_linear = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/Models/misclassified_linear.csv", index_col=0)
    df_log = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/Models/misclassified_log.csv", index_col=0)
    df_tree = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/Models/misclassified_tree.csv", index_col=0)
    df_svr = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/Models/misclassified_svr.csv", index_col=0)
    df_knn = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/Models/misclassified_knn.csv", index_col=0)

    models = ["Introduction", "Linear Regression", "Logistic Regression", "Decision Tree Classifier", "Support Vector Regression", "K-Nearest Neighbors Regression", "Discussion"]
    model_select = st.selectbox('Select a Relationship to Explore:', models)

    if model_select == "Introduction":
        st.markdown("<p style='font-size: 18px;'>In this section, fiva models are implemented to the dataset. Linear Regression, Support Vector Regression (SVR), and K-Nearest Neighbors (KNN) Regression target the 'frac_similar' feature, "
                    "while Logistic Regression and Decision Tree Classifier predict the categorical 'similar' attribute.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For each model, a grid search optimizes the hyperparameters to ensure peak performance. Each model is trained on a 5-Fold cross-validation split "
                    "of the dataset to enhance the generalizability of the models. For regression model, a threshold of 0.5 was applied to the predictions to segregate them into binary outcomes.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Model effectiveness is quantified through classification accuracy. Additionally, an interactive 3D visualization for each model is given, "
                    "offering an insight into their predictive behaviors.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Select a model to get started.</p>", unsafe_allow_html=True)

    elif model_select == "Linear Regression":
        st.markdown("<p style='font-size: 18px;'><strong>Data Loading:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended, TanimotoCombo are selected as features,, with frac_similar as the target variable.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Model Selection and Grid Search:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Ridge, Lasso, and a simple linear regression have been chosen for our grid search. This search utilizes 5-fold cross-validation, "
                    "with negative mean squared error (MSE) as the scoring metric. "
                    "After grid search, the simple linear regression model is selected for further analysis.</p>", unsafe_allow_html=True)   
        st.markdown("<p style='font-size: 18px;'><strong>Predictions and Evaluation:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The selected simple linear regression model was trained using a 5-Fold split of the data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For classification purposes, a threshold of 0.5 was applied to the predictions, segregating them into binary outcomes.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Identification of Misclassified Pairs:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>An essential part of our analysis was identifying pairs where predicted similarity diverged from actual similarity. "
                    "These instances are highlighted in the table below:</p>", unsafe_allow_html=True)
        st.write(df_linear)
        st.markdown("<p style='font-size: 18px;'>Conclusively, the linear regression model achieved a prediction accuracy of <span style='color: blue; font-weight: bold;'>81%</span>.</p>", unsafe_allow_html=True)
        model_toplot = LinearRegression()
        features = ["tanimoto_cdk_Extended", "TanimotoCombo"]
        target = "frac_similar"
        threed_model_visualization(model_toplot, features, target)

    
    elif model_select == "Logistic Regression":
        st.markdown("<p style='font-size: 18px;'><strong>Data Loading:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended, TanimotoCombo are selected as features,, with similar as the target variable. "
                    " To ensure uniformity and improve model performance, we have employed the StandardScaler for standardizing these features.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Model Selection and Grid Search:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>l1 and l2 penalty with different regularization strength C have been chosen for our grid search. This search utilizes 5-fold cross-validation, "
                    "with accuracy as the scoring metric. "
                    "After grid search, l2 penalty with C=0.01 is selected for further analysis.</p>", unsafe_allow_html=True)   
        st.markdown("<p style='font-size: 18px;'><strong>Predictions and Evaluation:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The selected logistic regression model (C=0.01, penalty='l2') was trained using a 5-Fold split of the data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Identification of Misclassified Pairs:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>An essential part of our analysis was identifying pairs where predicted similarity diverged from actual similarity. "
                    "These instances are highlighted in the table below:</p>", unsafe_allow_html=True)
        st.write(df_log)
        st.markdown("<p style='font-size: 18px;'>Conclusively, the linear regression model achieved a prediction accuracy of <span style='color: blue; font-weight: bold;'>85%</span>.</p>", unsafe_allow_html=True)
        model_toplot = LogisticRegression(C=0.01, penalty='l2', solver='saga')
        features = ["tanimoto_cdk_Extended", "TanimotoCombo"]
        target = "similar"
        threed_model_visualization(model_toplot, features, target)

    elif model_select == "Decision Tree Classifier":
        st.markdown("<p style='font-size: 18px;'><strong>Data Loading:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended, TanimotoCombo are selected as features,, with similar as the target variable.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Model Selection and Grid Search:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>max_depth from 2-10, min_samples_split from 2-8, min_samples_leaf from 1-5 have been chosen for our grid search. This search utilizes 5-fold cross-validation, "
                    "with accuracy as the scoring metric. "
                    "After grid search, model with max_depth: 4, min_samples_leaf: 3, min_samples_split: 2 is selected for further analysis.</p>", unsafe_allow_html=True)   
        st.markdown("<p style='font-size: 18px;'><strong>Predictions and Evaluation:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The selected Decision Trees Classifier (max_depth=4, min_samples_leaf=3, min_samples_split=2) was trained using a 5-Fold split of the data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Identification of Misclassified Pairs:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>An essential part of our analysis was identifying pairs where predicted similarity diverged from actual similarity. "
                    "These instances are highlighted in the table below:</p>", unsafe_allow_html=True)
        st.write(df_tree)
        st.markdown("<p style='font-size: 18px;'>Conclusively, the linear regression model achieved a prediction accuracy of <span style='color: blue; font-weight: bold;'>78%</span>.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>It is important to note that during grid search, the best hyperparameter results display considerable sensitivity to various splits of the dataset. "
                    "This observation indicates that the model may struggle to generalize across different subsets of data. "
                    "the decision tree model may not be a suitable choice for this particular problem.</p>", unsafe_allow_html=True)
        model_toplot = DecisionTreeClassifier(max_depth=4, min_samples_leaf=3, min_samples_split=2)
        features = ["tanimoto_cdk_Extended", "TanimotoCombo"]
        target = "similar"
        threed_model_visualization(model_toplot, features, target)
        
    elif model_select == "Support Vector Regression":
        st.markdown("<p style='font-size: 18px;'><strong>Data Loading:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended, TanimotoCombo are selected as features,, with frac_similar as the target variable.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Model Selection and Grid Search:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>kernel: ['rbf', 'linear', 'poly'] , epsilon: [0.1, 0.01, 0.001], C: [0.1, 1, 10, 100] have been chosen for our grid search. This search utilizes 5-fold cross-validation, "
                    "with negative mean squared error (MSE) as the scoring metric. "
                    "After grid search, model with rbf kernel, epsilon=0.01, C=1 is selected for further analysis.</p>", unsafe_allow_html=True)   
        st.markdown("<p style='font-size: 18px;'><strong>Predictions and Evaluation:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The selected Decision Trees model (kernel=rbf, epsilon=0.01, C=1) was trained using a 5-Fold split of the data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For classification purposes, a threshold of 0.5 was applied to the predictions, segregating them into binary outcomes.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Identification of Misclassified Pairs:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>An essential part of our analysis was identifying pairs where predicted similarity diverged from actual similarity. "
                    "These instances are highlighted in the table below:</p>", unsafe_allow_html=True)
        st.write(df_svr)
        st.markdown("<p style='font-size: 18px;'>Conclusively, the epsilon-support vector regression model achieved a prediction accuracy of <span style='color: blue; font-weight: bold;'>84%</span>.</p>", unsafe_allow_html=True)
        model_toplot = SVR(C=1, epsilon=0.005, kernel='rbf')
        features = ["tanimoto_cdk_Extended", "TanimotoCombo"]
        target = "frac_similar"
        threed_model_visualization(model_toplot, features, target)

    elif model_select == "K-Nearest Neighbors Regression":
        st.markdown("<p style='font-size: 18px;'><strong>Data Loading:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended, TanimotoCombo are selected as features,, with frac_similar as the target variable.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Model Selection and Grid Search:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>n_neighbors from 1-11 and metric: euclidean or manhattan have been chosen for our grid search. This search utilizes 5-fold cross-validation, "
                    "with negative mean squared error (MSE) as the scoring metric. "
                    "After grid search, model with metric=manhattan and n_neighbors=4 is selected for further analysis.</p>", unsafe_allow_html=True)   
        st.markdown("<p style='font-size: 18px;'><strong>Predictions and Evaluation:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The selected k-nearest neighbors regressionegression model (n=4, metric=\"manhattan\") was trained using a 5-Fold split of the data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For classification purposes, a threshold of 0.5 was applied to the predictions, segregating them into binary outcomes.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Identification of Misclassified Pairs:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>An essential part of our analysis was identifying pairs where predicted similarity diverged from actual similarity. "
                    "These instances are highlighted in the table below:</p>", unsafe_allow_html=True)
        st.write(df_knn)
        st.markdown("<p style='font-size: 18px;'>Conclusively, the k-nearest neighbors regression model achieved a prediction accuracy of <span style='color: blue; font-weight: bold;'>87%</span>.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>As of now, this model stands out as the most effective one that have been evaluated.</p>", unsafe_allow_html=True)
        model_toplot = KNeighborsRegressor(metric='manhattan', n_neighbors=4)
        features = ["tanimoto_cdk_Extended", "TanimotoCombo"]
        target = "frac_similar"
        threed_model_visualization(model_toplot, features, target)

    elif model_select == "Discussion":
        st.markdown("<p style='font-size: 18px;'>Among these five models, the KNN Regression stands out with the highest accuracy of 0.87. The turned Logistic Regression "
                    "model achieves an accuracy of 0.85, closely matching the performance reported in the original paper (0.85). Contrary to expectations, "
                    "the Decision Tree Classifier gives the least accuracy of 0.78.</p>", unsafe_allow_html=True)      
        st.markdown("<p style='font-size: 18px;'>The 3D plot of each model provides deep insights into the patterns within the dataset, "
                    "particularly around the decision boundary of the linear regression model.</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 18px;'> With a classification threshold set at 0.5, molecule pairs that exhibit either uniformly high or low similarities "
                    "in both 2D and 3D will be easily classified accurately. So, Our primary interest in the model lies in the \"grey area\" surrounding the 0.5 threshold. This aspect is consistent with our analyses in previous sections.</p>", unsafe_allow_html=True)      
        st.markdown("<p style='font-size: 18px;'>It's interesting to note that around the threshold, most molecule pairs tend to cluster together. For example:</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Molecule Pair 26 (tanimoto_cdk_Extended=0.878, TanimotoCombo=1.191, frac_similar=0.750):</p>", unsafe_allow_html=True)
        twod_viewer(26)
        st.markdown("<p style='font-size: 18px;'>And Molecule Pair 31 (tanimoto_cdk_Extended=0.826, TanimotoCombo=1.127, frac_similar=0.762):</p>", unsafe_allow_html=True)
        twod_viewer(31)
        st.markdown("<p style='font-size: 18px;'>It's evident that these two molecule pairs share similar functional groups, which, in my opinion, are crucial predictors used by chemists to determine the similarity of molecule pairs. "
                    "This similarity in functional groups might also explain why the KNN model exhibits the best performance.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'Upon examining the misclassified molecule pairs by the KNN model, it's surprising to find that out of the 13 pairs, 6 are misclassified due to "
                    "difference of the Peptide bond orientation. For example:</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Molecule Pair 32 (tanimoto_cdk_Extended=0.802, TanimotoCombo=1.275, frac_similar=0.381):</p>", unsafe_allow_html=True)
        twod_viewer(32)
        st.markdown("<p style='font-size: 18px;'>Despite this molecule pair exhibiting high 2D and 3D similarities, chemists have assigned it a low frac_similarity score of 0.381, "
                    "primarily due to the altered orientation of the Peptide bond.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Molecule pairs 29, 30, 43, 45, and 48 are misclassified similarly to molecule pair 32 for the same reason</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>For the remaining seven misclassified molecule pairs, two are misclassified due to their structural similarities overshadowing the differences between benzene and pyridine rings. "
                    "Another two are misclassified because of overlooked changes in the functional groups on the benzene ring, "
                    "while the final two are due to an overlook in the rearrangement of their structures.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Due to the limited size of the dataset, a more comprehensive analysis of general patterns in misclassified molecule pairs has not been undertaken. "
                    "However, identifying such patterns and applying appropriate preprocessing to the molecular pair data could pave "
                    "the way for a more objective and robust system for determining the similarity of molecule pairs.</p>", unsafe_allow_html=True)

