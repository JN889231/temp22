import streamlit as st
import requests

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "full_message" not in st.session_state:
    st.session_state["full_message"] = ""

st.title("테스트")

# 사용자 텍스트 입력
if prompt := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    max_messages = 5

    messages_to_send = st.session_state["messages"][-max_messages:]
    response = requests.post("http://13.125.119.225/chat", json={"messages": messages_to_send})

    if response.status_code == 200:
        assistant_response = response.json().get("response", "")
        st.session_state["messages"].append({"role": "assistant", "content": assistant_response})
        st.chat_message("assistant", avatar="🤖").write(assistant_response)
    else:
        st.error("서버 오류")

if st.button("접근"):
    try:
        # 서버의 기본 경로 (/)에 GET 요청 보내기
        response = requests.get("http://13.125.119.225")
        # 서버 응답 텍스트 출력
        if response.status_code == 200:
            st.write("서버 응답:", response.text)
        else:
            st.write("서버에 연결할 수 없습니다.")
    except requests.exceptions.RequestException as e:
        st.write("오류 발생:", e)