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

    # Submit button
    if st.button("Submit"):
        if name and roll_number and email and phone:
            # Display the entered details
            st.success("Student details submitted successfully!")
            st.subheader("Entered Details:")
            st.write(f"**Name:** {name}")
            st.write(f"**Roll Number:** {roll_number}")
            st.write(f"**Email:** {email}")
            st.write(f"**Phone:** {phone}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Course:** {course}")
            st.write(f"**Specialization:** {specialization if specialization else 'N/A'}")
            st.write(f"**Hobbies:** {hobbies if hobbies else 'N/A'}")
        else:
            st.error("Please fill in all the required fields.")

# Run the function
if __name__ == "__main__":
    collect_student_details()

