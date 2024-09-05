import streamlit as st
import zipfile
import os

# Folder containing files to download
def download_imgs():
    folder_path = "testing_images"

    # Zip the folder
    zip_file = "testing_images.zip"
    with zipfile.ZipFile(zip_file, "w") as z:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                z.write(os.path.join(root, file), arcname=file)

    # Download button for the zipped folder
    with open(zip_file, "rb") as file:
        btn = st.download_button(
            label="Download Testing Files",
            data=file,
            file_name="testing_img.zip",
            mime="application/zip"
        )
