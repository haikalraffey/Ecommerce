from tabulate import tabulate
from math import sqrt

class Membership():

    def __init__(self, username, expense, income):
        self.username = username
        self.expense = expense
        self.income = income
    
    def show_benefit(self):
        tables = [
            ["Platinum", "15%", "Gold and Silver Membership Benefit + Cashback up to 30%"],
            ["Gold", "10%", "Silver Membership Benefit + Voucher Online Ride"],
            ["Silver", "8%", "Voucher for Meals"]
        ]

        headers = ["Membership", "Discount", "Benefits"]

        print("E-commerce Membership Benefit")
        print("")
        print(tabulate(tables, headers))
    
    def show_requirements(self):
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7]
        ]

        headers = ["Membership", "Monthly Expense (Juta)", "Monthly Income (Juta)"]

        print("E-commerce Membership Requirements")
        print("")
        print(tabulate(tables, headers))
    
    def predict(self):
        user = [self.expense, self.income]

        parameter = [
            [5, 7], 
            [6, 10], 
            [8, 15]
        ]

        membership = ["Silver", "Gold", "Platinum"]

        def calc_dist(user, parameter):
            dist = sqrt(((user[0] - parameter[0]) ** 2) + ((user[1] - parameter[1]) ** 2))
            return dist
            
        self.tier = None
        nearest_distance = float('inf')

        for i in range(len(parameter)):
            distance = calc_dist(user, parameter[i])
            
            if distance < nearest_distance:
                nearest_distance = distance
                self.tier = membership[i]
        
        print(f"{self.username} will be a {self.tier} member.")

    def calculate_price(self, harga_barang):
        total_price = sum(harga_barang)

        if self.tier == "Silver":
            total_price = total_price - (total_price * 0.08)
        elif self.tier == "Golden":
            total_price = total_price - (total_price * 0.10)
        elif self.tier == "Platinum":
            total_price = total_price - (total_price * 0.15)
        elif self.tier == None:
            total_price = total_price
        else:
            print("Your membership is invalid.")
        
        print(f"You are {self.tier} membership. Your total price is {total_price}.")