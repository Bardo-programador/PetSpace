import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ['admin', 'user']
usernames = ['admin', 'user']
passwords = ['admin', 'user']

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open('wb') as f:
    pickle.dump(hashed_passwords, f)
