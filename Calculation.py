import random
import webbrowser
import mysql.connector as msc

conn = msc.connect(host = "localhost", username = "root", password = "ahsirk", database = "emi")
c = conn.cursor()
if conn.is_connected():
    print("Successfully connected to database.")
else:
    print("Error")
loan = ["Housing loan","Personal Loan","Vehicle Loan","Consumer Loan",
        "Gold Loan", "Renovation Loan", "Education Loan","Marriage Loan","Top Up Loan"]
interest = [ [6.9, 8.8], [12, 15], [10, 12],[10, 12], [25, 29], [8.7, 10.3], [7.75, 8.8], [8.15, 10.9], [7.45-8.80]]

for i, l in enumerate(loan):
    print(f"{l} - {i+1}", end = "\n")

while True:
    ch = int(input("\nEnter the number: "))
    if ch >=1 and ch <=8:
        principal = int(input("Enter the principal amount: "))
        rate = round(random.uniform(interest[ch-1][0],interest[ch-1][1]),2)
        monthly_i = rate/12/100
        print(f"\nThe annual interest is {rate}%")
        t = int(input("Enter the number of years: "))
        time = 12*t
        monthly_emi = round(principal*monthly_i*((1+monthly_i)**time)/(((1+monthly_i)**time)-1))
        t_amt_pay = monthly_emi * time
        interest_amt = t_amt_pay - principal
        phone = input("Enter your phone number: ")
        name = input("Enter your name: ")
        f = open("emi.html","w")
        h = f"""
        <html>
        <head>YOUR HOME LOAN DETAILS
        <title> EMI HTML</title>
        </head>
        <body>
        <p>Principal amount is &#8377; {principal:,}</p>
        <p>Annual Interest is {rate}%</p>
        <p>Your monthly emi is &#8377; {monthly_emi:,}</p>
        <p>Total amount payable is &#8377; {t_amt_pay:,}</p>
        <p>Interest amount is &#8377; {interest_amt:,}</p>
        <p>Total tenure is {t} years</p>
        </body>
        </html>"""
        f.write(h)
        webbrowser.open('emi.html', 'r')
        f.close()
        qry = "insert into loan values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (phone, name, principal, rate, monthly_emi, t_amt_pay, interest_amt, t)
        c.execute(qry, val)
        conn.commit()
        break

    elif ch == 9:
        print("You have chosen top up loan")
        break

    else:
        print("Invalid. Try Again")

'''
print(f"\nYour monthly emi is {monthly_emi}")
print(f"Total amount payable is {t_amt_pay}")
print(f"Principal amount is {principal}")
print(f"Interest amount is {interest_amt}")
'''
conn.close()
c.close()
