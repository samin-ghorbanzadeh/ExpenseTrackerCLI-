from expense_manager import read_all_expenses
from datetime import datetime
import argparse
from expense import Expense
from add_expense import valid_date

list_expense = read_all_expenses("expenses.csv")
new_list = sorted(list_expense, key=lambda e: datetime.strptime(e.date, '%Y-%m-%d'), reverse=True)

def filter_last(args_last):
    d = []
    if args_last > len(new_list):
        print(f"The requested number ({args_last}) is greater than the total number of expenses ({len(new_list)}). Displaying all available records.")
    for expense in new_list[:args_last]:
        d.append(expense)
    return d  

def filter_category(args_category):
    b = []
    for item in new_list:
        if item.category == args_category:
            b.append(item)
    return b    

def filter_date(args_from_date, args_to_date):
    c = []
    for item in new_list:
        if args_from_date <= item.date <= args_to_date:
            c.append(item)
    return c 

def apply_filters(args):
    if args.last and not args.category and not (args.from_date and args.to_date):
        return filter_last(args.last)
    
    if args.category and not args.last and not (args.from_date and args.to_date):
        return filter_category(args.category)
    
    if (args.from_date and args.to_date) and not args.category and not args.last:
        return filter_date(args.from_date, args.to_date)
    
    if args.last and args.category and not (args.from_date and args.to_date):      
        return list(set(filter_last(args.last)) & set(filter_category(args.category)))
    
    if args.last and (args.from_date and args.to_date) and not args.category:
        return list(set(filter_last(args.last)) & set(filter_date(args.from_date, args.to_date)))
    
    if (args.from_date and args.to_date) and args.category and not args.last:
        return list(set(filter_date(args.from_date, args.to_date)) & set(filter_category(args.category)))
    
    if (args.from_date and args.to_date) and args.category and args.last:
        return list(set(filter_last(args.last)) & set(filter_category(args.category)) & set(filter_date(args.from_date, args.to_date)))

parser = argparse.ArgumentParser()
parser.add_argument("--last", type=int, default=10, help="Show the last N expense records (default: 10)")
parser.add_argument("--category", type=str, help="Filter expenses by category")
parser.add_argument("--from", dest="from_date", type=valid_date, help='Filter expenses from this date (inclusive) - format: YYYY-MM-DD')
parser.add_argument("--to", dest="to_date", type=valid_date, help='Filter expenses up to this date (inclusive) - format: YYYY-MM-DD')

args = parser.parse_args()

result = sorted(apply_filters(args), key=lambda e: datetime.strptime(e.date, '%Y-%m-%d'), reverse=True)
for e in result:
    print(e)

        
        
        
        
        
        
        
        
        