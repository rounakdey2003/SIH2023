from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import streamlit_option_menu as option_menu
import requests
from PIL import Image

gange_loc = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/gange.png'
slide2_loc = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/slide2.png'
slide3_loc = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/slide1.png'
gange = Image.open(gange_loc)
slide2 = Image.open(slide2_loc)
slide3 = Image.open(slide3_loc)

st.set_page_config(layout="wide")

bg_image = """
                <style>
                [data-testid = "stAppViewContainer"] > .main {
                background-image: url("https://i.pinimg.com/originals/a7/9e/69/a79e69f1e792d396467b4a49f52f6497.gif");
                background-size: 100%;
                background-repeat: no-repeat;
                background-attachment: local;
                }
                </style>
                """
st.markdown(bg_image, unsafe_allow_html=True)

st.title("Chacha Chowdhury")
st.write('''Hello I'm Chacha Chowdhury, 
     I'm :rainbow[ **AI**] bot helps to provide solution about the :rainbow[ **NAMAMI GANGE**]''')
st.write("[READ MORE](https://nmcg.nic.in/ )")
st.write('---')

with st.container():
    menu = option_menu.option_menu(
        menu_title=None,
        options=['Chat Area', 'Overview', 'About Us', 'Features'],
        icons=['code-slash', 'eye', 'chat-left-text-fill', 'person'],
        orientation='horizontal'
    )
    if menu == 'Chat Area':
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.write("##")
                st.write("##")
                st.title("Welcome to :rainbow[*Chat Area*]")
                st.write("Designed for Namami Gange")
                #st_lottie(lt_image)
                st.write("##")
                st.write("##")

                st.image(gange)

                st.write("##")
                st.write("##")
                

            with col2:
                st.write("##")
                st.write("##")
                def main():
                    load_dotenv()

                    user_csv = st.file_uploader("Upload Area", type="csv")

                    if user_csv is not None:
                        user_question = st.text_input("Hii, How can I help you ?")

                        llm = OpenAI(temperature=0)
                        agent = create_csv_agent(llm, user_csv, verbose=True)

                        if user_question is not None and user_question != "":
                            response = agent.run(user_question)
                            st.write(f"Your have asked: {user_question}")

                if __name__ == "__main__":
                    main()

    if menu == 'Overview':
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.title(":rainbow[*Overview*]")
                st.write("##")
                st.image(slide2)
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")

            with col2:
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.image(slide3)


    if menu == 'About Us':
        with st.container():
            col3, col4 = st.columns(2)

            with col3:
                st.write("##")
                st.header("*INTRODUCTION*")
                st.write('''\n:rainbow[**Chacha Chaudhary**] was declared the mascot of the :rainbow[Namami Gange Programme] at the 37th Executive Committee meeting of the National Mission for Clean Ganga (NMCG). 
                \nNMCG has tied up with Diamond Toons to develop and distribute comics, e-comics, and animated videos. 
                \nThe objective of bringing about behavioral change amongst children towards the Ganga and other rivers. 
                \nTo make this solution more interactive one step further ahead, :rainbow[**AI, ML & Chat bot-powered**] Interactive Robot Mascot (Chacha Chaudhary) would add value to the product for the river people connect component of Namami Gange. 
                \n:rainbow[**Prerequisites:**] It should be an independent robot to connect with the School children, the common man, and all stakeholders of NMCG for creating awareness & information dissemination. The product should be user- friendly & citizen-centric. 
                \n:rainbow[**Solution:**] An interactive robot named “Chacha Chaudhary” would be the Artificial intelligence & machine learning & chat boat-enabled mascot of the Namami Gange made with the help of a touch panel, greets visitors at the entrance and takes them along to each component of the Namami Gange flagship program in River Basin War Room & Ganga Museum. 
                \nThe digital avatar of Chacha Chaudhary would also enable on the NMCG website. Robot Mascot (Chacha Chaudhary) & digital avatar solution would be providing to actively engage with citizens to impart information, awareness, and education around riverine ecology in an interactive format of digital and outdoor installations. 
                ''')
            with col4:
                st.write("##")
                st.header("*Important Links*")
                st.write('''\n1. https://nmcg.nic.in/ 
                \n2. http://cganga.org/scientific-advisory-committee/ 
                \n3. http://nihroorkee.gov.in/Gangakosh/ganga.htm 
                \n4. http://gangapedia.in/ 
                \n5. https://www.gangaaction.org/ganga-gyan-dhara-samgra-samvaad-workshop-for-clean-ganga/
                \n6. https://clap4ganga.com/
                ''')

    if menu == 'Features':
        with st.container():
            col5, col6 = st.columns(2)

            with col5:
                st.title(":rainbow[Coming Soon]")

st.write("##")
st.write("---")
st.title("Subscribe to our :rainbow[*Newsletter*]")
email = st.text_input("Please subscribe to our page. (Enter your email address)")
rate = st.selectbox("Please give us a rating", ('Outstanding', 'Good', 'Understandable', 'Poor'))
button = st.button("Submit")
if button:
    st.markdown(f"""
    Your Inputs
    \nEmail: :rainbow[{email}]
    \nRating: :rainbow[{rate}]
    """)

st.write("---")
st.write("Version 2")
