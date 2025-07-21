class Expense:
    def __init__(self, amount, date, category, description):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.amount} | {self.date} | {self.category} | {self.description}"

    def to_csv_row(self):
        return [str(self.amount), self.date, self.category, self.description]

    @staticmethod
    def from_csv_row(row):
        return Expense(float(row['amount']), row['date'], row['category'], row['description'])
    
    def __eq__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return (self.amount == other.amount and self.date == other.date and self.category == other.category and self.description == other.description)
    
    def __hash__(self):
        return hash((self.amount , self.date , self.category , self.description))