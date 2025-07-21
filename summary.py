from expense_manager import read_all_expenses
from collections import defaultdict
from datetime import datetime
import csv

def total_expenses(expenses):
    return sum(e.amount for e in expenses)

def sum_by_category(expenses):
    result = defaultdict(float)
    for e in expenses:
        result[e.category] += e.amount
    return result

def days_span(expenses):
    if not expenses:
        return 0
    dates = [datetime.strptime(e.date, '%Y-%m-%d') for e in expenses]
    return (max(dates) - min(dates)).days + 1

def daily_average(total, day_count):
    if day_count > 0:
        return total / day_count
    return 0

def write_report(total, category_sums, daily_avg):
    with open('report.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Type", "Label", "Value"])
        writer.writeheader()

        writer.writerow({"Type": "Total", "Label": "", "Value": f"{total:.2f}"})
        for cat, amt in category_sums.items():
            writer.writerow({"Type": "Category", "Label": cat, "Value": f"{amt:.2f}"})
        writer.writerow({"Type": "Average", "Label": "", "Value": f"{daily_avg:.2f}"})

def main():
    expenses = read_all_expenses("expenses.csv")
    total = total_expenses(expenses)
    category_sums = sum_by_category(expenses)
    day_count = days_span(expenses)
    avg = daily_average(total, day_count)

    print("✅ Summary Report:")
    print(f"Total Expenses: {total:.2f}")
    print("By Category:")
    for cat, amt in category_sums.items():
        print(f"  {cat} : {amt:.2f}")
    print(f"Daily Average: {avg:.2f}")

    write_report(total, category_sums, avg)
    print("Report saved to report.csv")

if __name__ == "__main__":
    main()