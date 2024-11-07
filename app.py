import streamlit as st
import pandas as pd
import numpy as np



#一个输入的文本框
st.text_input("输入字符串",key="name")

st.number_input("输入年龄",key="age")

st.date_input("选择出生日期",key="birthday")

a=2

if st.button("生成"): st.write(a)

# st.download_button(
#     label="下载",
#     data= "",
#     file_name="test.docx",
#     mime="text/docx"
# )


