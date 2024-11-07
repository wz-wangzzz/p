import streamlit as st

#一个输入的文本框
st.text_input("输入字符串",key="name")
sex = st.selectbox(
    label='请选择性别：',
    options=['男','女']
)

st.date_input("选择出生日期",key="birthday")
st.text_input("输入父亲身高",key="fathersHeight")
st.text_input("输入母亲身高",key="mothersHeight")
st.text_input("输入骨龄",key="boneAge")
st.text_input("输入身高",key="height")
st.text_input("输入体重",key="weight")

if st.button("生成"): st.write(111)

with open('Template.docx', 'rb') as file:
    st.download_button(
        label="下载",
        data= file,
        file_name="test.docx",
        mime="text/docx"
    )


