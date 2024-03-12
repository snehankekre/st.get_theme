import streamlit as st

st.info("When you change the theme, click the button to see the theme value update")
st.button("Show theme value")

st.write("The current theme is",
st.get_theme()
)


with st.expander("Show code"):
    st.code("""
st.write("The current theme is",
st.get_theme()
)
""")
