import streamlit as st

st.title('Todo')

login, signup = st.tabs(["Log In", "Sign Up"])
with login:
    with st.form("login_form"):
       st.title("Log In")
       lgmail = st.text_input('', placeholder='Enter your Email')
       lpaswd = st.text_input('', placeholder='Enter your Password', type='password')
       lsubmit = st.form_submit_button("Log In", type="primary")

       if lsubmit:
           if lgmail and lpaswd :
               file1 = open("C:/Users/gbvsa/PycharmProjects/pythonProject/Todo/users.txt", "r")
               lgp = lgmail+" "+lpaswd+"\n"
               if lgp in file1.readlines():
                   st.success('LogIn Successful')
                   file1.close()
               else:
                   st.error('Wrong Email/Password', icon="🚨")

           else:
               st.error('All Fields are required', icon="🚨")

with signup:
       with st.form("my_form"):
           st.title("Sign Up")
           sfname = st.text_input('', placeholder='Enter your First Name')
           slname = st.text_input('', placeholder='Enter your Last Name')
           sgmail = st.text_input('', placeholder='Enter your Email')
           spaswd = st.text_input('', placeholder='Enter your Password', type='password')
           scheckbox_val = st.checkbox("Agree to all Terms and Conditions")

           ssubmit = st.form_submit_button("Sign Up", type="primary")
           if ssubmit:
               if sfname and slname and sgmail and spaswd and scheckbox_val:
                   if sgmail.__contains__(" ") or spaswd.__contains__(" "):
                       st.error('Email/Password not valid.', icon="🚨")
                   else:
                       file1 = open("C:/Users/gbvsa/PycharmProjects/pythonProject/Todo/users.txt", "r")
                       sgp = sgmail+" "+spaswd+"\n"
                       if sgp in file1.readlines():
                           st.error('Email already Exists.', icon="🚨")
                           file1.close()
                       else:
                           file1 = open("C:/Users/gbvsa/PycharmProjects/pythonProject/Todo/users.txt", "w")
                           file1.write(sgp)
                           file1.close()
                           st.success('Registered Successfully')
               else:
                   st.error('All Fields are required', icon="🚨")





