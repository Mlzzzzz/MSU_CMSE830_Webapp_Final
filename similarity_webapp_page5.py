import streamlit as st
import pandas as pd

def page5():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Model Analysis</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    df_linear = pd.read_csv(r"C:\Users\User\OneDrive - Michigan State University\Data Science\cmse830\Final Project\Webapp\Models\misclassified_linear.csv", index_col=0)
    df_log = pd.read_csv(r"C:\Users\User\OneDrive - Michigan State University\Data Science\cmse830\Final Project\Webapp\Models\misclassified_log.csv", index_col=0)
    df_tree = pd.read_csv(r"C:\Users\User\OneDrive - Michigan State University\Data Science\cmse830\Final Project\Webapp\Models\misclassified_tree.csv", index_col=0)
    df_svr = pd.read_csv(r"C:\Users\User\OneDrive - Michigan State University\Data Science\cmse830\Final Project\Webapp\Models\misclassified_svr.csv", index_col=0)
    df_knn = pd.read_csv(r"C:\Users\User\OneDrive - Michigan State University\Data Science\cmse830\Final Project\Webapp\Models\misclassified_knn.csv", index_col=0)

    models = ["Introduction", "Linear Regression", "Logistic Regression", "Decision Trees", "Support Vector Regression", "K-Nearest Neighbors Regressionegression", "Discussion"]
    model_select = st.selectbox('Select a Relationship to Explore:', models)

    if model_select == "Introduction":
        st.markdown("<p style='font-size: 18px;'>In this section, </p>", unsafe_allow_html=True)

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

    elif model_select == "Decision Trees":
        st.markdown("<p style='font-size: 18px;'><strong>Data Loading:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>tanimoto_cdk_Extended, TanimotoCombo are selected as features,, with similar as the target variable.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Model Selection and Grid Search:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>max_depth from 2-10, min_samples_split from 2-8, min_samples_leaf from 1-5 have been chosen for our grid search. This search utilizes 5-fold cross-validation, "
                    "with accuracy as the scoring metric. "
                    "After grid search, model with max_depth: 4, min_samples_leaf: 3, min_samples_split: 2 is selected for further analysis.</p>", unsafe_allow_html=True)   
        st.markdown("<p style='font-size: 18px;'><strong>Predictions and Evaluation:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>The selected Decision Trees model (max_depth=4, min_samples_leaf=3, min_samples_split=2) was trained using a 5-Fold split of the data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'><strong>Identification of Misclassified Pairs:</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>An essential part of our analysis was identifying pairs where predicted similarity diverged from actual similarity. "
                    "These instances are highlighted in the table below:</p>", unsafe_allow_html=True)
        st.write(df_tree)
        st.markdown("<p style='font-size: 18px;'>Conclusively, the linear regression model achieved a prediction accuracy of <span style='color: blue; font-weight: bold;'>77%</span>.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>It is important to note that during grid search, the best hyperparameter results display considerable sensitivity to various splits of the dataset. "
                    "This observation indicates that the model may struggle to generalize across different subsets of data. "
                    "the decision tree model may not be a suitable choice for this particular problem.</p>", unsafe_allow_html=True)
        
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

    elif model_select == "K-Nearest Neighbors Regressionegression":
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
    
    elif model_select == "Discussion":
        st.markdown("<p style='font-size: 18px;'>Discussion, </p>", unsafe_allow_html=True)


