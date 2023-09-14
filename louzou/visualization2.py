import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/intake.csv')

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['hours'], df['date'], alpha=0.5)
plt.xlabel('hours')
plt.ylabel('date')
plt.title('Hour of Taking vs. Date')
plt.grid(True)

# Set custom x-axis tick labels for better readability
plt.xticks(range(24), ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM'], rotation=45)

plt.savefig("static/intake2.png")