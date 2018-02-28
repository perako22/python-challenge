# Dependencies
import pandas as pd

# Save path to data set in a variable
data_file = "budget_data_1.csv"

# Use Pandas to read data
data_file_pd = pd.read_csv(data_file)

# The aggregate method groups all the dates by Month 
tot_Months = data_file_pd.aggregate("Date")

# The sum method sums total Revenue
tot_Revenue = data_file_pd["Revenue"].sum()

# The mean method averages total Revenue
ave_Revenue = data_file_pd["Revenue"].mean()

# The max method finds the max in the Revenue column
max_Revenue = data_file_pd["Revenue"].max()

# The min method finds the min in the Revenue column
min_Revenue = data_file_pd["Revenue"].min()

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Date))
print("Total Revenue: " + str(tot_Revenue))
print("Average Revenue Change: " + str(ave_Revenue))
print("Greatest Increase in Revenue: " + str(Date) + str("(") + str(max_Revenue ) + str(")"))
print("Greatest Decrease in Revenue: " + str(Date) + str("(") + str(min_Revenue) + str(")"))