import streamlit as st 
from streamlit_lottie import st_lottie
import requests
import json


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_py = load_lottiefile("Python logo.json")   # local file
lottie_robo = load_lottiefile("Ai-powered marketing tools abstract.json")   # local file

st_lottie(lottie_py, height=150)


st.set_page_config(page_title="Factorization Formulas", page_icon="🧮", layout="centered")
st.title("Most Important Factorization Formulas", text_alignment="center")
st.divider()

st.markdown("*Formulas:*")

st.write("**[1]. Square Of Binomial (a + b)**")
st.latex(r"(a + b)^2 = a^2 + 2ab + b^2")

st.write("**[2]. Square Of Binomial (a - b)**")
st.latex(r"(a - b)^2 = a^2 - 2ab + b^2")

st.write("**[3]. Cude Of Binomial (a + b)**")
st.latex(r"(a+b)^3 = a^3 + b^3 + 3ab(a+b)")

st.write("**[4]. Difference Of Squares**")
st.latex(r"(a^2 - b^2) = (a-b)(a+b)")

st.write("**[5]. Sum of Cubes**")
st.latex(r"a^3 + b^3 = (a+b)(a^2-ab+b^2)")

st.write("**[6]. Sum of Squares**")
st.latex(r"a^3 - b^3 = (a-b)(a^2+ab+b^2)")

st.divider()

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("**Enter Value Of [a]:**")
with col2:
    b = st.number_input("**Enter Value Of [b]:**")

st.divider()

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("Square Of Binomial (a + b)"):
        st.divider()
        sbs = (a+b)**2
        st.success(sbs)

with c2:
    if st.button("Square Of Binomial (a - b)"):
        st.divider()
        sbm = (a-b)**2
        st.success(sbm)

    
with c3:
    if st.button("Cube Of Binomial (a + b)"):
        st.divider()
        cb = (a + b)**3
        st.success(cb)
    
with c4:
    if st.button("Difference Of Squares"):
        st.divider()
        ds = a**2 - b**2
        st.success(ds)

    
with c5:
    if st.button("Sum of Cubes"):
        st.divider()
        sc = a**3 + b**3
        st.success(sc)

    
with c6:
    if st.button("Difference Of Cubes"):
        st.divider()
        dc = a**3 - b**3
        st.success(dc)

    
st.divider()

st_lottie(lottie_robo, height=200)
