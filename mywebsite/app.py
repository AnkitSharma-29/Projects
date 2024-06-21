import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r =requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

#---load section-----
lottie_coding="https://lottie.host/67de458b-a726-47cd-8858-b01aa8cca5a9/cn3BvJcGgW.json"

#-----header section ----
st.subheader("Hi,I am Ankit :wave:")
st.title("A Data Analyst From INDIA")
st.write("I am passionate about finding ways to use Python and R to be more efficient and effective in business")
st.write("[Learn More>](https://interesto.online)")

#------WHAT I DO------
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""  As a Computer Science and Data Science student, I'm passionate about technology and data analysis. I thrive on solving complex problems and have a solid foundation in programming, machine learning, and statistics. I'm an avid learner, constantly seeking new knowledge and skills to further my understanding of these fields. I'm actively seeking research opportunities or internships to apply my skills in real-world settings and contribute to innovative projects. With strong analytical and problem-solving abilities, I'm eager to learn and make meaningful contributions in the fields of computer science and data science.
            """
        )
        st.write("[youtube channel>](https://youtube.com)")
with right_column:
    st_lottie(lottie_coding,height =400,key="coding")

#----CONTACT----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")   

    # Documention:https://formsumit.co/ !!! change email address !!! 
    contact_form = """
     <form action="https://formsubmit.co/csvtustudent@gmail.com" method="POST">
     <input type="hidden" name=""_captcha" value"false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name = "message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
