import cv2
import numpy as np

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

default_markers= [23,25, 30, 30]
def custom(number):
    return cv2.aruco.generateImageMarker(dictionary, number, 200)



def return_img(frame_dst):
    frame_dst=frame_dst
    # frame_dst = cv2.imread('images\IMG_20240904_092026.jpg')

    # Detect the markers in the destination image.
    corners, ids, rejected = cv2.aruco.detectMarkers(frame_dst, dictionary)

    frame_detetced = frame_dst.copy()

    cv2.aruco.drawDetectedMarkers(frame_detetced, corners, ids)
    return frame_detetced



# Extract reference point coordinates from marker corners.


def corner_roi(id, corner):

    # Upper-left corner of ROI.
    index = np.squeeze(np.where(ids == id[0]))
    ref_pt1 = np.squeeze(corners[index[0]])[0]

    # Upper-right corner of ROI.
    index = np.squeeze(np.where(ids == id[1]))
    ref_pt2 = np.squeeze(corners[index[0]])[1]

    # Lower-right corner of ROI.
    index = np.squeeze(np.where(ids == id[2]))
    ref_pt3 = np.squeeze(corners[index[0]])[2]

    # Lower-left corner of ROI.
    index = np.squeeze(np.where(ids == id[3]))
    ref_pt4 = np.squeeze(corners[index[0]])[3]



# Compute horizontal and vertical distance between markers.
    x_distance = np.linalg.norm(ref_pt1 - ref_pt2)
    y_distance = np.linalg.norm(ref_pt1 - ref_pt3)

    scaling_fac_x = .015  # Scale factor in x (horizontal).
    scaling_fac_y = .025 # Scale factor in y (vertical).

    delta_x = round(scaling_fac_x * x_distance)
    delta_y = round(scaling_fac_y * y_distance)

# Apply the scaling factors to the ArUco Marker reference points to make.
# the final adjustment for the destination points.
    pts_dst = [[ref_pt1[0] - delta_x, ref_pt1[1] - delta_y]]
    pts_dst = pts_dst + [[ref_pt2[0] + delta_x, ref_pt2[1] - delta_y]]
    pts_dst = pts_dst + [[ref_pt3[0] + delta_x, ref_pt3[1] + delta_y]]
    pts_dst = pts_dst + [[ref_pt4[0] - delta_x, ref_pt4[1] + delta_y]]



# Read input image with the markers.
def replacement_image(frame_src):
# Get the image corners of the source image.
    pts_src = [[0,0], [frame_src.shape[1], 0], [frame_src.shape[1], frame_src.shape[0]], [0, frame_src.shape[0]]]
        
# pts_src_m = np.asarray(pts_src)
# pts_dst_m = np.asarray(pts_dst)





import streamlit as st
if "number" not in st.session_state:
    st.session_state.number = [23, 25, 30, 33]
def main():
    st.title("Main Page")
    st.write("Welcome to the main page.")
    if st.button('Go to Another Page'):
        st.session_state.page = 'another_page'

if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

if st.session_state.page == 'main_page':
    main()
elif st.session_state.page == 'another_page':
    import another_page
    another_page.show()