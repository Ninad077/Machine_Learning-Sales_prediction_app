import requests
import streamlit as st
from PIL import Image
import webbrowser as web
import streamlit.components.v1 as components


# ---- HEADER SECTION ----
with st.container():
    st.header(":red[Howdy, I'm Ninad :)]")
    st.write("Aspiring Data Scientist. Weirdly passionate about Maths, Machine Learning & programming")
    st.write("[Learn More >](https://www.linkedin.com/in/ninad-s-mandavkar-12328715b/)")
    

# ---- ABOUT ME ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(":red[About me]")
        st.write(
            "Let me give a brief introduction of myself. I am Ninad. A Master's graduate from TU Ilmenau, Germany. I love to code, deploy ML algorithms and play around with data. Maths is something that I was always enamoured by and apparently the prime reason for my inclination towards Data Science as a field. I am equally curious about leveraging Deep Learning, NLPs & AI as a tool to enhance productivity in the workforce. **I strongly believe in being passionate, curious & resilient.** Nuf' said, to know more about me do visit my social media handles below. Also, for official queries one can drop me a mail."

        )
        with right_column:
            st.image('Ninad_photo.jpeg')
    
    with left_column:
        st.write('##')
        st.write('')
        st.write("---")
        st.subheader(":red[Check out my profile]")
        components.html("""<div><a href="https://github.com/Ninad077" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
                        <a href="https://www.linkedin.com/in/ninad-s-mandavkar-12328715b" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
                        <a href="https://medium.com/@ninadmandavkar28" target="blank"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="35" fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16">
                        <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8m4.95 0c0 2.34-1.01 4.236-2.256 4.236S9.463 10.339 9.463 8c0-2.34 1.01-4.236 2.256-4.236S13.975 5.661 13.975 8M16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795"/>
                        </svg></div>""")

    with right_column:
        st.write("---")
        st.subheader(":mailbox: :red[Get in touch with me!]") 
        contact_form = """<form action="https://formsubmit.co/ninadmandavkar28@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your name" required>
        <input type="email" name="email" placeholder= "Your email" required>
        <textarea name="message" placeholder="Your message"></textarea>
        <button type="submit">Send</button>
        </form>"""

        st.markdown(contact_form,unsafe_allow_html=True)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

        local_css("style/style.css.txt")