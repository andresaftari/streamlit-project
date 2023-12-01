import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

st.title('Hola, welcome to Andzzz Streamlit!')

show_pages(
    [
        Page('streamlit_app.py', "Home", '🏠'),
        # The section itself will look like a normal page, but it won't be clickable
        Section(name='Example Code', icon='🐍'),
        Page('pages/tugas_mod_1.py', 'Pengenalan Python', '🐍'),
    ]
)

add_page_title()
