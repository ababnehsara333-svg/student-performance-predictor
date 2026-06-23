import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_score_model.pkl")

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #4F46E5;
}
.subtitle {
    font-size: 18px;
    color: #6B7280;
}
.card {
    padding: 24px;
    border-radius: 18px;
    background-color: #F8FAFC;
    border: 1px solid #E5E7EB;
    margin-bottom: 20px;
}
.result-card {
    padding: 28px;
    border-radius: 20px;
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🎓 Project Info")
st.sidebar.info("""
Student Performance Predictor

This app predicts a student's exam score using machine learning.

Built with:
- Python
- Scikit-learn
- Streamlit
""")

st.markdown('<div class="main-title">🎓 Student Performance Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict student exam performance based on study habits, attendance, lifestyle, and support factors.</div>',
    unsafe_allow_html=True
)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📘 Academic", "🌿 Lifestyle", "🏫 Support & Environment"])

with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
        hours = st.number_input("Hours Studied", 0, 50, 10)
        attendance = st.number_input("Attendance (%)", 0, 100, 80)

    with col2:
        previous = st.number_input("Previous Scores", 0, 100, 70)
        tutoring = st.number_input("Tutoring Sessions", 0, 20, 2)

    with col3:
        extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])
        school = st.selectbox("School Type", ["Public", "Private"])

with tab2:
    col1, col2, col3 = st.columns(3)

    with col1:
        sleep = st.number_input("Sleep Hours", 0, 12, 7)
        physical = st.number_input("Physical Activity", 0, 20, 3)

    with col2:
        internet = st.selectbox("Internet Access", ["No", "Yes"])
        learning = st.selectbox("Learning Disabilities", ["No", "Yes"])

    with col3:
        gender = st.selectbox("Gender", ["Female", "Male"])
        motivation = st.selectbox("Motivation Level", ["High", "Medium", "Low"])

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        distance = st.selectbox("Distance from Home", ["Far", "Moderate", "Near"])
        parent_edu = st.selectbox("Parental Education Level", ["College", "High School", "Postgraduate", "Unknown"])

    with col2:
        peer = st.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])
        teacher = st.selectbox("Teacher Quality", ["High", "Medium", "Low"])

    with col3:
        income = st.selectbox("Family Income", ["High", "Medium", "Low"])
        resources = st.selectbox("Access to Resources", ["High", "Medium", "Low"])
        parent_involvement = st.selectbox("Parental Involvement", ["High", "Medium", "Low"])

st.markdown("---")

input_data = pd.DataFrame({
    "Hours_Studied": [hours],
    "Attendance": [attendance],
    "Extracurricular_Activities": [1 if extracurricular == "Yes" else 0],
    "Sleep_Hours": [sleep],
    "Previous_Scores": [previous],
    "Internet_Access": [1 if internet == "Yes" else 0],
    "Tutoring_Sessions": [tutoring],
    "School_Type": [1 if school == "Private" else 0],
    "Physical_Activity": [physical],
    "Learning_Disabilities": [1 if learning == "Yes" else 0],
    "Gender": [1 if gender == "Male" else 0],
    "Distance_from_Home_Moderate": [1 if distance == "Moderate" else 0],
    "Distance_from_Home_Near": [1 if distance == "Near" else 0],
    "Parental_Education_Level_High School": [1 if parent_edu == "High School" else 0],
    "Parental_Education_Level_Postgraduate": [1 if parent_edu == "Postgraduate" else 0],
    "Parental_Education_Level_Unknown": [1 if parent_edu == "Unknown" else 0],
    "Peer_Influence_Neutral": [1 if peer == "Neutral" else 0],
    "Peer_Influence_Positive": [1 if peer == "Positive" else 0],
    "Teacher_Quality_Low": [1 if teacher == "Low" else 0],
    "Teacher_Quality_Medium": [1 if teacher == "Medium" else 0],
    "Family_Income_Low": [1 if income == "Low" else 0],
    "Family_Income_Medium": [1 if income == "Medium" else 0],
    "Motivation_Level_Low": [1 if motivation == "Low" else 0],
    "Motivation_Level_Medium": [1 if motivation == "Medium" else 0],
    "Access_to_Resources_Low": [1 if resources == "Low" else 0],
    "Access_to_Resources_Medium": [1 if resources == "Medium" else 0],
    "Parental_Involvement_Low": [1 if parent_involvement == "Low" else 0],
    "Parental_Involvement_Medium": [1 if parent_involvement == "Medium" else 0],
})

center_col1, center_col2, center_col3 = st.columns([1, 2, 1])

with center_col2:
    if st.button("🔮 Predict Exam Score", use_container_width=True):
        prediction = model.predict(input_data)[0]

        st.markdown(f"""
        <div class="result-card">
            <h2>Predicted Exam Score</h2>
            <h1>{prediction:.2f}</h1>
            <p>Based on the provided student profile</p>
        </div>
        """, unsafe_allow_html=True)

        if prediction >= 85:
            st.success("Excellent predicted performance. The student profile shows strong academic indicators.")
        elif prediction >= 70:
            st.info("Good predicted performance. There is room for improvement in some areas.")
        else:
            st.warning("The predicted score is low. Improving attendance, study hours, and support factors may help.")