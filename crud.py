import streamlit as st
import sqlite3

#Função para criar a tabela no banco de dados, se ainda não existir
def create_table():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_name TEXT,
            pet_name TEXT,
            breed TEXT,
            description TEXT
        )
        
    ''')
    conn.commit()
    conn.close()

#Função para inserir um novo pet no banco de dados
def insert_pet(owner_name, pet_name, breed, description):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pets (owner_name, pet_name, breed, description)
        VALUES (?, ?, ?, ?)
    ''', (owner_name, pet_name, breed, description))
    conn.commit()
    conn.close()

#Função para atualizar os dados de um pet no banco de dados
def update_pet(id, owner_name, pet_name, breed, description):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pets
        SET owner_name=?, pet_name=?, breed=?, description=?
        WHERE id=?
    ''', (owner_name, pet_name, breed, description, id))
    conn.commit()
    conn.close()

#Função para deletar um pet do banco de dados
def delete_pet(id):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pets WHERE id=?', (id,))
    conn.commit()
    conn.close()

#Função para recuperar todos os pets do banco de dados
def get_pets():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets')
    pets = cursor.fetchall()
    conn.close()
    return pets #

#Função para recuperar um pet específico do banco de dados
def get_pet(id):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets WHERE id=?', (id,))
    pet = cursor.fetchone()
    conn.close()
    return pet

# get_pet(1)