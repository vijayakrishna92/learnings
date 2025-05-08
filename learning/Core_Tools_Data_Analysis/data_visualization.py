#data visualization
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o') # Create a simple line plot
plt.title('Simple Line Plot') # Add a title
plt.xlabel('X-axis') # Add x-axis label
plt.ylabel('Y-axis') # Add y-axis label
plt.show() # Display the plot
plt.savefig('images/plot_1.png')  # Save the plot as a PNG file

plt.bar(x, y, color='blue', alpha=0.5)  # Add a bar plot
plt.title('Simple Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
plt.savefig('images/plot_2.png')  # Save the bar plot as a PNG file

plt.hist(y, bins=5, color='green', alpha=0.7)  # Add a histogram
plt.title('Simple Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
plt.savefig('images/plot_3.png')  # Save the histogram as a PNG file

plt.scatter(x, y, color='red', label='Scatter Points')  # Add a scatter plot
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()  
plt.savefig('images/plot_4.png')  # Save the scatter plot as a PNG file