import streamlit as st
from db import init_db

def admin_dashboard():
    st.title("Admin Dashboard - Device Table")
    conn = init_db()

    st.subheader("Device Inventory Table")
    rows = conn.execute("SELECT * FROM devices").fetchall()
    st.table(rows)

    st.subheader("Actions")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Insert"):
            st.switch_page("insert_device.py")
    with col2:
        if st.button("❌ Delete"):
            st.switch_page("delete_device.py")
    with col3:
        if st.button("✏ Update"):
            st.switch_page("update_device.py")
