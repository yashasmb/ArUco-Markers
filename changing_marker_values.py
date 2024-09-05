import streamlit as st

# Initialize default values in session_state

# Checkbox for default setting.
def initial_marker_values():
    default_checked = st.checkbox('Use Default Values', value=True)

    # Display 4 input boxes
    if default_checked:
        st.session_state.number = st.session_state.default_number
        # If checkbox is checked, show default values
        st.write("Default values:")
        col1, col2 = st.columns(2)
        with col1:
            val1 = st.number_input("Top Left", value=st.session_state.number[0], disabled=True)
        with col2:
            val2 = st.number_input("Top Right", value=st.session_state.number[1], disabled=True)
        with col2:
            val3 = st.number_input("Bottom Right", value=st.session_state.number[2], disabled=True)
        with col1:
            val4 = st.number_input("Bottom Left", value=st.session_state.number[3], disabled=True)
    else:
        # If unchecked, allow user to modify the values within range 0-200
        st.write("Modify values:")
        col1, col2 = st.columns(2)
        with col1:
            val1 = st.number_input("Top Left", value=st.session_state.number[0], min_value=0, max_value=200)
        with col2:    
            val2 = st.number_input("Top Right", value=st.session_state.number[1], min_value=0, max_value=200)
        with col2:    
            val3 = st.number_input("Bottom Right", value=st.session_state.number[2], min_value=0, max_value=200)
        with col1:    
            val4 = st.number_input("Bottom Left", value=st.session_state.number[3], min_value=0, max_value=200)

    # Update session state with new values when the checkbox is unchecked
    if not default_checked:
        st.session_state.number = [val1, val2, val3, val4]


