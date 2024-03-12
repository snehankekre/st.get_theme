import streamlit as st

st.info("When you change the theme, move the slider to see the theme value update")
st.slider("Slider")

st.write("The current theme is",
st.get_theme()
)

with st.expander("Show code"):
    st.code("""
import streamlit as st

st.caption("When you change the theme, move the slider to see the theme value update")
st.slider("Slider")

st.write("The current theme is",
st.get_theme()
)
""")
