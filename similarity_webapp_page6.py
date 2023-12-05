import streamlit as st
import base64

def page6():

    def get_base64_of_image(file_path):
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    data_chemist_path = "C:\\Users\\User\\OneDrive - Michigan State University\\Data Science\\cmse830\\Final Project\\Webapp\\pictures\\data-chem.png"
    mo_pic_path = "C:\\Users\\User\\OneDrive - Michigan State University\\Data Science\\cmse830\\Final Project\\Webapp\\pictures\\Mo_Pic.png"
    data_knowledge_path = "C:\\Users\\User\\OneDrive - Michigan State University\\Data Science\\cmse830\\Final Project\\Webapp\\pictures\\data-knowledge.jpg"
    chem_joke_path = "C:\\Users\\User\\OneDrive - Michigan State University\\Data Science\\cmse830\\Final Project\\Webapp\\pictures\\chemistry-joke.jpg"
    foods_path = "C:\\Users\\User\\OneDrive - Michigan State University\\Data Science\\cmse830\\Final Project\\Webapp\\pictures\\foods.jpg"

    combined_html = f"""
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Sacramento&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="top-container">
            <div class="title-text">
                <h1>I'm Linqing.</h1>
                <h2>a <span class="pro">data scientist and chemist.</span></h2>
            </div>
            <img class="data-chem" src="data:image/png;base64,{get_base64_of_image(data_chemist_path)}" alt="data-chem">
        </div>
        <div class="middle-container">
            <div class="profile">
                <img class="mo-profile" src="data:image/png;base64,{get_base64_of_image(mo_pic_path)}" alt="mo-profile-img">
                <h2>Hello.</h2>
                <h4 class="intro">I am a chemist and data scientist graduate student working at Michigan State University. I ❤️ coding, cooking and music.</h4>
            </div>
            <hr>
            <div class="skills">
                <h2>My Skills.</h2>
                <div class="skill-row">
                    <img class="data-img" src="data:image/png;base64,{get_base64_of_image(data_knowledge_path)}" alt="data-img">
                    <h3>Data Science & Development</h3>
                    <h4>As a graduate student in Data Science, I have gained a wealth of experience analysing data and building models, complemented by my enduring interest in web and software development.</h4>
                </div>
                <div class="skill-row">
                    <img class="chem-joke" src="data:image/png;base64,{get_base64_of_image(chem_joke_path)}" alt="chem-joke-img">
                    <h3>Chemistry</h3>
                    <h4>With four years of reseach experience in chemistry, I'm the expert of organometallics and organic synthesis, with sound experience in characterization techniques like X-ray crystallography and chromatography.</h4>
                </div>
                <div class="skill-row">
                    <img class="foods" src="data:image/png;base64,{get_base64_of_image(foods_path)}" alt="foods-img">
                    <h3>Cooking</h3>
                    <h4>Truth be told, actually this is my best skill. I'm confident that my dishes rival those of the finest restaurants.</h4>
                </div>
            </div>
            <hr>
            <div class="contact-me">
                <h2>Contact Me.</h2>
                <h3>Want to know more about me? Follow my:</h3>
                <h4><a href="https://github.com/Mlzzzzz" target="_blank">Github</a></h4>
                <h4><a href="https://www.linkedin.com/in/linqing-mo-1897b4215/" target="_blank">LinkedIn</a></h4>
                <h4>Email: <a href="mailto:molinqin@msu.edu">molinqin@msu.edu</a></h4>
            </div>
        </div>
    </body>
    <style>
        .top-container {{
            background-color: #E4F9F5;
            padding-top: 100px;
            text-align: center;
        }}
        .title-text h1 {{
            font-family: 'Sacramento', cursive;
            color: #18453B;
            font-size: 5.625rem;
        }}
        .title-text h2 {{
            color: #18453B;
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            font-weight: normal;
            padding-bottom: 10px;
            text-align: center;
        }}
        .data-chem {{
            width: 30%;
            height: auto;
            margin-top: 40px;
        }}
        .middle-container {{
            padding-top: 100px;
            text-align: center;
        }}
        .mo-profile {{
            width: 22%;
            height: auto;
        }}
        .intro {{
            width: 40%; 
            margin: 0 auto; 
            color: #40514E;
            font-family: 'Merriweather', serif;
            text-align: center;
        }}
        .profile h2 {{
            color: #18453B;
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            font-weight: normal;
            padding-bottom: 10px;
            text-align: center;
        }}
        hr {{
            border: dotted #EAF6F6 6px;
            border-bottom: none;
            width: 4%;
            margin: 30px auto;
        }}
        .skills h2 {{
            color: #18453B;
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            font-weight: normal;
            text-align: center;
        }}
        .skill-row {{
            width: 50%;
            margin: 40px auto 40px auto;
            text-align: center;
        }}
        .skill-row h3{{
            color: #18453B;
            font-family: 'Montserrat', sans-serif;
            display: block;
            margin-block-start: 1em;
            margin-inline-start: 0px;
            margin-inline-end: 0px;
            font-weight: bold;
        }}
        .skill-row h4{{
            color: #40514E;
            font-family: 'Merriweather', serif;
            text-align: center;
        }}
        .data-img {{
            width: 100%; /* Adjust as needed, keeping it within 100% */
            height: auto; /* Maintain aspect ratio */
            display: block; /* Makes the margin auto centering work */
            margin: auto; /* Centers the image */
        }}
        .chem-joke {{
            width: 80%;
            height: auto;
        }}
        .foods {{
            width: 83%;
            height: auto;
        }}
        .contact-me h2 {{
            color: #18453B;
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            font-weight: normal;
            text-align: center;
        }}
        .contact-me h3{{
            color: #18453B;
            font-family: 'Montserrat', sans-serif;
            display: block;
            margin-block-start: 1em;
            margin-inline-start: 0px;
            margin-inline-end: 0px;
            font-weight: bold;
        }}
        .contact-me h4{{
            color: #40514E;
            font-family: 'Merriweather', serif;
            text-align: center;
        }}
    </style>
    """

    st.markdown(combined_html, unsafe_allow_html=True)
