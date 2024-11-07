import streamlit as st
from openpyxl import Workbook, load_workbook


wb = load_workbook('身高曲线图.xlsx')


#一个输入的文本框
st.text_input("输入字符串",key="name")

sex = st.selectbox(
    label='请选择性别：',
    options=['男','女']
)

sheet = wb[sex]
age =  sheet['v3'].value
# ws = wb.active
# ws._images[0] # 第一张图片对象
# data = ws._images[0]._data() # 图片的字节数据
# st.image(data)

st.date_input("选择出生日期",key="birthday")

if st.button("生成"):
    st.write(age)


with open('Template.docx', 'rb') as file:
    st.download_button(
        label="下载",
        data= file,
        file_name="test.docx",
        mime="text/docx"
    )


