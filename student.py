import streamlit as st

def collect_student_details():
    st.title("Student Details Form")

    # Input fields for student details
    name = st.text_input("Full Name")
    roll_number = st.text_input("Roll Number")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    gender = st.radio("Gender", ("Male", "Female", "Other"))
    course = st.selectbox("Course", ["B.Tech", "B.Sc", "B.Com", "MBA", "MCA", "Other"])
    specialization = st.text_input("Specialization (if any)")
    hobbies = st.text_area("Hobbies")

    

# Run the function
if __name__ == "__main__":
    collect_student_details()

