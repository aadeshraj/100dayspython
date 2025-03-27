print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $ ")
total_bill_float = float(total_bill)
tip_percentage = input( "How much tip would you like to give? 10 , 12 or 15?")
tip_percent_float = float(tip_percentage)
split_bill = input("How many people to split the bill?")
split_bill_int = int(split_bill)
totalbillfinal = (total_bill_float * (tip_percent_float / 100)) + total_bill_float
divide = totalbillfinal / split_bill_int
print(f"Each person should pay: ${divide}")

