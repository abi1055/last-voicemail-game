import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play 
import os 

load_dotenv()

#loading in API key 
elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

st.set_page_config(page_title= "The Last Voicemail - Mystery Game")

st.title("The Last Voicemail - Mystery Game") 
st.write("You wake up to find three missed voicemails on your phone.")

player_name = st.text_input("Enter your name")

voicemails = {
    "Jake - 8:14 PM": (
        f"Hi, it's Jake. {player_name}, please call me back. I saw something strange near the old train station."
    ), 
    "Detective Deborah - 8:32 PM": (
        "This is Detective Deb. We need to speak about the phone you found last night."
    ),
    "Unknown Number - 8:47 PM": (
        "Do not trust either of them. Meet me at the train station before midnight."
    )
}

selected_message = st.radio(
    "Which voicemail do you listen to first?",
    list(voicemails.keys())
)

if st.button("Play voicemail"):
    st.subheader(selected_message)
    st.write(f'"{voicemails[selected_message]}"')

    if selected_message == "Jake - 8:14 PM":
        st.info("Jake sounds scared. Do you go to the train station?")
    elif selected_message == "Detective Deborah - 8:32 PM":
        st.info("Why does the detective know about the phone?")
    else:
        st.warning("The caller hands up brefore you can respond.")

#SDK client

#convert function

#save the response as mp3 your app can use