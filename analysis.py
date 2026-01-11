import pandas as pd
import matplotlib.pyplot as plt

#Load Processed Data
df = pd.read_excel("data/processed/student_performance_dataset.xlsx")

#Basis statistics
average_sgpa = df["SGPA"].mean()
highest_sgpa = df["SGPA"].max()
lowest_sgpa = df["SGPA"].min()

#Print Statistical Data 
print("Average SGPA: ", round(average_sgpa, 2))
print("Highest SGPA: ", highest_sgpa)
print("Lowest SGPA: ", lowest_sgpa)

#Bar Chart
plt.figure()
plt.bar(["Average SGPA"], [average_sgpa])
plt.title("Average Student SGPA")
plt.ylabel("SGPA")
plt.show()

#Line Chart
plt.figure()
plt.plot(df["Roll No"], df["SGPA"])
plt.title("Student Performance Trend")
plt.xlabel("Roll Number")
plt.ylabel("SGPA")
plt.show()

#Pie Chart
plt.figure()
df["Result"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Re-Appear")
plt.ylabel("")
plt.show()
