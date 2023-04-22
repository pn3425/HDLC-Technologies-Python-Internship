import streamlit as st

st.title("BMI CALCULATOR")
name = st.text_input("Enter Name ")
gen = st.radio("Select Gender  ",('Male','Female'))
if(gen == 'Male'):
    st.success("Male")
else:
    st.success("Female")

age = st.number_input("Enter Age")
add = st.text_input("Enter Address")

st.text("Select Hobbies")
if st.checkbox('Painting'):
    st.text('')
if st.checkbox('Coding'):
    st.text('')
if st.checkbox('Table Tennis'):
    st.text('')
if st.checkbox('Cooking'):
    st.text('')
if st.checkbox('Others'):
    st.text('For other Hobbies type below')
    st.text_input('')

weight = st.number_input("Enter Weight in Kg")
height = st.number_input("Enter Height in cms")
conv = float(height / 100)
bmi = float(weight / (conv ** 2))



if(st.button('Click here to Calculate BMI')):

    st.text('Your BMI is {}'.format(bmi))
    if (bmi < 18.5):
        st.error(" Underweight")
        link ='https://familydoctor.org/healthy-ways-to-gain-weight-if-youre-underweight/'
        st.markdown(link, unsafe_allow_html=True)


    elif (bmi >= 18.5 and bmi < 24.9):
        st.success("Healthy")


    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")


    elif (bmi >= 30):
        st.error("Obese")
        st.write("Obesity preventive measures")
        link = 'https://www.verywellhealth.com/obesity-prevention-4014175'
        st.markdown(link, unsafe_allow_html=True)






















