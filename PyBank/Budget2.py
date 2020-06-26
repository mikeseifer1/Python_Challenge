import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_csv_path = os.path.join("..","Resources", "budget_data.csv")
month = 0
profits = 0
monthly_changes = 0
initial_profits = []
dollar_change = []
lowprofits = 0
highprofits = 0
total_chg_profits = 0
with open(budget_csv_path,'r') as csvfile:
    budget = csv.reader(csvfile, delimiter=",")
    csv_header = next(budget)
    #print(f"CSV Header: {csv_header}")
    monthly = 0
    date = 0
    
    for row in budget:
        
        month = month + 1
        
        profits = profits + int(row[1]) 
        final_profits = int(row[1]) 
        if  month ==1:
            dollar_change = row[1]
            initial_profits.append(row[1])
            index = 0 
        else:
            dollar_change = final_profits - int(initial_profits[index])
            initial_profits.append(row[1])
            index = index + 1
            monthly_changes = monthly_changes + dollar_change
        
        if int(dollar_change) < lowprofits:
            lowprofits = int(dollar_change)
            lowmonth = row[0] 
        if int(dollar_change) > highprofits:
            highprofits = int(dollar_change)
            highmonth = row[0]
        
average_chg_profit = monthly_changes/(month-1)

print("Financial Analysis")
print("------------------------------------")
print(f"Total months:  {month}")
print(f"Net Total Profits: ${profits}")
print(f"Average change: {average_chg_profit:.2f}")
print(f"Greatest Increase in Profits: {highmonth} ({highprofits})")
print(f"Greatest Decrease in Profits: {lowmonth} ({lowprofits})")

output_file = os.path.join("Budget.txt")
result = (
    "Financial Analysis\n"
    "------------------------------------\n"
    f"Total months:  {month}\n"
    f"Net Total Profits: ${profits}\n"
    f"Average change: {average_chg_profit:.2f}\n"
    f"Greatest Increase in Profits: {highmonth} ({highprofits})\n"
    f"Greatest Decrease in Profits: {lowmonth} ({lowprofits})\n"
)
with open(output_file, "w") as datafile:
    datafile.write(result)
    