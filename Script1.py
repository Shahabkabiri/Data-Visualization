import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = r'C:\Users\Shahab Kabiri\Desktop\GAResults2.xlsx'

# Read Excel file into a dataframe
df = pd.read_excel(file_path)

# Filter the dataframe based on conditions
filtered_df = df[(df['TimeFilter'] == False) & (df['VolumeFilter'] == False)]

# Get the values for X and Y axes
x_values = filtered_df['LastTrainMSE']
y_values = filtered_df['LastTestMSE']
fbar_values = filtered_df['Fbars']

# Define the marker size based on Fbars values
marker_sizes = fbar_values * 1  # Adjust the scaling factor as needed

# Create the scatter plot with green data points
scatter = plt.scatter(x_values, y_values, marker='o', s=marker_sizes, c='green', label='Fbars')

# Set plot labels
plt.xlabel('LastTrainMSE')
plt.ylabel('LastTestMSE')

# Add legend for the size of data points with minimum and maximum values
min_marker_size = marker_sizes.min()
max_marker_size = marker_sizes.max()
min_fbar_value = fbar_values.min()
max_fbar_value = fbar_values.max()

plt.legend(
    title='Fbars',
    handles=[plt.scatter([], [], marker='o', s=min_marker_size, c='green', label=f'Min Size: {min_fbar_value}'),
             plt.scatter([], [], marker='o', s=max_marker_size, c='green', label=f'Max Size: {max_fbar_value}')],
    loc='best'
)

# Remove the plot title
scatter.axes.set_title('')

# Display the plot
plt.show()
