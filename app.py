import streamlit as st
import streamlit_authenticator as stauth

names = ['John Smith','Rebecca Briggs']
usernames = ['jsmith','rbriggs']
hashed_passwords = ['$2b$12$aQHnEmGfUTtauDP41PZTtObwLayhR3Nrui4PInymtv0J5OvjPYa4O',
 '$2b$12$43.4ixYKxSr22wPj3HfGzum7pNO0IMMYkV6eOyXyT8WMFWsJJRhMK']

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Login','main')

if authentication_status:
    st.write('Welcome *%s*' % (name))
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')





