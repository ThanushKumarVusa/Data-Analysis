import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Book1.csv'  # Replace with the path to your file
df = pd.read_csv(file_path)

# Replace NaN values with 0 for proper stacking
df.fillna(0, inplace=True)

# Set the 'Week' column as the index
df.set_index('Week', inplace=True)

# Plot a stacked bar chart
ax = df.plot(kind='bar', stacked=True, figsize=(10, 6),
             color=['orange', 'green', 'red', 'purple'], 
             alpha=0.8)

# Set plot labels and title
plt.xlabel('Week', fontsize=12)
plt.ylabel('test change count', fontsize=12)
plt.title('Corrib Malawi 8.5', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate week labels for readability

# Add numbers on top of the bars
for p in ax.patches:
    height = p.get_height()
    if height > 0:  # Only annotate non-zero values
        width = p.get_width()
        x = p.get_x() + width / 2
        y = p.get_y() + height / 2
        ax.annotate(f'{height:.1f}', (x, y), ha='center', va='center', fontsize=8, color='white')

# Ensure y-axis starts from 0 and use integer values
plt.ylim(0, 30)  # Set the y-axis limit to 30
plt.yticks(range(0, 31, 2))  # Set y-ticks as integers with a step of 2

# Display the plot
plt.legend(title='', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend placement
plt.tight_layout()  # Adjust layout to prevent label cut-off
plt.show()
