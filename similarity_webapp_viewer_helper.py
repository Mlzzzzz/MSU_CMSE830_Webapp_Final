import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import plotly.graph_objects as go

def format_number(n):
    if n < 10:
        return "00" + str(n)
    elif n < 100:
        return "0" + str(n)
    else:
        return str(n)

def structure_viewer(n):
    n_str = format_number(n)

    twod_urla = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_{n_str}a.svg"
    twod_urlb = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_{n_str}b.svg"

    col1, col2 = st.columns(2)
    col1.markdown(f"<img src={twod_urla} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown(f"<img src={twod_urlb} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: black; font-size: 18px;'>For 3D structure, please access <a href='https://github.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/tree/main/pictures/3d_conformers' target='_blank'>My GitHub Repository</a> to download the conformer file and submit it to <a href='https://www.rcsb.org/3d-view' target='_blank'>RCSB 3D-View</a>.</h1>", unsafe_allow_html=True)

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

    twod_urla = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_{n_str}a.svg"
    twod_urlb = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/pictures/2d_structures/image_molecule_{n_str}b.svg"

    col1, col2 = st.columns(2)
    col1.markdown(f"<img src={twod_urla} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown(f"<img src={twod_urlb} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)


def threed_model_visualization(model_toplot, features_name, target_name):
    st.markdown(f"<p style='font-size: 18px;'>This 3D visualization of the <strong>{model_toplot.__class__.__name__}</strong> model training on the whole dataset is shown below. Points in blue represent the original data, while points in red represent the model's predictions. "
                "The red plane illustrates the model's decision boundary, and the green plane illustrates the classification threshold. The short purple lines highlight the pairs of molecules that have been misclassified.</p>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp_Final/main/preprocessing/preprocessed_dataset.csv")
    features = df[features_name]
    targets = df[target_name]
    
    if isinstance(model_toplot, LogisticRegression):
        scaler = StandardScaler()
        features = scaler.fit_transform(features)
        features = pd.DataFrame(features, columns=features_name)
    else:
        features = pd.DataFrame(features, columns=features_name)
    
    model = model_toplot
    model.fit(features, targets)
    
    # Predictions for each point
    df['predicted'] = model.predict(features)

    # Prepare meshgrid for regression surface
    x_range = np.linspace(features[features_name[0]].min(), features[features_name[0]].max(), 100)
    y_range = np.linspace(features[features_name[1]].min(), features[features_name[1]].max(), 100)
    xx, yy = np.meshgrid(x_range, y_range)
    mesh_features = pd.DataFrame(np.c_[xx.ravel(), yy.ravel()], columns=features_name)
    zz = model.predict(mesh_features).reshape(xx.shape)
    
    fig = go.Figure()

    # Add scatter plot of original points
    fig.add_trace(go.Scatter3d(
        x=features[features_name[0]],
        y=features[features_name[1]],
        z=df[target_name],
        mode='markers',
        marker=dict(size=3, color='blue'),
        name='Original Data'
    ))

    # Add scatter plot of predicted points
    fig.add_trace(go.Scatter3d(
        x=features[features_name[0]],
        y=features[features_name[1]],
        z=df['predicted'],
        mode='markers',
        marker=dict(size=3, color='red'),
        name="Model's Predictions"
    ))

    # Add a plane at z=0.5
    x_plane = np.linspace(features[features_name[0]].min(), features[features_name[0]].max(), 10)
    y_plane = np.linspace(features[features_name[1]].min(), features[features_name[1]].max(), 10)
    xx_plane, yy_plane = np.meshgrid(x_plane, y_plane)
    zz_plane = np.full(xx_plane.shape, 0.5)

    fig.add_trace(go.Surface(
        x=xx_plane,
        y=yy_plane,
        z=zz_plane,
        name='Classification Threshold',
        showscale=False,
        opacity=0.2,
        colorscale=[[0, 'green'], [1, 'green']],
    ))

    # Add a verticle line between original value and predicted value
    for i in df.index:
        original_z = df.at[i, target_name]
        predicted_z = df.at[i, 'predicted']
        x_val = features.at[i, features_name[0]]
        y_val = features.at[i, features_name[1]]

        # Check if the line crosses z=0.5 plane. If so, highlight this line.
        crosses_plane = (original_z < 0.5 and predicted_z >= 0.5) or (original_z >= 0.5 and predicted_z < 0.5)
        line_color = 'magenta' if crosses_plane else 'gray'  
        line_width = 4 if crosses_plane else 2  
        line_opacity = 1.0 if crosses_plane else 0.3  

        fig.add_trace(go.Scatter3d(
            x=[x_val, x_val],
            y=[y_val, y_val],
            z=[original_z, predicted_z],
            mode='lines',
            line=dict(color=line_color, width=line_width),
            opacity=line_opacity,
            showlegend=False
        ))  

    # Add the plane defined by the model
    fig.add_trace(go.Surface(
        x=xx, y=yy, z=zz,
        name="Model's Decision Boundary",
        opacity=0.2,
        colorscale=[[0, 'red'], [1, 'red']],
        showscale=False,
    ))

    fig.update_layout(
        title=f"3D Visualization for {type(model_toplot).__name__} Model",
        scene=dict(
            xaxis_title=features_name[0],
            yaxis_title=features_name[1],
            zaxis_title=target_name
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    st.plotly_chart(fig)
