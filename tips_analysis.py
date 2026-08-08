import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset (built-in)
tips = sns.load_dataset('tips')

print("🍽️ TIPS DATASET – FIRST 5 ROWS")
print("=" * 40)
print(tips.head())

# 1. Distribution of total bill
sns.histplot(tips['total_bill'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Total Bill')
plt.savefig('bill_distribution.png')
plt.show()

# 2. Scatter plot: total bill vs tip (colored by day)
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time', s=100)
plt.title('Tip vs Total Bill (by Day and Time)')
plt.savefig('bill_tip_scatter.png')
plt.show()

# 3. Boxplot: tip by day
sns.boxplot(data=tips, x='day', y='tip', palette='Set2')
plt.title('Tip Distribution by Day')
plt.savefig('tip_by_day_boxplot.png')
plt.show()

# 4. Bar plot: average tip by sex and smoker
sns.barplot(data=tips, x='sex', y='tip', hue='smoker', palette='pastel')
plt.title('Average Tip by Sex and Smoking Status')
plt.savefig('tip_sex_smoker.png')
plt.show()

# 5. Heatmap: correlation between numeric columns
corr = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# 6. Pairplot: explore relationships
sns.pairplot(tips, hue='sex', diag_kind='hist')
plt.suptitle('Pairplot of Tips Data', y=1.02)
plt.savefig('pairplot.png')
plt.show()

print("\n✅ All plots saved as PNG files in the current folder.")