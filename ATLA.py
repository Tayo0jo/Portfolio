import streamlit as st
import datta
import pandas as pd
import requests
base_url = "https://last-airbender-api.fly.dev/api"

#Intro Page
def intro_page():
    st.header("Welcome to the Avatar: The Last Airbender Character Encyclopedia!")
    st.image('images/title.jpeg', width = 700)
    st.write("Immerse yourself in the four nations' cultures and learn about the fascinating people who have shaped this unique cosmos. Choose your favorite characters from Aang's epic quest,then learn about their histories, skills, and connections.")
    
intro_page()

def fetch_character_info(character_name):
    api_url = f"https://last-airbender-api.fly.dev/api/v1/characters?name={character_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None
def is_ally_of_aang(character_name):
    api_url = f"https://last-airbender-api.fly.dev/api/v1/characters?allies=Aang"
    response = requests.get(api_url)
    if response.status_code == 200:
        allies = [ally['name'] for ally in response.json()]
        return character_name in allies
    return False



def sidedrop():
    st.header("Choose a charecter!")
    st.write("Once you pick a charecter you will receive various information regarding them like their allies and enemies, as well as their affiliation.")
    avatar_characters = [
    'Aang', 'Katara', 'Sokka', 'Toph Beifong', 'Zuko',
    'Iroh', 'Azula', 'Appa', 'Momo', 'Suki',
    'Ozai', 'Ty Lee', 'Mai', 'Jet', 'Cabbage Merchant'
]
    selected_character = st.selectbox('Select a character', avatar_characters)#NEW
    st.write('You chose:', selected_character)
    if st.button('Get Character Info'):#NEW
        character_info = fetch_character_info(selected_character)
        if character_info:
            character = character_info[0]
            st.write(f"### {selected_character}")
            st.image(character['photoUrl'], caption=f"Image of {selected_character}")
            st.write(f"Name: {selected_character}")
            st.write(f"Affiliation: {character['affiliation']}")
            st.write(f"Allies: {', '.join(character['allies'])}" if character['allies'] else "No allies listed")
            st.write(f"Enemies: {', '.join(character['enemies'])}" if character['enemies'] else "No enemies listed")
sidedrop()

def avatar():
    st.header("Are they an ally of the Avatar?")
    st.write("Select a charecter and test to see if they are in good standings with the current avatar!")
    avatar_characters = [
    'Haru', 'Pathik', 'Toph Beifong', 'Zuko', 'Iroh', 'Azula', 'Lian and Shen', 'Foaming mouth guy', 'Suki', 'Ozai',
    'Three-Eyed-Man', 'Mai', 'Jet', 'Cabbage Merchant'
]
    selected_character = st.radio('Select a potential ally', avatar_characters)#NEW
    if st.button('Check'):
            is_ally = is_ally_of_aang(selected_character)
            if is_ally:
                st.write(f"{selected_character} is an ally of Aang!")
                st.image("images/happy.png", width = 400)
            else:
                st.write(f"{selected_character} is not an ally of Aang.")
                st.image("images/angry.jpeg", width = 400)
avatar()

