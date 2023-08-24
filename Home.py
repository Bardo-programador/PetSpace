import streamlit as st 
from st_pages import Page, show_pages, add_page_title, hide_pages
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title='Petshop', page_icon='🐶')
st.sidebar.title('Menu')
# show_pages([
#     Page("Home.py", "Home"),
#     Page("pages/Funcionário.py", "Funcionário"),
#     Page("pages/Usuário.py", "Usuário"),
# ])
hide_pages(["Funcionário", "Usuário"])
if st.button("Página de funcionário"):
  switch_page("Funcionário")

if st.button("Usuárii"):
  switch_page("Usuário")