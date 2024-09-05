import cv2
import streamlit as st
import random
from io import BytesIO
from PIL import Image
import zipfile
from session_state import get_session_state


session_state = get_session_state()
    

def show():
    st.title("Generation of Markers Page")
    st.write("Generation of Markers Page")
    if st.button('Back to Main Page'):
        st.session_state.page = 'main_page'

    
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    positions = ["Top Left (1st)", "Top Right", "Bottom Right", "Bottom Left (2nd)"]

    # Define default number list as session state to persist changes

    
    # Create number input fields
    st.session_state.number[0] = st.number_input("Top Left (1st)", min_value=0, max_value=200, value=st.session_state.number[0], step=1)
    st.session_state.number[1] = st.number_input("Top Right", min_value=0, max_value=200, value=st.session_state.number[1], step=1)
    st.session_state.number[2] = st.number_input("Bottom Right", min_value=0, max_value=200, value=st.session_state.number[2], step=1)
    st.session_state.number[3] = st.number_input("Bottom Left (2nd)", min_value=0, max_value=200, value=st.session_state.number[3], step=1)

    # Button to randomize numbers
    if st.button("Randomize Numbers"):
        st.session_state.number = [random.randint(0, 200) for _ in range(4)]
        st.experimental_rerun()  # Rerun the app to reflect random values in inputs

    def custom(numbers):
        return cv2.aruco.generateImageMarker(dictionary, numbers, 200)

    if st.button("Generate and Download All Images"):
        img = [custom(num) for num in st.session_state.number]

        # Display images with captions
        col1, col2 = st.columns(2)

        # Top row
        with col1:
            st.image(img[0], caption=f"marker_{st.session_state.number[0]}_Top_Left(1st).png")

        with col2:
            st.image(img[1], caption=f"marker_{st.session_state.number[1]}_Top_Right.png")

        # Bottom row
        with col2:
            st.image(img[2], caption=f"marker_{st.session_state.number[2]}_Bottom_Right.png")

        with col1:
            st.image(img[3], caption=f"marker_{st.session_state.number[3]}_Bottom_Left(2nd).png")

        # Create a ZIP file
        with BytesIO() as zip_buffer:
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for i, image in enumerate(img):
                    img_pil = Image.fromarray(image)
                    img_bytes = BytesIO()
                    img_pil.save(img_bytes, format="PNG")
                    zip_file.writestr(f"marker_{st.session_state.number[i]}_{positions[i].replace(' ', '_').replace('(', '').replace(')', '')}.png", img_bytes.getvalue())

            zip_buffer.seek(0)

            # Provide a download button for the ZIP file
            st.download_button(
                label="Download All Images as ZIP",
                data=zip_buffer,
                file_name="all_images.zip",
                mime="application/zip"
            )




        st.write("Download the image and stick it on any plane surface with following the image orientation and the position of the AruCo markers.")


    # another_page.py


    
