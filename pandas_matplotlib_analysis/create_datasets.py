# Simple Dataset schema.
# Run this first to create your CSV file

import pandas as pd
import numpy as np

print(" Creating Simple Student Dataset...")
print("=" * 40)

# Set random seed for consistent results
np.random.seed(42)

# Create simple student data
students = []
majors = ["Engineering", "Business", "Arts", "Science", "Medicine"]
genders = ["Male", "Female"]
years = [2021, 2022, 2023, 2024]

# Generate 150 students
for i in range(1, 151):
    # Basic info
    student_id = i
    name = f"Student_{i:03d}"
    age = np.random.randint(18, 25)
    gender = np.random.choice(genders)
    major = np.random.choice(majors)
    year = np.random.choice(years)

    # Academic info
    study_hours = np.random.randint(5, 40)
    activities = np.random.randint(0, 5)
    has_job = np.random.choice(["Yes", "No"])

    # Generate realistic GPA based on study hours
    if study_hours >= 30:
        gpa = np.random.uniform(3.5, 4.0)
    elif study_hours >= 20:
        gpa = np.random.uniform(3.0, 3.7)
    elif study_hours >= 10:
        gpa = np.random.uniform(2.5, 3.2)
    else:
        gpa = np.random.uniform(2.0, 2.8)

    gpa = round(gpa, 2)

    # Generate final grade based on GPA
    final_grade = int(60 + (gpa - 2.0) * 20 + np.random.randint(-5, 10))
    final_grade = max(60, min(100, final_grade))  # Keep between 60-100

    # Add student to list
    students.append(
        {
            "student_id": student_id,
            "name": name,
            "age": age,
            "gender": gender,
            "major": major,
            "year": year,
            "gpa": gpa,
            "study_hours_per_week": study_hours,
            "extracurricular_activities": activities,
            "part_time_job": has_job,
            "final_grade": final_grade,
        }
    )

# Create DataFrame
df = pd.DataFrame(students)

# Save to CSV
filename = "student_dataset.csv"
df.to_csv(filename, index=False)

print(f" Dataset created successfully!")
print(f" Saved as: {filename}")
print(f" {len(df)} students with {len(df.columns)} features")

# Show preview
print("\n First 5 students:")
print("-" * 30)
print(df.head())

print(f"\n Quick Stats:")
print("-" * 20)
print(f"Age range: {df['age'].min()}-{df['age'].max()} years")
print(f"GPA range: {df['gpa'].min()}-{df['gpa'].max()}")
print(
    f"Study hours: {df['study_hours_per_week'].min()}-{df['study_hours_per_week'].max()} hrs/week"
)

print(f"\n Majors:")
for major, count in df["major"].value_counts().items():
    print(f"  {major}: {count} students")

print(f"\n Gender split:")
for gender, count in df["gender"].value_counts().items():
    print(f"  {gender}: {count} students")

print("\n Ready to analyze!")
