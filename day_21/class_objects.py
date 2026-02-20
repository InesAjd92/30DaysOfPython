### Day 21 : Class and objects ###

## Exercises ##

# Level 1 : 

# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics: 
    def __init__(self, data): 
        self.data = data 

    def count(self): 
        return len(self.data) # ok 
    def sum(self): 
        return sum(self.data) # ok 
    def min(self): 
        return min(self.data) # ok 
    def max(self):
        return max(self.data) # ok 
    def range(self): 
        return max(self.data) - min(self.data) # ok 
    def mean(self):
        return self.sum() / self.count() # don't forget () bc they are methods 
    def median(self): 
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2 

        if n % 2 == 0: 
            median = (sorted_data[mid - 1 ] + sorted_data[mid])/ 2
        else : 
            median = sorted_data[mid]
        return median
    def mode(self):
        frequency = dict()
        max_count = 0 
        mode = None
        for item in self.data : 
            frequency[item] = frequency.get(item, 0) + 1
            if frequency[item] > max_count:
                max_count = frequency[item]
                mode = item
        return mode 
    
    def variance(self): 
        mean = self.mean()
        return sum((x-mean)**2 for x in self.data) / self.count() # x is each data point, squared and substracted to the mean and divided by the len of the list 
        
    def std(self):
        return self.variance() ** 0.5
    
    def freq_dist(self): 
        frequency = dict()
        for item in self.data : 
            frequency[item] = frequency.get(item, 0) + 1
        return sorted(frequency.items(), key= lambda x: x[1], reverse= True)
    def describe(self):
        print(f"Count: {self.count()}")
        print(f"Sum: {self.sum()}")
        print(f"Min: {self.min()}")
        print(f"Max: {self.max()}")
        print(f"Range: {self.range()}")
        print(f"Mean: {round(self.mean())}")
        print(f"Median: {self.median()}")
        print(f"Mode: {self.mode()}")  
        print(f"Variance: {round(self.variance(), 1)}")
        print(f"Standard Deviation: {round(self.std(), 1)}")
        print(f"Frequency Distribution: {self.freq_dist()}")  


data = Statistics(ages)
data.describe()

# Level 2 :

# 1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount: 
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes if incomes is not None else []
        self.expenses = expenses if expenses is not None else []

    def total_income(self):
        total = 0
        for amount, description in self.incomes:
            total += amount
        return total
        
    def total_expense(self): 
        total = 0
        for amount, description in self.expenses:
            total += amount
        return total
    
    def add_income(self, amount, description): 
        self.incomes.append((amount, description))
    
    def add_expense(self, amount, description): 
        self.expenses.append((amount, description))

    def account_balance(self): 
        return self.total_income() - self.total_expense()
    
    def account_info(self): 
        return (f"{self.firstname} {self.lastname} - "
                f"Total Income: {self.total_income()}, "
                f"Total Expense: {self.total_expense()}, "
                f"Balance: {self.account_balance()}")


# test : 

account = PersonAccount("Ines", "Ajd", None, None)
account.add_income(2000, "Salary")
account.add_income(150, "Selling items")
account.add_expense(500, "Rent")
account.add_expense(200, "Groceries")

print("Total Income:", account.total_income())      # Should print 2150
print("Total Expense:", account.total_expense())    # Should print 700
print("Balance:", account.account_balance())        # Should print 1450
print(account.account_info())
