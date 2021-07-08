'''
Calculate the tip
Your goal is to find out exactly how much tip you should give after receiving a service. In this scenario, ask for the total bill.
Then display the tip for 18%, 20% and 25%.

Example:

Prompt: what's the total bill for today, please?
Input: $55.87
Output: 18% tip is $10.06, which brings your total to $65.93
Remember you want to be nice, so don't forget to round up. To push this more, ask for the number of people involved,
then evenly split the tip and total cost among them.

To go even a step further, split unevenly (for example, one person pays 70% of the bill while the other pays 30%)

'''

import math
import sys


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def calculate_tip(rate, total):
    return round_up(rate*total,2)

def calculate_total(rate, total):
    tip = calculate_tip(rate,total)
    return round(tip + total,2)

def calculate_even_split(rate,total,number_paying):
    tip = calculate_tip(rate, total)
    return round((tip+total)/number_paying,2)


print('This program will calculate the tip for a bill or payment')
try:
    total_bill = float(input('Please enter the total amount to be paid: '))
except ValueError:
    sys.exit('Not a number')

total_number_paying = int(input('How many people are paying the bill? '))
print('The total amount to be paid is: £{}'.format(total_bill))

print('An 18% tip would be: £{}'.format(calculate_tip(0.18,total_bill)))
print('And the total will therefore be: £{}'.format(calculate_total(0.18,total_bill)))
print('For the total number of {} payees. The payment with 18% tip will be £{} per payee'.format(total_number_paying,calculate_even_split(0.18,total_bill,total_number_paying)))

print('An 20% tip would be: £{}'.format(calculate_tip(0.20,total_bill)))
print('And the total will therefore be: £{}'.format(calculate_total(0.20,total_bill)))
print('For the total number of {} payees. The payment with 20% tip will be £{} per payee'.format(total_number_paying,calculate_even_split(0.20,total_bill,total_number_paying)))

print('An 25% tip would be: £{}'.format(calculate_tip(0.25,total_bill)))
print('And the total will therefore be: £{}'.format(calculate_total(0.25,total_bill)))
print('For the total number of {} payees. The payment with 25% tip will be £{} per payee'.format(total_number_paying,calculate_even_split(0.25,total_bill,total_number_paying)))
print()

print('If we consider an unequal split between the payees')
split_percentage = input('What will be the split of the bill payment? For example 70/30? Please state in this format: ')
percentages = (split_percentage.split('/'))
splitOne = float(percentages[0])
splitTwo = float(percentages[1])
#calculate what part of total and tip goes to each person
print('The first payment is', round_up(splitOne/100*total_bill,2))
print('The second payment is', round_up(splitTwo/100*total_bill,2))
