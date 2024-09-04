# import streamlit as st
# import pandas as pd
# import numpy as np
import cv2
import streamlit as st
# import numpy as np
# import pandas as pd
# import streamlit as st
# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name

# import streamlit as st
# import pandas as pd

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option



# import streamlit as st

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )



# import streamlit as st

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
    
    
    
    
# import streamlit as st
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

st.title("ArUcoMarkers")

aruco_file = st.file_uploader("Choose a ArUco marker file", type=['png', 'jpg','jpeg'], )

# (label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")


uploaded_file = st.file_uploader("Replacement image", type=['png', 'jpg','jpeg'], )

# st.image(aruco_file, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


frame_dst = cv2.imread(aruco_file)

# Detect the markers in the destination image.
corners, ids, rejected = cv2.aruco.detectMarkers(frame_dst, dictionary)

frame_detetced = frame_dst.copy()