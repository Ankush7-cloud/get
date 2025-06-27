import streamlit as st
from signup import signup
from login import login
from home import home
from admin_dashboard import admin_dashboard
from user_management import user_management
from resource_management import resource_management
from insert_device import insert_device
from delete_device import delete_device
from update_device import update_device

# Set page config
st.set_page_config(page_title="Device Management App", layout="wide")

# Initialize session
if "username" not in st.session_state:
  st.session_state["username"] = None
  st.session_state["role"] = None
  st.session_state["page"] = "Home"

# Logout functionality
if st.session_state["username"]:
  st.sidebar.markdown(f"👤 Logged in as: {st.session_state.username}")
  if st.sidebar.button("Logout"):
      st.session_state.clear()
      st.experimental_rerun()

# Role-based navigation
if st.session_state["username"]:
  role = st.session_state["role"]

  if role == "admin":
    menu = st.sidebar.selectbox("Admin Menu", [
            "Dashboard",
            "Insert Device",
            "Delete Device",
            "Update Device",
            "User Management",
            "Resource Management"
        ])
        if menu == "Dashboard":
          admin_dashboard()
        elif menu == "Insert Device":
          insert_device()
        elif menu == "Delete Device":
          delete_device()
        elif menu == "Update Device":
          update_device()
        elif menu == "User Management":
          user_management()
        elif menu == "Resource Management":
          resource_management()

  elif role == "user":
    menu = st.sidebar.selectbox("User Menu", [
            "User Management",
            "Resource Management"
        ])
        if menu == "User Management":
          user_management()
        elif menu == "Resource Management":
          resource_management()

# Unauthenticated users
else:
  menu = st.sidebar.selectbox("Menu", ["Home", "Signup", "Login"])

    if menu == "Home":
     home()
   elif menu == "Signup":
     signup()
   elif menu == "Login":
     login()
