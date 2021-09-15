import yfinance as fin

# Set the start and end date
start_date = '2000-01-01'
end_date = '2021-09-12'

target1 = 'GOOG'
target2 = 'MSFT'
target3 = 'CVLT'
data1 = fin.download(target1, start_date, end_date)
data2 = fin.download(target2, start_date, end_date)
data3 = fin.download(target3, start_date, end_date)


import matplotlib.pyplot as plt
%matplotlib inline

# Plot adjusted close price data
data1['Adj Close'].plot()
plt.show()


# Plot the adjusted close price
data1['Adj Close'].plot(figsize=(10, 7))

# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % target1, fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='red', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()


# Plot adjusted close price data
data2['Adj Close'].plot()
plt.show()

# Plot the adjusted close price
data2['Adj Close'].plot(figsize=(10, 7))

# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % target2, fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='orange', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()


# Plot adjusted close price data
data3['Adj Close'].plot()
plt.show()

# Plot the adjusted close price
data3['Adj Close'].plot(figsize=(10, 7))

# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % target3, fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='green', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()
