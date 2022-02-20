import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('/Model/ML_Model.pkl', 'rb'))


def run():
    img1 = Image.open('/Media/bank.png')
    img1 = img1.resize((156, 145))
    st.image(img1, use_column_width=False)
    st.title('Bank Loan Grant Prediction')

    account_no = st.text_input('Account Number')

    fn = st.text_input('Full Name')

    gen_display = ('Select', 'Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox('Gender', gen_options, format_func=lambda x: gen_display[x])

    mar_display = ('Select', 'No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox('Married?', mar_options, format_func=lambda x: mar_display[x])

    dep_display = ('Select', 'None', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox('Dependents', dep_options, format_func=lambda x: dep_display[x])

    edu_display = ('Select', 'Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox('Education', edu_options, format_func=lambda x: edu_display[x])

    emp_display = ('Select', 'Job', 'Self Employed')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox('Employement Status', emp_options, format_func=lambda x: emp_display[x])

    prop_display = ('Select', 'Rural', 'Semiurban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox('Property Area', prop_options, format_func=lambda x: prop_display[x])

    cred_display = ('Select', 'Between 300-500', 'Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox('Credit Display', cred_options, format_func=lambda x: cred_display[x])

    mon_income = st.number_input("Applicant's Monthly Income ($)", value=0)

    co_mon_income = st.number_input("Co-Applicant's Monthly Income ($)", value=0)

    loan_amt = st.number_input("Loan Amount", value=0)

    dur_display = ('Select', '2 Month', '6 Month', '8 Month', '12 Month', '16 Month')
    dur_options = list(range(len(dur_display)))
    dur = st.selectbox('Loan Duration', dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        elif dur == 1:
            duration = 180
        elif dur == 2:
            duration = 240
        elif dur == 3:
            duration = 360
        elif dur == 4:
            duration = 480

        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)

        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))

        if ans == 0:
            st.error(
                'Hello: ' + fn + " || "
                'According to our Calculations, you will not get the loan from the Bank'
            )
        else:
            st.success(
                'Hello: ' + fn + " || "
                'Account Number: ' + account_no + ' || '
                'Congratulations you will get the loan from the bank!'
            )


run()
