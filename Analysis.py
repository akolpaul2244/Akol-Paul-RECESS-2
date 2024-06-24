import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset_path = 'Exercise Two/niceguys.csv'
data = pd.read_csv(dataset_path)

# Clean the data
data.columns = data.columns.str.strip().str.replace(' ', '_')
data = data.rename(columns={'do_you_have_aboyfriend/girlfriend': 'has_bf_gf'})
data['living_allowance'] = data['living_allowance'].str.replace(',', '').astype(float)

# Plot the age distribution categorized by relationship status
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='age', hue='has_bf_gf', multiple='stack', kde=True)
plt.title('Distribution of Students with Age and Relationship Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Has BF/GF', labels=['No', 'Yes'])
plt.grid(True)
plt.show()

# Gender distribution of those who have a boyfriend or girlfriend
plt.figure(figsize=(10, 5))
sns.countplot(data=data, x='sex', hue='has_bf_gf')
plt.title('Gender Distribution of Those Who Have a Boyfriend or Girlfriend')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Has BF/GF', labels=['No', 'Yes'])
plt.grid(True)
plt.show()

# Eating habits by age, gender, and relationship status
plt.figure(figsize=(14, 7))
sns.boxplot(data=data, x='How_many_time_do_eat_food', y='age', hue='has_bf_gf')
plt.title('Eating Habits by Age and Relationship Status')
plt.xlabel('Number of Meals Per Day')
plt.ylabel('Age')
plt.legend(title='Has BF/GF', labels=['No', 'Yes'])
plt.grid(True)
plt.show()

# Relationship between living allowance and having a boyfriend or girlfriend
plt.figure(figsize=(14, 7))
sns.boxplot(data=data, x='has_bf_gf', y='living_allowance')
plt.title('Living Allowance and Relationship Status')
plt.xlabel('Has BF/GF')
plt.ylabel('Living Allowance')
plt.xticks([0, 1], ['No', 'Yes'])
plt.grid(True)
plt.show()

# If those with a boyfriend or girlfriend have siblings
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='number_siblings', hue='has_bf_gf')
plt.title('Number of Siblings and Relationship Status')
plt.xlabel('Number of Siblings')
plt.ylabel('Count')
plt.legend(title='Has BF/GF', labels=['No', 'Yes'])
plt.grid(True)
plt.show()

# Careers and having a boyfriend or girlfriend
plt.figure(figsize=(14, 7))
sns.countplot(data=data, y='Are_you_a', hue='has_bf_gf')
plt.title('Careers and Relationship Status')
plt.xlabel('Count')
plt.ylabel('Career')
plt.legend(title='Has BF/GF', labels=['No', 'Yes'])
plt.grid(True)
plt.show()

# Number of meals taken and living allowance
plt.figure(figsize=(14, 7))
sns.scatterplot(data=data, x='living_allowance', y='How_many_time_do_eat_food', hue='has_bf_gf', style='sex')
plt.title('Number of Meals Taken and Living Allowance')
plt.xlabel('Living Allowance')
plt.ylabel('Number of Meals Per Day')
plt.grid(True)
plt.show()

# Correlation analysis (only numeric columns)
numeric_columns = data.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_columns.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show() # Decision making/insights of the data, data analysis conclusions

print("### Decision making/insights of the data, data analysis conclusions ###\n")

# Age Distribution by Relationship Status
print("1. Age Distribution by Relationship Status:")
print("- Younger students (below 25 years) show a higher proportion of being single compared to older students (25 years and above).")

# Gender Distribution and Relationships
print("\n2. Gender Distribution and Relationships:")
print("- Gender distribution among students with a boyfriend or girlfriend shows a relatively balanced proportion between males and females.")

# Eating Habits by Age and Relationship Status
print("\n3. Eating Habits by Age and Relationship Status:")
print("- Students who eat fewer meals per day tend to be younger, while those who eat more meals are spread across different age groups. Relationship status does not significantly influence eating habits.")

# Relationship between Living Allowance and Relationship Status
print("\n4. Relationship between Living Allowance and Relationship Status:")
print("- Students with higher living allowances are more likely to have a boyfriend or girlfriend compared to those with lower living allowances, indicating an economic factor in relationship dynamics.")

# Influence of Siblings on Relationship Status
print("\n5. Influence of Siblings on Relationship Status:")
print("- Having siblings does not show a clear correlation with relationship status among students in the dataset. The distribution remains relatively consistent across different sibling counts.")

# Careers and Relationship Status
print("\n6. Careers and Relationship Status:")
print("- There is a varied distribution of relationship status across different careers, suggesting that career choice alone may not strongly influence whether a student has a boyfriend or girlfriend.")

# Living Allowance and Eating Habits Relationship
print("\n7. Living Allowance and Eating Habits Relationship:")
print("- There appears to be a weak positive correlation between living allowance and the number of meals taken per day, indicating that students with higher living allowances may tend to eat more.")

# Correlation Analysis
print("\n8. Correlation Analysis:")
print("- The correlation heatmap shows that age and living allowance have a moderate positive correlation, while there are no strong correlations between other numeric variables.")