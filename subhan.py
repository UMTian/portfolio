import streamlit as st
from PIL import Image

# Load a profile picture (replace with the path you'll provide)
profile_pic = Image.open("WhatsApp Image 2024-10-30 at 16.44.40_d4cefba5.jpg")  # Replace with your actual image path

# Set page title and icon
st.set_page_config(page_title="Muhammad Subhan's Portfolio", page_icon=":wave:")

# Sidebar - Contact Information
with st.sidebar:
    st.title("Contact")
    st.write("📧 Email: your_email@example.com")
    st.write("🌐 LinkedIn: [Muhammad Subhan](https://www.linkedin.com/in/muhammad-subhan-khokhar-2194442b1)")
    st.write("💼 GitHub: [subhaan1223](https://github.com/subhaan1223/Projects)")  # Updated GitHub link
    st.write("🔗 Portfolio: [yourwebsite.com](https://yourwebsite.com)")  # Optional website link

# Header section
st.title("👋 Hi, I'm Muhammad Subhan")
st.subheader("C++ with OOP and DSA | Python | SQL | Data Analysis | Machine Learning")

# Profile picture
st.image(profile_pic, width=150, caption="Muhammad Subhan")

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
st.subheader("📊 Project 1: Sentiment Analysis on Amazon Reviews")
st.write(
    """
    Built a sentiment analysis model using NLTK to classify Amazon product reviews as positive, neutral, or negative.
    This model provides insights into customer feedback, helping businesses enhance customer satisfaction.
    - Tools Used: Python, NLTK, Pandas
    - GitHub: [Link to project](https://github.com/subhaan1223/Projects)
    """
)

# Project 2
st.subheader("🔍 Project 2: Bone Fracture Detection using Deep Learning")
st.write(
    """
    Developed a deep learning model for bone fracture detection using transfer learning.
    This project aims to assist healthcare providers in accurately diagnosing fractures.
    - Tools Used: Python, TensorFlow, OpenCV
    - GitHub: [Link to project](https://github.com/subhaan1223/Projects)
    """
)

# Project 3
st.subheader("🤖 Project 3: Voice-Assisted Chatbot")
st.write(
    """
    Created a multi-language voice-assisted chatbot using Streamlit, pyttsx3, and Google Gemini Pro. 
    The chatbot can accept voice and text inputs, making it highly accessible.
    - Tools Used: Python, Streamlit, Google Gemini Pro
    - GitHub: [Link to project](https://github.com/subhaan1223/Projects)
    """
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
