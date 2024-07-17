import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("宝贝天堂 Baby Paradise")
st.write("""
《无缘子女》当精卵结合成胎之际即有生命的迹象。据《地藏经》所
载,亲子关系来自报恩报怨讨债及还债4种宿生缘,然而,由于诸多俱
因如流产,堕胎,夭折等,使宿生缘被终止小生命无法诞生于人间,
这种来不及出生的无缘宝宝,多称之为【无缘子女】或【婴灵】。

世间有情生命,都希望远离痛苦,得享安乐的生活,无辜的小生命不
幸夭折后,稚幼的童魂也渴望极关心,被呵护。无论是堕胎或不小心
流产的胎儿,无论事隔多久,都应该尽力为这些来不及出生的无缘子

女超渡迴向。""")
st.write("""
Babies who pass away prematurely, whether through miscarriage, abortion, or early
death, are affectionately known as infant spirits. They return to heaven before fully
experiencing life on earth, leaving behind a tender spiritual connection.

Releasing them from suffering through blessing rituals can help ease the inner guilt of

parents and bring relief to the spirits in the underworld.""")
image1 = Image.open("image/kulai29.png")
st.image(image1.resize((720, 360)))