#!/usr/bin/usr python3
import sys
income=sys.argv[1]
try:
    income=int(income)
except:
    print('Error:',income)
    exit()
taxable_income=income-3500
tax=0
if taxable_income<=1500:
    tax=taxable_income*0.03
elif taxable_income<=4500:
    tax=taxable_income*0.1-105
elif taxable_income<=9000:
    tax=taxable_income*0.2-555;
elif taxable_income<=35000:
    tax=taxable_income*0.25-1005;
elif taxable_income<=55000:
    tax=taxable_income*0.3-2755;
elif taxable_income<=80000:
    tax=taxable_income*0.35-5505;
else:
    tax=taxable_income*0.45-13505;
tax=format(tax,".2f")
print(tax)
