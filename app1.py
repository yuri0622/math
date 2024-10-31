# streamlit 라이브러리 불러오기
import streamlit as st      

st.title('동생아 공부 열심히 해')  
st.subheader('오늘의 주제: 양수와 음수')
st.write('음수?? 어렵지 않아!') 

col1, col2 = st.columns(2)       

with col1:
st.subheader('**개념정리')
st.write('- 양수: 0보다 큰 수')
st.write('- 음수: 0보다 작은 수')
st.write('- 양수: (+) / 음수: (-) 부호가 붙음')
st.write('- 부호: (+)는 생략 가능 /(-)는 생략 불가')

with col2:
st.image('수학이미지.PNG')  # 이미지 파일 불러오기

# 사용자의 입력을 받아서 a에 저장하기(초기값은 0)
a = st.number_input('수를 입력하세요', value= 0)  

# 버튼 생성 및 동작
if st.button('양수일까 음수일까?'):
       if a > 0:
              st.write('________')
       elif a < 0:
              st.write('________')
       else:
              st.write('________')
