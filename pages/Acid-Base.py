import streamlit as st
import math

st.header('Acid-Base Calculator')

st.write('Select your desired calculation:')

# Session state keys for first and second layer of buttons
if 'b1' not in st.session_state:
    st.session_state.b1 = False

if 'b1_1' not in st.session_state:
    st.session_state.b1_1 = False

if 'b1_2' not in st.session_state:
    st.session_state.b1_2 = False

if 'b2' not in st.session_state:
    st.session_state.b2 = False

if 'b2_1' not in st.session_state:
    st.session_state.b2_1 = False

if 'b2_2' not in st.session_state:
    st.session_state.b2_2 = False

if 'b3' not in st.session_state:
    st.session_state.b3 = False

if 'b3_1' not in st.session_state:
    st.session_state.b3_1 = False

if 'b3_2' not in st.session_state:
    st.session_state.b3_2 = False

col1, col2, col3 = st.columns(3)

with col1:
    button_1 = st.button('Acid Calculations')

    if button_1:
        st.session_state.b1 = not st.session_state.b1

    if st.session_state.b1:

        if st.button('Strong Acids'):
            st.session_state.b1_1 = not st.session_state.b1_1

        if st.session_state.b1_1:

            st.write('To calculate the pH of a strong acid in solution,')
            conc = st.number_input('Enter the concentration of the acid in M (mol/L)', key='c1', step=0.000001,
                                    format='%0.8f')
            submitted = st.button('Calculate', key='s1')

            if submitted:

                if conc <= 0:
                    st.error('Error: please input a positive/non-zero concentration value')

                if conc >= 0.000001:
                    pH = round(-1 * math.log(conc, 10), 2)
                    st.success("The pH of the solution will be: " + str(pH))

                if 0 < conc < 0.000001 :
                    concH = (conc + math.sqrt(math.pow(conc, 2) + 4 * math.pow(10, -14))) / 2
                    pH = round(-1 * math.log(concH, 10), 2)
                    st.success("The pH of the solution will be: " + str(pH))

        if st.button('Weak Acids'):
            st.session_state.b1_2 = not st.session_state.b1_2

        if st.session_state.b1_2:

            st.write('To calculate the pH of a weak acid in solution,')

            conc = st.number_input('Enter the concentration of the weak acid in M (mol/L)', key='c2',
                                   step=0.000001, format='%0.6f')
            pKa = st.number_input('Enter the pKa of the weak acid')
            Ka = math.pow(10, -pKa)

            submitted = st.button('Calculate', key='s2')

            if submitted:

                if 0.000001 <= conc:

                    concH = (-Ka + math.sqrt(math.pow(Ka, 2) + 4 * Ka * conc)) / 2
                    pH = round(-math.log(concH, 10), 2)
                    st.success('The pH of the solution will be: ' + str(pH))

                if 0 < conc < 0.000001:
                    st.success('It appears that the systematic treatment of equilibrium method for weak '
                               'acids and bases has yet to be implemented in this calculator. Sorry and '
                               'please keep an eye out for future updates! - Shao')

                if conc <= 0:
                    st.error('Error: please input a positive/non-zero concentration value.')

with col2:
    button_2 = st.button('Base Calculations')

    if button_2:
        st.session_state.b2 = not st.session_state.b2

    if st.session_state.b2:
        if st.button('Strong Bases'):
            st.session_state.b2_1 = not st.session_state.b2_1

        if st.session_state.b2_1:

            st.write('To calculate the pH of a strong base in solution,')
            conc = st.number_input('Enter the concentration of the base in M (mol/L)', key='c3', step=0.000001,
                                   format='%0.8f')
            submitted = st.button('Calculate', key='s3')

            if submitted:

                if conc <= 0:
                    st.error('Error: please input a positive/non-zero concentration value')

                if conc >= 0.000001:
                    pH = round(14 + math.log(conc, 10), 2)
                    st.success("The pH of the solution will be: " + str(pH))

                if 0 < conc < 0.000001:
                    concOH = (conc + math.sqrt(math.pow(conc, 2) + 4 * math.pow(10, -14))) / 2
                    pH = round(14 + math.log(concOH, 10), 2)
                    st.success("The pH of the solution will be: " + str(pH))

        if st.button('Weak Bases'):
            st.session_state.b2_2 = not st.session_state.b2_2

        if st.session_state.b2_2:

            st.write('To calculate the pH of a weak base in solution,')

            conc = st.number_input('Enter the concentration of the weak base in M (mol/L)', key='c4',
                                   step=0.000001, format='%0.6f')
            pKa = st.number_input('Enter the pKa of the weak base')
            pKb = 14 - pKa
            Kb = math.pow(10, -pKb)

            submitted = st.button('Calculate', key='s4')

            if submitted:

                if 0.000001 <= conc:
                    concOH = (-Kb + math.sqrt(math.pow(Kb, 2) + 4 * Kb * conc)) / 2
                    pH = round(14 + math.log(concOH, 10), 2)
                    st.success('The pH of the solution is: ' + str(pH))

                if 0 < conc < 0.000001:
                    st.success('It appears that the systematic treatment of equilibrium method for weak '
                               'acids and bases has yet to be implemented in this calculator. Sorry and '
                               'please keep an eye out for future updates! - Shao')

                if conc <= 0:
                    st.error('Error: please input a positive/non-zero concentration value.')

with col3:
    button_3 = st.button('Titrations')

    if button_3:
        st.session_state.b3 = not st.session_state.b3

    if st.session_state.b3:

        st.write('To Calculate the pH of a titration: ')

        if st.button('Addition of Strong Acid to a Weak Base'):
            st.session_state.b3_1 = not st.session_state.b3_1

        if st.session_state.b3_1:

            prot = st.number_input('Enter the Max Proticity of the Weak Base: ', key='p1',
                                  step=1)

            if st.session_state.p1 == 1:
                pKa1 = st.number_input('Enter pKa 1 of the Weak Base', key='pKa1', format='%0.3f')
                molB = st.number_input('Enter the no. of moles of Weak Base', key='mB1', step=0.000001,
                                       format='%0.6f')
                molA = st.number_input('Enter the no. of moles of Strong Acid added', key='mA1', step=0.000001,
                                       format='%0.6f')
                volF = st.number_input('Enter the final volume (in L) of the mixture', key='v1', format='%0.5f')

                submitted = st.button('Calculate', key='s5')

                if submitted:
                    # moles of base remaining after the addition of strong acid
                    diff = molB - molA

                    if molB <= 0:
                        st.error('Please enter a non-zero base value.')

                    if molA <= 0:
                        st.error('Please enter a non-zero acid value.')

                    if volF <= 0:
                        st.error('Please enter a non-zero final concentration.')

                    if molB > 0 and molA > 0 and volF > 0:

                        # if there are moles of base remaining, use Henderson Hasselbalch Equation
                        if diff > 0:
                            pH = round(pKa1 + math.log(diff / molA, 10), 2)
                            st.success('The pH after the titration is: ' + str(pH))

                        # if there are no moles of acid or base remaining, treat as weak acid problem
                        if diff == 0:
                            Ka1 = math.pow(10, -pKa1)
                            conc = molA / volF
                            concH = (-Ka1 + math.sqrt(math.pow(Ka1, 2) + 4 * Ka1 * conc)) / 2
                            pH = round(-math.log(concH, 10), 2)
                            st.success('The pH after the titration is: ' + str(pH))

                        # if there is excess strong acid, treat as strong acid problem
                        if diff < 0:
                            conc = -1 * diff / volF

                            if conc >= 0.000001:
                                pH = round(-1 * math.log(conc, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                            if conc < 0.000001:
                                concH = (conc + math.sqrt(math.pow(conc, 2) + 4 * math.pow(10, -14))) / 2
                                pH = round(-1 * math.log(concH, 10), 2)
                                st.success("The pH after the titration is: " + str(pH))

            if st.session_state.p1 == 2:
                pKa1 = st.number_input('Enter pKa 1 of the Weak Base', key='pKa1', format='%0.3f')
                pKa2 = st.number_input('Enter pKa 2 of the Weak Base', key='pKa2', format='%0.3f')
                form = st.number_input('Enter which form the Weak Base is in (1 for fully deprotonated and '
                                       '2 for intermediate species).', key='f1', step=1)
                molB = st.number_input('Enter the no. of moles of Weak Base', key='mB1', step=0.000001,
                                       format='%0.6f')
                molA = st.number_input('Enter the no. of moles of Strong Acid added', key='mA1', step=0.000001,
                                       format='%0.6f')
                volF = st.number_input('Enter the final volume (in L) of the mixture', key='v1', format='%0.5f')

                submitted = st.button('Calculate', key='s5')

                if submitted:
                    # moles of base remaining after addition of acid
                    diff = molB - molA

                    if molB <= 0:
                        st.error('Please enter a non-zero base value.')

                    if molA <= 0:
                        st.error('Please enter a non-zero acid value.')

                    if volF <= 0:
                        st.error('Please enter a non-zero final concentration.')

                    if form < 1 or form > 2:
                        st.error('Form must be 1 or 2 only.')

                    if pKa2 < pKa1:
                        st.error('pKa2 must be greater than pKa1.')

                    if molB > 0 and molA > 0 and volF > 0 and 1 <= form <= 2 and pKa2 > pKa1:

                        # if there is base remaining, use HH equation
                        if diff > 0:

                            # if form is fully deprotonated, use pKa2
                            if st.session_state.f1 == 1:
                                pH = round(pKa2 + math.log(diff / molA, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                            # if form is intermediate, use pKa1
                            if st.session_state.f1 == 2:
                                pH = round(pKa1 + math.log(diff / molA, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                        # weak acid or intermediate species calculations
                        if diff == 0:

                            # intermediate species calculation
                            if st.session_state.f1 == 1:
                                pH = round((pKa1 + pKa2) / 2, 2)
                                st.success('The pH after the titration is: ' + str(pH))

                            # weak acid problem
                            if st.session_state.f1 == 2:
                                Ka1 = math.pow(10, -pKa1)
                                conc = molB / volF
                                concH = (-Ka1 + math.sqrt(math.pow(Ka1, 2) + 4 * Ka1 * conc)) / 2
                                pH = round(-math.log(concH, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                        # if more acid than base, either strong acid or next form
                        if diff < 0:

                            # if form is fully deprotonated, next form problem
                            if st.session_state.f1 == 1:

                                # scenario if the acid is enough to skip one form, HH equation with pKa1
                                if -1 * diff < molB:
                                    diff2 = molB + diff
                                    pH = round(pKa1 + math.log(diff2 / (-1 * diff), 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                                # scenario if the acid is enough to second eq. point, weak acid problem
                                if -1 * diff == molB:
                                    Ka1 = math.pow(10, -pKa1)
                                    conc = molB / volF
                                    concH = (-Ka1 + math.sqrt(math.pow(Ka1, 2) + 4 * Ka1 * conc)) / 2
                                    pH = round(-math.log(concH, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                                # scenario if the acid is enough to pass 2 forms, strong acid problem
                                if -1 * diff > molB:
                                    diff2 = molB + diff
                                    conc = -1 * diff2 / volF
                                    pH = round(-math.log(conc, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                            # if form is intermediate, strong acid problem
                            if st.session_state.f1 == 2:
                                conc = -1 * diff / volF

                                if conc >= 0.000001:
                                    pH = round(-1 * math.log(conc, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                                if conc < 0.000001:
                                    concH = (conc + math.sqrt(math.pow(conc, 2) + 4 * math.pow(10, -14))) / 2
                                    pH = round(-1 * math.log(concH, 10), 2)
                                    st.success("The pH after the titration is: " + str(pH))

        if st.button('Addition of Strong Base to a Weak Acid'):
            st.session_state.b3_2 = not st.session_state.b3_2

        if st.session_state.b3_2:

            prot = st.number_input('Enter the Max Proticity of the Weak Acid: ', key='p2',
                                   step=1)

            if st.session_state.p2 == 1:
                pKa1 = st.number_input('Enter pKa 1 of the Weak Acid', key='pKa1_1', format='%0.3f')
                molA = st.number_input('Enter the no. of moles of Weak Acid', key='mA2', step=0.000001,
                                       format='%0.6f')
                molB = st.number_input('Enter the no. of moles of Strong Base added', key='mB2', step=0.000001,
                                       format='%0.6f')
                volF = st.number_input('Enter the final volume (in L) of the mixture', key='v2', format='%0.5f')

                submitted = st.button('Calculate', key='s6')

                if submitted:

                    diff = molA - molB

                    if molB <= 0:
                        st.error('Please enter a non-zero base value.')

                    if molA <= 0:
                        st.error('Please enter a non-zero acid value.')

                    if volF <= 0:
                        st.error('Please enter a non-zero final concentration.')

                    if molB > 0 and molA > 0 and volF > 0:

                        # if there are moles of acid remaining, use Henderson Hasselbalch Equation
                        if diff > 0:
                            pH = round(pKa1 + math.log(molB / diff, 10), 2)
                            st.success('The pH after the titration is: ' + str(pH))

                        # if there are no moles of acid or base remaining, treat as weak base problem
                        if diff == 0:
                            pKb1 = 14 - pKa1
                            Kb1 = math.pow(10, -pKb1)
                            conc = molA / volF
                            concOH = (-Kb1 + math.sqrt(math.pow(Kb1, 2) + 4 * Kb1 * conc)) / 2
                            pH = round(14 + math.log(concOH, 10), 2)
                            st.success('The pH of the solution is: ' + str(pH))

                        # if there is excess strong base, treat as strong base problem
                        if diff < 0:
                            conc = -1 * diff / volF

                            if conc >= 0.000001:
                                pH = round(14 + math.log(conc, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                            if conc < 0.000001:
                                concOH = (conc + math.sqrt(math.pow(conc, 2) + 4 * math.pow(10, -14))) / 2
                                pH = round(14 + math.log(concOH, 10), 2)
                                st.success("The pH after the titration is: " + str(pH))

            if st.session_state.p2 == 2:
                pKa1 = st.number_input('Enter pKa 1 of the Weak Acid', key='pKa1_1', format='%0.3f')
                pKa2 = st.number_input('Enter pKa 2 of the Weak Acid', key='pKa2_1', format='%0.3f')
                form = st.number_input('Enter which form the Weak Acid is in (1 for fully protonated and '
                                       '2 for intermediate species).', key='f2', step=1)
                molA = st.number_input('Enter the no. of moles of Weak Acid added', key='mA2', step=0.000001,
                                       format='%0.6f')
                molB = st.number_input('Enter the no. of moles of Strong Base', key='mB2', step=0.000001,
                                       format='%0.6f')
                volF = st.number_input('Enter the final volume (in L) of the mixture', key='v2', format='%0.5f')

                submitted = st.button('Calculate', key='s6')

                if submitted:
                    # moles of base remaining after addition of acid
                    diff = molA - molB

                    if molB <= 0:
                        st.error('Please enter a non-zero base value.')

                    if molA <= 0:
                        st.error('Please enter a non-zero acid value.')

                    if volF <= 0:
                        st.error('Please enter a non-zero final concentration.')

                    if form < 1 or form > 2:
                        st.error('Form must be 1 or 2 only.')

                    if pKa2 < pKa1:
                        st.error('pKa2 must be greater than pKa1.')

                    if molB > 0 and molA > 0 and volF > 0 and 1 <= form <= 2 and pKa2 > pKa1:

                        # if there is acid remaining, use Henderson Hasselbalch
                        if diff > 0:

                            # if fully protonated form, use pKa1
                            if form == 1:
                                pH = round(pKa1 + math.log(molB / diff, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                            # if intermediate form, use pKa2
                            if form == 2:
                                pH = round(pKa2 + math.log(molB / diff, 10), 2)
                                st.success('The pH after the titration is: ' + str(pH))

                        # if molA == molB, either intermediate or weak base problem
                        if diff == 0:

                            # if fully protonated, intermediate problem
                            if form == 1:
                                pH = round((pKa1 + pKa2) / 2, 2)
                                st.success('The pH after the titration is: ' + str(pH))

                            # if intermediate, becomes weak base problem
                            if form == 2:
                                pKb1 = 14 - pKa2
                                Kb1 = math.pow(10, -pKb1)
                                conc = molA / volF
                                concOH = (-Kb1 + math.sqrt(math.pow(Kb1, 2) + 4 * Kb1 * conc)) / 2
                                pH = round(14 + math.log(concOH, 10), 2)
                                st.success('The pH of the solution is: ' + str(pH))

                        # if there is excess Base, strong base or next form problem
                        if diff < 0:

                            # if form is fully protonated, next form problem
                            if form == 1:

                                # scenario if the base is enough to skip one form, HH equation with pKa2
                                if -1 * diff < molA:
                                    diff2 = molA + diff
                                    pH = round(pKa2 + math.log(-diff / diff2, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                                # if the base is enough to skip to the second eq. point, weak base problem
                                if -1 * diff == molA:
                                    pKb1 = 14 - pKa2
                                    Kb1 = math.pow(10, -pKb1)
                                    conc = molA / volF
                                    concOH = (-Kb1 + math.sqrt(math.pow(Kb1, 2) + 4 * Kb1 * conc)) / 2
                                    pH = round(14 + math.log(concOH, 10), 2)
                                    st.success('The pH of the solution is: ' + str(pH))

                                # if base is enough to skip 2 eq points, strong base problem
                                if -1 * diff > molA:
                                    diff2 = molA + diff
                                    conc = -1 * diff2 / volF
                                    pH = round(14 + math.log(conc, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                            # if form is intermediate, strong base problem
                            if form == 2:

                                conc = -1 * diff / volF

                                if conc >= 0.000001:
                                    pH = round(14 + math.log(conc, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))

                                if conc < 0.000001:
                                    concOH = (conc + math.sqrt(math.pow(conc, 2) + 4 * math.pow(10, -14))) / 2
                                    pH = round(14 + math.log(concOH, 10), 2)
                                    st.success('The pH after the titration is: ' + str(pH))


