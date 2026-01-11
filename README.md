📊 Student Performance Analysis Using Python

📌 Project Overview

This project analyzes student academic performance using Python by converting grades into numerical values, calculating SGPA, and identifying pass or re-appear cases. The analysis focuses on core subjects and uses data visualization to highlight performance trends and insights.

🎯 Objectives

Analyze student performance using structured academic data

Calculate SGPA based on subject-wise grading

Identify pass and re-appear students

Visualize academic trends and results

📂 Dataset Description

The project uses two datasets:

Raw Data: Original student result records

Processed Data: Cleaned and structured dataset with calculated SGPA and result status

📚 Subjects Considered

Maths

English

MMP

Chemistry

🎓 Grading System
Grade	Points
O	10
A+	9
A	8
B+	7
B	6
C	5
P	4
F	0

Result Logic:
If any subject has grade F, the student is marked as Re-Appear.

⚙️ Technologies Used

Python

Pandas

Matplotlib

OpenPyXL

📊 Analysis Performed

Data cleaning and preprocessing

SGPA calculation

Pass and Re-Appear classification

Performance trend analysis

📈 Visualizations

The following visualizations were generated:

Average SGPA (Bar Chart)

Student Performance Trend (Line Chart)

Pass vs Re-Appear Distribution (Pie Chart)

📁 Figures are available in the Figures/ folder.

▶️ How to Run the Project

Clone the repository

Install dependencies:

pip install -r requirements.txt


Run the analysis:

python analysis.py

🧠 Key Insights

The average SGPA indicates overall good academic performance

Students with at least one failing subject are correctly classified as Re-Appear

Visual trends help in understanding performance distribution

🔮 Future Enhancements

Subject-wise average analysis

SGPA distribution histogram

Interactive dashboard using Streamlit

🏁 Conclusion

This project demonstrates a complete data analysis workflow, from raw academic data processing to insight generation using Python. It highlights the practical application of data analysis and visualization techniques in an educational context.
