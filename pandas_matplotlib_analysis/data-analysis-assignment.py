# Data Analysis Assignment

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("DATA ANALYSIS ASSIGNMENT - STUDENT PERFORMANCE ANALYSIS")
print("=" * 60)

# CONFIGURATION
CSV_FILENAME = 'student_dataset.csv'

# TASK 1: LOAD AND EXPLORE THE DATASET

print("\n" + "="*50)
print("TASK 1: LOAD AND EXPLORE THE DATASET")
print("="*50)
try:
    print(f"Loading dataset: {CSV_FILENAME}")
    df = pd.read_csv(CSV_FILENAME)
    print(" Dataset loaded successfully!")
    
except FileNotFoundError:
    print(f" Error: File '{CSV_FILENAME}' not found.")
    print("Please run 'create_dataset.py' first!")
    exit()
except Exception as e:
    print(f" Error: {e}")
    exit()

# 1. Display first few rows
print("\n1. First 5 rows:")
print("-" * 30)
print(df.head())

# 2. Dataset structure
print("\n2. Dataset Information:")
print("-" * 30)
print(f"Shape: {df.shape}")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# 3. Data types
print("\n3. Data Types:")
print("-" * 30)
print(df.dtypes)

# 4. Dataset info
print("\n4. Dataset Info:")
print("-" * 30)
df.info()

# 5. Missing values
print("\n5. Missing Values:")
print("-" * 30)
missing_values = df.isnull().sum()
print(missing_values)
if missing_values.sum() == 0:
    print(" No missing values!")

# 6. Basic overview
print("\n6. Dataset Overview:")
print("-" * 30)
print("Majors:", list(df['major'].unique()))
print("Genders:", list(df['gender'].unique()))
print("Years:", sorted(list(df['year'].unique())))

# TASK 2: BASIC DATA ANALYSIS

print("\n" + "="*50)
print("TASK 2: BASIC DATA ANALYSIS")
print("="*50)

# 1. Basic statistics
numerical_cols = ['age', 'gpa', 'study_hours_per_week', 'extracurricular_activities', 'final_grade']
print("\n1. Basic Statistics:")
print("-" * 30)
print(df[numerical_cols].describe())

# 2. Group analysis by major
print("\n2. Analysis by Major:")
print("-" * 30)
major_analysis = df.groupby('major')[numerical_cols].mean()
print("Average values by major:")
print(major_analysis.round(2))

print("\nStudent count by major:")
print(df['major'].value_counts())

# 3. Correlations
print("\n3. Key Correlations:")
print("-" * 30)
corr1 = df['study_hours_per_week'].corr(df['gpa'])
corr2 = df['gpa'].corr(df['final_grade'])
print(f"Study Hours ↔ GPA: {corr1:.3f}")
print(f"GPA ↔ Final Grade: {corr2:.3f}")

# TASK 3: DATA VISUALIZATION

print("\n" + "="*50)
print("TASK 3: DATA VISUALIZATION")
print("="*50)

# Create figure with subplots
fig = plt.figure(figsize=(16, 12))

# Define colors for consistency
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']

# 1. LINE CHART
print("\n1. Creating Line Chart...")
plt.subplot(2, 2, 1)

majors = list(df['major'].unique())
for i, major in enumerate(majors):
    major_data = df[df['major'] == major]
    yearly_gpa = major_data.groupby('year')['gpa'].mean()
    
    plt.plot(yearly_gpa.index, yearly_gpa.values, 
             marker='o', linewidth=3, label=major, color=colors[i], markersize=8)

plt.title('GPA Trends by Major Over Years', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Year')
plt.ylabel('Average GPA')
plt.legend()
plt.grid(True, alpha=0.3)

# 2. BAR CHART
print("2. Creating Bar Chart...")
plt.subplot(2, 2, 2)

avg_grades = df.groupby('major')['final_grade'].mean()
x_pos = list(range(len(avg_grades)))
heights = [float(val) for val in avg_grades.values]
labels = [str(label) for label in avg_grades.index]

bars = plt.bar(x_pos, heights, color=colors[:len(heights)], alpha=0.8, width=0.6)

plt.title('Average Final Grade by Major', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Major')
plt.ylabel('Average Final Grade')
plt.xticks(x_pos, labels, rotation=45)

# Add value labels
for i, (bar, value) in enumerate(zip(bars, heights)):
    plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{value:.1f}', ha='center', va='bottom', fontweight='bold')

# 3. HISTOGRAM
print("3. Creating Histogram...")
plt.subplot(2, 2, 3)

plt.hist(df['study_hours_per_week'], bins=15, color='#74B9FF', 
         alpha=0.7, edgecolor='black', linewidth=1.2)
plt.title('Distribution of Study Hours per Week', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Study Hours per Week')
plt.ylabel('Number of Students')

mean_hours = df['study_hours_per_week'].mean()
plt.axvline(mean_hours, color='red', linestyle='--', linewidth=2, 
            label=f'Mean: {mean_hours:.1f}h')
plt.legend()
plt.grid(True, alpha=0.3)

# 4. SCATTER PLOT
print("4. Creating Scatter Plot...")
plt.subplot(2, 2, 4)

for i, major in enumerate(majors):
    major_data = df[df['major'] == major]
    plt.scatter(major_data['study_hours_per_week'], major_data['gpa'],
                alpha=0.7, s=60, label=major, color=colors[i])

plt.title('Study Hours vs GPA by Major', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Study Hours per Week')
plt.ylabel('GPA')
plt.legend()
plt.grid(True, alpha=0.3)

# Add trend line
x_vals = df['study_hours_per_week']
y_vals = df['gpa']
z = np.polyfit(x_vals, y_vals, 1)
p = np.poly1d(z)
plt.plot(sorted(x_vals), p(sorted(x_vals)), "r--", alpha=0.8, linewidth=2)

plt.tight_layout()
plt.show()

print(" Created 4 main visualizations!")

# ADDITIONAL VISUALIZATIONS

print("\n" + "="*40)
print("ADDITIONAL VISUALIZATIONS")
print("="*40)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Correlation heatmap
print("Creating correlation heatmap...")
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0, 
            square=True, ax=axes[0,0], fmt='.2f')
axes[0,0].set_title('Correlation Matrix', fontsize=14, fontweight='bold')

# 2. Box plot
print("Creating box plot...")
sns.boxplot(data=df, x='major', y='gpa', ax=axes[0,1])
axes[0,1].set_title('GPA Distribution by Major', fontsize=14, fontweight='bold')
axes[0,1].tick_params(axis='x', rotation=45)

# 3. Violin plot
print("Creating violin plot...")
sns.violinplot(data=df, x='gender', y='final_grade', ax=axes[1,0])
axes[1,0].set_title('Final Grade by Gender', fontsize=14, fontweight='bold')

# 4. Count plot
print("Creating count plot...")
job_counts = df.groupby(['major', 'part_time_job']).size().unstack()
job_counts.plot(kind='bar', ax=axes[1,1], color=['#FF6B6B', '#4ECDC4'])
axes[1,1].set_title('Part-time Jobs by Major', fontsize=14, fontweight='bold')
axes[1,1].tick_params(axis='x', rotation=45)
axes[1,1].legend(title='Part-time Job')

plt.tight_layout()
plt.show()

print(" Additional visualizations complete!")

# SUMMARY AND FINDINGS

print("\n" + "="*60)
print("ANALYSIS SUMMARY AND FINDINGS")
print("="*60)

print("\n DATASET SUMMARY:")
print("-" * 30)
print(f"• Total students: {len(df)}")
print(f"• Age range: {df['age'].min()}-{df['age'].max()} years")
print(f"• GPA range: {df['gpa'].min():.2f}-{df['gpa'].max():.2f}")
print(f"• Study hours: {df['study_hours_per_week'].min()}-{df['study_hours_per_week'].max()}/week")

print("\n KEY FINDINGS:")
print("-" * 30)

# Top performing major
top_major = df.groupby('major')['gpa'].mean().idxmax()
top_gpa = df.groupby('major')['gpa'].mean().max()
print(f"1.  Highest GPA Major: {top_major} (avg: {top_gpa:.2f})")

# Correlation insights
study_corr = df['study_hours_per_week'].corr(df['gpa'])
if study_corr > 0.5:
    strength = "Strong"
elif study_corr > 0.3:
    strength = "Moderate"
else:
    strength = "Weak"
print(f"2.  {strength} correlation: Study hours ↔ GPA ({study_corr:.3f})")

# Gender comparison
male_avg = df[df['gender'] == 'Male']['gpa'].mean()
female_avg = df[df['gender'] == 'Female']['gpa'].mean()
if abs(male_avg - female_avg) < 0.1:
    print(f"3.  Similar performance: Male ({male_avg:.2f}) vs Female ({female_avg:.2f})")
else:
    better = 'Male' if male_avg > female_avg else 'Female'
    print(f"3.  {better} students perform slightly better")

# Job impact
job_yes_avg = df[df['part_time_job'] == 'Yes']['gpa'].mean()
job_no_avg = df[df['part_time_job'] == 'No']['gpa'].mean()
impact = "positive" if job_yes_avg > job_no_avg else "negative"
print(f"4.  Part-time jobs: {impact} impact on GPA")

print("\n INSIGHTS:")
print("-" * 30)
high_performers = df[df['gpa'] >= 3.5]
if not high_performers.empty:
    avg_study = high_performers['study_hours_per_week'].mean()
    print(f" High performers (GPA ≥ 3.5) study {avg_study:.1f} hours/week on average")

most_common_major = df['major'].value_counts().index[0]
print(f" Most popular major: {most_common_major}")
print(f" Average student age: {df['age'].mean():.1f} years")

print("\n RECOMMENDATIONS:")
print("-" * 30)
print("• Increase study hours to improve academic performance")
print("• Balance extracurricular activities with studies")
print("• Consider major-specific academic support")
print("• Monitor part-time work impact on grades")

print("\n" + "="*60)
print(" ASSIGNMENT COMPLETED SUCCESSFULLY!")
print("="*60)
print("✓ Dataset loaded and explored (Task 1)")
print("✓ Statistical analysis performed (Task 2)") 
print("✓ 4 required visualizations created (Task 3)")
print("✓ Advanced plots and insights provided")
print("✓ Professional findings and recommendations")
print("="*60)
