import pandas as pd
import numpy as np
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import streamlit_option_menu as option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import altair as alt
import pydeck as pdk

slide1_loc = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/slide1.png'
slide2_loc = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/slide2.png'
slide3_loc = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/slide3.png'

slide1 = Image.open(slide1_loc)
slide2 = Image.open(slide2_loc)
slide3 = Image.open(slide3_loc)

st.set_page_config(layout="wide")
def lottie_url(url):
    request = requests.get(url)
    if request.status_code != 200:
        return None
    return request.json()

lt_siri = lottie_url("https://lottie.host/7503d066-a7e4-4303-8b99-13d60f72d1a2/ghkg9nhmxo.json")
lt_soon = lottie_url("https://lottie.host/a1eee7b1-cc91-4e1a-96b4-f6d8f7ef7de6/Myo4fYMbcC.json")

st.title("Chacha Chowdhury")
st.write('''Hello I'm Chacha Chowdhury, 
     I'm :rainbow[ **AI**] bot helps to provide solution about the :rainbow[ **NAMAMI GANGE**]''')
st.write("[READ MORE](https://nmcg.nic.in/ )")
st.write('---')

with (st.container()):
    menu = option_menu.option_menu(
        menu_title=None,
        options=['Chat Area', 'Overview', 'About Us', 'Machine Learning Area'],
        icons=['code-slash', 'eye', 'chat-left-text-fill', 'person'],
        orientation='horizontal'
    )
    if menu == 'Chat Area':
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.title("Welcome to :rainbow[*Chat Area*]")
                st.write("Designed for Namami Gange")
                st_lottie(lt_siri)


            with col2:
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")

                def main():
                    load_dotenv()

                    user_csv = 'C:/Users/rouna/OneDrive/Documents/WebDevelopmentProject/Python/SIH/assets/dataset.csv'

                    #st.file_uploader("Upload Area", type="csv")

                    if user_csv is not None:
                        user_question = st.text_input("Chat Box")

                        llm = OpenAI(temperature=0)
                        agent = create_csv_agent(llm, user_csv, verbose=True)

                        if user_question is not None and user_question != "":
                            response = agent.run(user_question)
                            st.write(f"Your have asked: {user_question}")

                if __name__ == "__main__":
                    main()

    if menu == 'Overview':
        with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                st.title("Welcome to :rainbow[*Overview*]")
                st.write("##")
                st.write("##")
                st.image(slide1)

            with col2:
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.image(slide2)
            with col3:
                st.write("##")
                st.write("##")
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
                st.write("##")
                st.write("##")
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
                st.write("##")
                st.write("##")
                st.write('''\n1. https://nmcg.nic.in/ 
                \n2. http://cganga.org/scientific-advisory-committee/ 
                \n3. http://nihroorkee.gov.in/Gangakosh/ganga.htm 
                \n4. http://gangapedia.in/ 
                \n5. https://www.gangaaction.org/ganga-gyan-dhara-samgra-samvaad-workshop-for-clean-ganga/
                \n6. https://clap4ganga.com/
                ''')

    if menu == 'Machine Learning Area':
        with st.container():
            col5, col6 = st.columns(2)

            with col5:
                st.title("Welcome to :rainbow[*Machine Learning Area*]")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.title("More :rainbow[*Features*]")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st.write("##")
                st_lottie(lt_soon)

            with col6:
                st.write("##")
                st.write("##")
                st.write("##")
                upload = st.file_uploader('Please upload .csv file', type='csv')
                if upload:
                    st.write('---')
                    dataset = pd.read_csv(upload, engine='python')
                    st.dataframe(dataset)

                    st.header("Scatter Plot")
                    chart = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Color'])
                    c = alt.Chart(chart).mark_circle().encode(x='X', y='Y', size='Color', color='Color',
                                                              tooltip=['X', 'Y', 'Color'])
                    st.altair_chart(c, use_container_width=True)
                    st.area_chart(chart)
                    st.line_chart(chart)
                    st.bar_chart(chart)
                    #
                    st.header("Map")
                    chart_data = pd.DataFrame(
                        np.random.randn(1000, 2) / [50, 50] + [25.53964636017534, 83.19580536400075],
                        columns=['lat', 'lon'])

                    st.pydeck_chart(pdk.Deck(
                        map_style=None,
                        initial_view_state=pdk.ViewState(
                            latitude=25.53964636017534,
                            longitude=83.19580536400075,
                            zoom=11,
                            pitch=50,
                        ),
                        layers=[
                            pdk.Layer(
                                'HexagonLayer',
                                data=chart_data,
                                get_position='[lon, lat]',
                                radius=200,
                                elevation_scale=4,
                                elevation_range=[0, 1000],
                                pickable=True,
                                extruded=True,
                            ),
                            pdk.Layer(
                                'ScatterplotLayer',
                                data=chart_data,
                                get_position='[lon, lat]',
                                get_color='[200, 30, 0, 160]',
                                get_radius=200,
                            ),
                        ],
                    ))
                    #
                    df = pd.DataFrame({
                        "col1": np.random.randn(1000) / 50 + 25.53964636017534,
                        "col2": np.random.randn(1000) / 50 + 83.19580536400075,
                        "col3": np.random.randn(1000) * 100,
                        "col4": np.random.rand(1000, 4).tolist(),
                    })

                    st.map(df,
                           latitude='col1',
                           longitude='col2',
                           size='col3',
                           color='col4')


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
st.write("CC version 2")
