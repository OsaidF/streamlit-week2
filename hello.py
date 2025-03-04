import streamlit as st

st.set_page_config(
    page_title="Unit Converter Project",
    page_icon=":scales:",
)


st.header('Unit Converter Project _by :red[Osaid]_')
st.subheader('Click on one of the tabs in the sidebar on the links down below to begin!')
st.balloons()

st.page_link("pages/converter.py", label="Unit Convertor", icon="⚖️")
st.page_link("pages/ai-converter.py", label="AI Unit Converter", icon="💻")