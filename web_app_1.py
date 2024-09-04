import streamlit as st
if "number" not in st.session_state:
    st.session_state.number = [23, 25, 30, 33]
def main():
    st.title("Main Page")
    st.write("Welcome to the main page.")
    if st.button('Go to Aruco marker generation page'):
        st.session_state.page = 'another_page'
        
        
        
    aruco_file = st.file_uploader("Choose a ArUco marker file", type=['png', 'jpg','jpeg'], )
    uploaded_file = st.file_uploader("Replacement image", type=['png', 'jpg','jpeg'], )

if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

if st.session_state.page == 'main_page':
    main()
elif st.session_state.page == 'another_page':
    import another_page
    another_page.show()
    
    
    
    
