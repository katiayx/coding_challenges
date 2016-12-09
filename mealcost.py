meal_cost = float(raw_input())
tip_percent = int(float(raw_input()))
tax_percent = int(float(raw_input()))


def calc_total_meal_cost(meal_cost, tip_percent, tax_percent):
 
    tip = float(tip_percent)/100*meal_cost #integer divide by 100(int) will return zero, e.g. (8/100=0). 
    #must float one number
    tax = float(tax_percent)/100*meal_cost
    total_cost = round(float(meal_cost) + tip + tax) #need to round UP so e.g. 2.5 is rounded to 3.0
    total_cost = int(total_cost)
    
    print "The total meal cost is " + str(total_cost) + " " + "dollars."


calc_total_meal_cost(meal_cost, tip_percent, tax_percent)