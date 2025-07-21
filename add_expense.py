import argparse
from datetime import datetime
from expense import Expense
from expense_manager import save_expense

def positive_amount(value):
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid float")
    if fvalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not positive")
    return fvalue

def valid_date(date_str):
    try:
        # برمی‌گردونیم رشته‌ی تاریخ به فرمت استاندارد (YYYY-MM-DD)
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.strftime('%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(f"{date_str} is not a valid date")

def non_empty_string(value):
    if not value.strip():
        raise argparse.ArgumentTypeError("This field cannot be empty")
    return value

parser = argparse.ArgumentParser()
parser.add_argument("--amount", type=positive_amount, required=True, help='Amount of expense; must be a positive number')
parser.add_argument("--date", type=valid_date, required=True, help='Date of the expense in YYYY-MM-DD format')
parser.add_argument("--category", type=non_empty_string, required=True, help='Category of the expense')
parser.add_argument("--description", type=str, default="", help='Description about the expense')
if __name__ == "__main__":
  args = parser.parse_args()

# ساخت شی Expense با مقادیر گرفته شده
  expense = Expense(args.amount, args.date, args.category, args.description)

# ذخیره هزینه در فایل
  save_expense(expense, 'expenses.csv')

  print("✅ Expense saved successfully!")





  
  
  
















