
import streamlit as st
from PIL import Image

# Load a profile picture (replace with the path you'll provide)
profile_pic = Image.open("subhanpic.jpg")  # Replace with your actual image path

# Set page title and icon
st.set_page_config(page_title="Muhammad Subhan's Portfolio", page_icon=":wave:")

# Inject custom CSS for background color and styling
st.markdown(
    """
    <style>
    /* Set body background color */
    .stApp {
        background-color: #1a1a2e;  /* Dark blue background color */
        color: #ffffff;  /* White text color for contrast */
    }
    /* Sidebar styles */
    [data-testid="stSidebarContent"] {
        background-color: #c6aef9;  /* Updated light blue background for the sidebar */
    }
    /* Change text color for specific sidebar elements */
    .stSidebar p {
        color: #000000;  /* Black color for paragraph text */
    }
    /* Header and subheader styles */
    h1, h2, h3, h4 {
        color: #00adb5;  /* Bright cyan color for headers */
    }
    /* Buttons */
    .stButton button {
        background-color: #00adb5;  /* Cyan color for buttons */
        color: #ffffff;  /* White text color for buttons */
    }
    /* Links */
    a {
        color: #00adb5;  /* Cyan links */
    }
    /* Input fields */
    input, textarea {
        color: #000000;  /* Black text for input fields */
        background-color: #ffffff;  /* White background for input fields */
        border: 1px solid #00adb5;  /* Add a border */
        padding: 5px;  /* Add some padding */
        margin-bottom: 10px;  /* Add some margin */
    }
    /* Form submit button */
    .stFormSubmitButton {
        background-color: #00adb5;  /* Cyan color for buttons */
        color: #ffffff;  /* White text color for buttons */
        border: 1px solid #00adb5;  /* Add a border */
        padding: 5px 10px;  /* Add some padding */
    }
    /* Form container */
    .stForm {
        color: #ffffff;  /* White text color for form elements */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar - Contact Information
with st.sidebar:
    st.title("Contact")
    st.write("📧 Email: your_email@example.com")
    st.write("🌐 LinkedIn: [Muhammad Subhan](https://www.linkedin.com/in/muhammad-subhan-khokhar-2194442b1)")
    st.write("💼 GitHub: [subhaan1223](https://github.com/subhaan1223/Projects)")  # Updated GitHub link

# Header section
st.title("👋 Hi, I'm Muhammad Subhan")
st.subheader("C++ with OOP and DSA | Python | SQL | Data Analysis | Machine Learning")

# Profile picture
st.image(profile_pic, width=150)

# About Me section
st.header("About Me")
st.write(
    """
    I'm a dedicated developer with expertise in C++, Python, SQL, Data Analysis, and Machine Learning.
    I’m passionate about solving complex problems through technology and data-driven insights.
    With a strong foundation in data structures, algorithms, and object-oriented programming, 
    I strive to create impactful solutions.
    """
)

# Skills section
st.header("Skills")
skills = ["C++ with OOP and DSA", "Python", "SQL", "Data Analysis", "Machine Learning"]
for skill in skills:
    st.write(f"- {skill}")

# Projects section
st.header("Projects")

# Project 1
st.subheader("📊 Project 1: Student Management System")
st.markdown(
    """
    This C++ project is a simple Student Management System designed to handle essential student records efficiently. 
    It allows users to add, view, search, update, and delete student data, including fields for each student’s name, 
    roll number, department, and course. Key features include:

    - *Data Entry*: Users can input details for multiple students.
    - *Display Records*: Provides a quick view of all stored student records.
    - *Search Function*: Enables searching by roll number.
    - *Update Function*: Allows modifying details of existing records.
    - *Delete Function*: Supports deletion of specific student records.

    - *Tools Used*: C++
    - [GitHub Link to project](https://github.com/subhaan1223/Projects/blob/main/Student%20Management%20System%20c%2B%2B)
    """, unsafe_allow_html=True
)

# Project 2
st.subheader("🔍 Project 2: Student Management System DSA")
st.markdown(
    """
    This project is a C++-based Student Management System that employs both a linked list and an array for efficient data handling.

    Key Features:

    - *Dual Data Storage*: Uses a linked list and an array for data management.
    - *Add New Students*: Allows input of essential student information.
    - *Display Records*: Displays all student records in a structured format.
    - *Search by Roll Number*: Facilitates efficient searching.
    - *Update Records*: Modifies existing records.
    - *Delete Records*: Supports removal of individual records.

    - *Tools Used*: C++ and DSA
    - [GitHub Link to project](https://github.com/subhaan1223/Projects/blob/main/Student%20Management%20System%20(DSA))
    """, unsafe_allow_html=True
)

# Project 3
st.subheader("🤖 Project 3: House Price Prediction System")
st.markdown(
    """
    This project is a house price prediction model created in Python using Jupyter Notebook and Google Colab.

    Key Steps:

    - *Data Loading*: Loaded training and test datasets from Google Drive.
    - *Exploratory Data Analysis (EDA)*: Visualized missing values.
    - *Data Cleaning*: Imputed missing values and combined datasets for consistency.
    - *Feature Engineering*: One-hot encoding for categorical variables.
    - *Model Training*: Trained the XGBoost model with hyperparameter tuning.
    - *Evaluation*: Calculated RMSE on the validation set.
    - *Submission*: Generated a submission file for predictions.

    - *Tools and Technologies*: Python Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, XGBoost
    - [GitHub Link to project](https://github.com/subhaan1223/Projects/blob/main/House%20Price%20Prediction%20System)
    """, unsafe_allow_html=True
)

# Contact Form (using a Streamlit form for user input)
st.header("Get in Touch")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        st.success("Thank you for your message! I'll get back to you soon.")

# Footer section
st.write("Made with ❤️ in Streamlit")
