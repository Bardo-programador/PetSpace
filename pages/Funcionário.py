import streamlit as st
import crud
import pandas as pd
crud.create_table()

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
    if st.button('Salvar'):
        crud.insert_pet(nome_dono, nome_pet, raca, descricao)
        st.success('Pet inserido com sucesso!')
    
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

        