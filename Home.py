import streamlit as st

st.set_page_config(layout="wide")
st.header("Welcome to our Nirvana Page， 欢迎来到")

st.image("image/kulai1.jpg")

content1 = """
✨事前规划，心无牵挂✨\n
根据自己的意愿规划，无需贷款 0% 利息供期✔\n
全方位的一条龙服务⭐⭐⭐⭐⭐

我提供的服务包括：“骨灰福位、风水宝地、殡仪配套、遗嘱规划、神主牌位、龙龟生基"""
st.write(content1)

col1, emptycol1, col2 = st.columns([2, 0.5, 2])
with col1:
    st.image("image/kulai2.jpg")

with col2:
    st.image("image/kulai3.jpg")
