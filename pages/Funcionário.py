import streamlit as st
import crud
import pandas as pd
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, add_page_title

## --- Autenticador ---
names = ['admin']
usernames = ['admin']
crud.create_table()

## -- Carregar senhas --
file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open('rb') as f:
    hashed_passwords = pickle.load(f)
credenciais ={'usernames': {user: {'name': name, 'password': password} for user, name, password in zip(usernames, names, hashed_passwords)}}
autenticador = stauth.Authenticate(credenciais, "cookie_demo", "abdef")
name, authentication_status, username = autenticador.login('Login', 'main')
if st.button("Voltar"):
    switch_page("Home")
if st.session_state['authentication_status']:
    autenticador.logout("Sair", 'sidebar')
    inserir, visualizar, atualizar, deletar = st.tabs(['Inserir', 'Visualizar', 'Atualizar', 'Deletar'])
    with visualizar:
        st.title('Visualizar')
        st.write('Aqui você pode visualizar os dados dos pets cadastrados no banco de dados.')

        pets = crud.get_pets()
        df = pd.DataFrame(pets, columns=['ID', 'Nome do dono', 'Nome do pet', 'Raça', 'Descrição'])
        st.table(df)

    with inserir:
        st.title('Inserir')
        nome_dono = st.text_input('Nome do dono')
        nome_pet = st.text_input('Nome do pet')
        raca = st.text_input('Raça')
        descricao = st.text_area('Descrição')
        vacinacao = st.checkbox('Vacinado')
        reativo = st.checkbox('Reativo')
        restricao = st.checkbox('Restrição')
        if st.button('Salvar'):
            try:
                crud.insert_pet(nome_dono, nome_pet, raca, descricao,vacinacao,reativo,restricao)
                st.success('Pet inserido com sucesso!')
            except TypeError:
                st.error('Erro ao inserir pet!')
        
    with atualizar:
        st.title('Atualizar')
        st.write('Aqui você pode atualizar os dados dos pets cadastrados no banco de dados.')

        id_pet = st.number_input("Qual ID você deseja atualizar?", step = 1)
        nome_dono = st.text_input('Novo nome do dono')
        nome_pet = st.text_input('Novo nome do pet')
        raca = st.text_input('Nome da raça')
        descricao = st.text_area('Nova descrição')
        if st.button('Atualizar'):
            if crud.get_pet(id_pet) == None:
                st.error('ID não encontrado!')
            if nome_dono == '':
                nome_dono = crud.get_pet(id_pet)[1]
            if nome_pet == '':
                nome_pet = crud.get_pet(id_pet)[2]
            if raca == '':
                raca = crud.get_pet(id_pet)[3]
            if descricao == '':
                descricao = crud.get_pet(id_pet)[4]
            crud.update_pet(id_pet, nome_dono, nome_pet, raca, descricao)
            st.success('Pet atualizado com sucesso!')
        
    with deletar:
        st.title('Deletar')
        st.write('Aqui você pode deletar os dados dos pets cadastrados no banco de dados.')

        id_pet = st.number_input("Qual ID você deseja deletar?", step = 1)
        
        if st.button('Deletar'):
            if crud.get_pet(id_pet) == None:
                st.error('ID não encontrado!')
            else:
                crud.delete_pet(id_pet)
                st.success('Pet deletado com sucesso!')

if st.session_state['authentication_status'] == False:
    st.error('Usuário ou senha incorretos!')

if st.session_state['authentication_status'] == None:
    st.info('Faça o login para continuar')           