import streamlit as st
from changing_marker_values import initial_marker_values
from testing101 import generate_image1
from dowload_test_images import download_imgs
from session_state import get_session_state


session_state = get_session_state()
    
def main():
    st.title(" Augmented Reality using ArUco Markers")
    st.write("ArUco markers are binary square fiducial markers used in computer vision for object detection, camera calibration, and pose estimation")
    st.write("Go to ArUco marker generation page and generate the markers. ")
    if st.button('Go to Aruco marker generation page'):
        st.session_state.page = 'another_page'
    initial_marker_values()
    
    st.write("for testing purpose you can download the images from the below link")
    download_imgs()
        
    #taking in the files    
    aruco_file = st.file_uploader("Choose a ArUco marker file", type=['png', 'jpg','jpeg'], )
    uploaded_file = st.file_uploader("Replacement image", type=['png', 'jpg','jpeg'], )

    result = st.button("generate image")
    
    if result:
        generate_image1(aruco_file,uploaded_file)
        



if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

if st.session_state.page == 'main_page':
    main()
elif st.session_state.page == 'another_page':
    import another_page
    another_page.show()
    
    
    
    
