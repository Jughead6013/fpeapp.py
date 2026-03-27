import os
from datetime import date
import datetime
import streamlit as st


st.set_page_config(page_title="FPE MEMBER", layout="wide")

st.title("FPE FORMS", text_alignment="center")

with st.container():
    st.subheader("Personal Information")
    with st.form("fpe_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            lastname = st.text_input(
                "Lastname",
            )
        with col2:
            firstname = st.text_input("Firstname")
        with col3:
            middlename = st.text_input("Middlename")
        with col4:
            suffix = st.text_input("Suffix")

        (
            col8,
            col9,
            col10,
            col11,
        ) = st.columns(4)
        with col8:
            dob = st.date_input(
                "Date of Birth", min_value=date(1930, 1, 1), max_value=date.today()
            )
        with col9:
            birthplace = st.text_input("Birthplace")
        with col10:
            civilstatus = st.selectbox(
                label="Civil Status",
                options=[
                    "Annulled",
                    "Co-Habitation",
                    "Married",
                    "Separated",
                    "Single",
                    "Widower",
                ],
            )
        with col11:
            maidenname = st.text_input("Maidenname")
        (
            col5,
            col6,
            col7,
            col12,
        ) = st.columns(4)
        with col5:
            sex = st.radio("Gender", ["Male", "Female"])
        with col6:
            alcohol = st.radio("Alcohol Intake", ["YES", "NO"])
        with col7:
            cigarettes = st.radio("Use Cigarettes", ["YES", "NO"])
        with col12:
            employmentstatus = st.radio(
                "Employment Status",
                ["Employed", "Unemployed", "Retire", "Student", "Unknown"],
            )
        (col13, col14, col15, col16) = st.columns(4)
        with col13:
            bloodtype = st.radio(
                "bloodtype",
                ["A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"],
            )
        with col14:
            familymember = st.text_input("Family Member")
        with col15:
            fourpsmember = st.text_input("4ps member")
        with col16:
            pwd = st.text_input("PWD")

        (col18, col19, col20, col21) = st.columns(4)
        with col18:
            philhealthnumber = st.text_input("Philhealth Number")
        with col19:
            yakapregistered = st.selectbox(
                label="YAKAP Registered?",
                options=["yes", "no"],
            )
        with col20:
            natureofvisit = st.selectbox(
                label="Nature of Visit",
                options=["New Consultation", "Follow up Visit"],
            )
        with col21:
            age = st.number_input("Age", min_value=0, max_value=120, step=1)

        with st.container():
            st.subheader("Vital Signs")
        (
            col22,
            col23,
        ) = st.columns(2)
        with col22:
            height = st.number_input(
                "Height (cm)", min_value=30.0, max_value=250.0, step=0.1
            )
        with col23:
            weight = st.number_input(
                "Weight (kg)", min_value=1.0, max_value=300.0, step=0.1
            )
        (
            col24,
            col25,
            col26,
        ) = st.columns(3)
        with col24:
            systolic = st.number_input(
                "Systolic (mmHg)", min_value=50, max_value=250, step=1
            )
        with col25:
            diastolic = st.number_input(
                "Diastolic (mmHg)", min_value=30, max_value=150, step=1
            )
        with col26:
            respiratory_rate = st.number_input(
                "RR (bpm)", min_value=5, max_value=60, step=1
            )
        medicalhistory = st.multiselect(
            "Medical History",
            [
                "Allergy",
                "Pneumonia",
                "Asthma",
                "UTI",
                "TB",
                "Cancer",
                "Diabetes Melitus",
                "Hyperlipidemia",
                "Epilepsy/Seizure Disorder",
                "Cerebrovasscular Disease",
                "Hepatits",
                "Mental Illness",
                "Pectic Ulcer",
                "Thyroid Disease",
                "Pulomnary Tuberculosis",
                "Others",
                "Extrapulmonary Tuberculosis",
                "Coronary Artery Disease",
                "Hepatits",
                "Emphysema",
            ],
        )
        Remarks = st.text_area("REMARKS")
        Surgical_Operation = st.text_area("Description of Surgical Operation:")
        submitted = st.form_submit_button("Submit")
        if submitted:
            folder_path = "saved_forms"
            os.makedirs(folder_path, exist_ok=True)
            now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join("folder_path", f"{lastname}_{firstname}_{now}.txt")
            with open("file_path", "w") as f:
                f.write(f"lastname: {lastname}\n")
                f.write(f"firstname: {firstname}\n")
                f.write(f"middlename: {middlename}\n")
                f.write(f"suffix: {suffix}\n")
                f.write(f"dateofbirth: {dob}\n")
                f.write(f"birthplace: {birthplace}\n")
                f.write(f"civilstatus: {civilstatus}\n")
                f.write(f"maidenname: {maidenname}\n")
                f.write(f"Gender: {sex}\n")
                f.write(f"Alcohol Intake: {alcohol}\n")
                f.write(f"cigarettes: {cigarettes}\n")
                f.write(f"Employment Status: {employmentstatus}\n")
                f.write(f"bloodtype: {bloodtype}\n")
                f.write(f"Family Member: {familymember}\n")
                f.write(f"4ps member: {fourpsmember}\n")
                f.write(f"PWD: {pwd}\n")
                f.write(f"YAKAP Registered: {philhealthnumber}\n")
                f.write(f"Nature of Visit: {natureofvisit}\n")
                f.write(f"Age: {age}\n")
                f.write(f"Height: {height}\n")
                f.write(f"Weight: {weight}\n")
                f.write(f"systolic: {systolic}\n")
                f.write(f"RR: {respiratory_rate}\n")
                f.write(f"Medical History: {medicalhistory}\n")
                f.write(f"Remarks: {Remarks}\n")
                f.write(f"Description of Surgical Operation: {Surgical_Operation}\n")
                folder_path = "./saved_forms"
            if not os.path.exists("tempDir"):
                os.makedirs("tempDir")
                st.success(f"Form saved to {file_path}")
            st.rerun()
