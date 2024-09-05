import streamlit as st
import cv2
import numpy as np
from session_state import get_session_state
session_state = get_session_state()
def generate_image1 (img1 ,img2, scaling_x=.015,scaling_y=.025):
    
    file_bytes = np.frombuffer(img1.read(), np.uint8)
    
    # Decode the image bytes to an OpenCV image
    frame_dst = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Display the image using Streamlit
   
    # frame_dst = cv2.imread(img1)
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    corners, ids, rejected = cv2.aruco.detectMarkers(frame_dst, dictionary)
    frame_detetced = frame_dst.copy()
    cv2.aruco.drawDetectedMarkers(frame_detetced, corners, ids)
    st.image(frame_detetced, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    
    
    
    index = np.squeeze(np.where(ids == session_state.number[0]))
    ref_pt1 = np.squeeze(corners[index[0]])[0]

    # Upper-right corner of ROI.
    index = np.squeeze(np.where(ids == session_state.number[1]))
    ref_pt2 = np.squeeze(corners[index[0]])[1]

    # Lower-right corner of ROI.
    index = np.squeeze(np.where(ids == session_state.number[2]))
    ref_pt3 = np.squeeze(corners[index[0]])[2]

    # Lower-left corner of ROI.
    index = np.squeeze(np.where(ids == session_state.number[3]))
    ref_pt4 = np.squeeze(corners[index[0]])[3]
    
    
    
    x_distance = np.linalg.norm(ref_pt1 - ref_pt2)
    y_distance = np.linalg.norm(ref_pt1 - ref_pt3)

    scaling_fac_x = scaling_x  # Scale factor in x (horizontal).
    scaling_fac_y = scaling_y # Scale factor in y (vertical).

    delta_x = round(scaling_fac_x * x_distance)
    delta_y = round(scaling_fac_y * y_distance)

    # Apply the scaling factors to the ArUco Marker reference points to make.
    # the final adjustment for the destination points.
    pts_dst = [[ref_pt1[0] - delta_x, ref_pt1[1] - delta_y]]
    pts_dst = pts_dst + [[ref_pt2[0] + delta_x, ref_pt2[1] - delta_y]]
    pts_dst = pts_dst + [[ref_pt3[0] + delta_x, ref_pt3[1] + delta_y]]
    pts_dst = pts_dst + [[ref_pt4[0] - delta_x, ref_pt4[1] + delta_y]]
    
    
    file_bytes = np.frombuffer(img2.read(), np.uint8)
    
    # Decode the image bytes to an OpenCV image
    frame_src = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Display the image using Streamlit
    
    

    # Get the image corners of the source image.
    pts_src = [[0,0], [frame_src.shape[1], 0], [frame_src.shape[1], frame_src.shape[0]], [0, frame_src.shape[0]]]
            
    pts_src_m = np.asarray(pts_src)
    pts_dst_m = np.asarray(pts_dst)
    
    
    h, mask = cv2.findHomography(pts_src_m, pts_dst_m, cv2.RANSAC)

# Warp source image onto the destination image.
    warped_image = cv2.warpPerspective(frame_src, h, (frame_dst.shape[1], frame_dst.shape[0]))

    warped_image_copy = warped_image.copy() # Save for display below.

    # Prepare a mask representing the region to copy from the warped image into the destination frame.
    mask = np.zeros([frame_dst.shape[0], frame_dst.shape[1]], dtype=np.uint8)

    # Fill ROI in destination frame with white to create mask.
    cv2.fillConvexPoly(mask, np.int32([pts_dst_m]), (255, 255, 255), cv2.LINE_AA)

    # Copy the mask into 3 channels.
    warped_image = warped_image.astype(float)
    mask3 = np.zeros_like(warped_image)
    for i in range(0, 3):
        mask3[:, :, i] = mask / 255

    # Create inverse mask.
    mask3_inv = 1 - mask3

    # Create black region in destination frame ROI.
    frame_masked = cv2.multiply(frame_dst.astype(float), mask3_inv)

    # Create final result by adding the warped image with the masked destination frame.
    frame_out = cv2.add(warped_image, frame_masked)

    frame_masked = np.uint8(frame_masked)  # For display below.
    frame_out = frame_out.astype(np.uint8) # For display below.
    
    
    st.image(frame_out, caption=None, width=None, use_column_width=None, clamp=False, channels="BGR", output_format="auto")
    