import streamlit as st

st.header('Dilutions Calculator')

st.write('Select your desired calculation: ')

# Initial Volume Button and Calculations

# Session state for the first button, toggle-able boolean
if 'b1' not in st.session_state:
    st.session_state.b1 = False

button_1 = st.button('Initial Volume Needed')

# if first button is pressed, toggles the boolean session state value
if button_1:
    st.session_state.b1 = not st.session_state.b1

# if the session state is toggled, shows number inputs
if st.session_state.b1:

    conc_I = st.number_input('Enter the Initial Concentration', key='cI1')
    conc_F = st.number_input('Enter the Final Concentration', key='cF1')
    vol_F = st.number_input('Enter the Final Volume', key='vF1')

    # Submit button triggers calculation, does not reset session state of first button
    submitted = st.button('Calculate', key='sub1')

    if submitted:

        # error messages, only does calculations if no errors
        if conc_I == 0 or conc_F == 0 or vol_F == 0:
            st.error('Error: please input a non-zero value in the fields.')

        if conc_I < conc_F:
            st.error('Error: this dilution is not possible, '
                     'final concentration cannot be greater than initial concentration.')

        if conc_I != 0 and conc_F != 0 and vol_F != 0 and conc_I > conc_F:
            vol_I = round(vol_F * conc_F / conc_I, 5)
            st.success('The Initial Volume Needed is: ' + str(vol_I))


# Final Concentration Button and Calculations

# Session state for the second button
if 'b2' not in st.session_state:
    st.session_state.b2 = False

button_2 = st.button('Final Concentration')

# Toggles boolean session state when pressed
if button_2:
    st.session_state.b2 = not st.session_state.b2

if st.session_state.b2:

    conc_I = st.number_input('Enter the Initial Concentration')
    vol_I = st.number_input('Enter the Initial Volume')
    vol_F = st.number_input('Enter the Final Volume')

    submitted = st.button('Calculate', key='sub2')

    if submitted:

        if conc_I == 0 or vol_I == 0 or vol_F == 0:
            st.error('Error: please input a non-zero value in the fields.')

        if vol_F < vol_I:
            st.error('Error: final volume cannot be less than initial volume.')

        if conc_I != 0 and vol_I != 0 and vol_F != 0 and vol_F > vol_I:
            conc_F = round(vol_I * conc_I / vol_F, 5)
            st.success('The Final Concentration is: ' + str(conc_F))





