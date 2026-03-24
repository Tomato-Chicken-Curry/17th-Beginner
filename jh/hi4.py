import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Today's Vibe", page_icon="✨", layout="centered")

# 세션 상태 초기화 (데이터 저장을 위해)
if 'vibes' not in st.session_state:
    st.session_state.vibes = []

# 타이틀
st.title("✨ Today's Vibe")
st.markdown("오늘의 기분이나 목표를 기록해보세요!")

# 입력 폼
with st.form(key='vibe_form', clear_on_submit=True):
    col1, col2 = st.columns([8, 2])
    with col1:
        new_vibe = st.text_input("Vibe 입력", label_visibility="collapsed", placeholder="여기에 적어보세요...")
    with col2:
        submit_button = st.form_submit_button(label='추가 🚀')

    if submit_button and new_vibe.strip() != "":
        st.session_state.vibes.append({"text": new_vibe, "done": False})
        st.rerun()

st.divider()

# 리스트 출력
for i, vibe in enumerate(st.session_state.vibes):
    col_check, col_text, col_del = st.columns([1, 8, 1])
    
    with col_check:
        # 체크박스로 완료 처리
        is_done = st.checkbox("완료", value=vibe["done"], key=f"check_{i}", label_visibility="collapsed")
        st.session_state.vibes[i]["done"] = is_done
        
    with col_text:
        # 완료되었으면 취소선, 아니면 일반 텍스트
        if is_done:
            st.markdown(f"<span style='text-decoration: line-through; color: gray;'>{vibe['text']}</span>", unsafe_allow_html=True)
        else:
            st.write(vibe['text'])
            
    with col_del:
        # 삭제 버튼
        if st.button("✖", key=f"del_{i}"):
            st.session_state.vibes.pop(i)
            st.rerun()
