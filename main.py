# from dotenv import load_dotenv
# load_dotenv()
# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("hi!")
# print (result)

import streamlit as st
import time

st.header('인공지능 시인 대박', divider='rainbow')

st.title('-- 버튼 누르면 실행 만들기 ')


title = st.text_input("시의 주제를 제시해주세요.")
# st.write("시의 주제는 : ", title)

if st.button("시 작성 요청 버튼"):
    with st.spinner('테스트 중.'):
        time.sleep(5)
    st.write("시")


# st.title('_Streamlit_ is :blue[cool] :sunglasses:')