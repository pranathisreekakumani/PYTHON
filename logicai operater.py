age=16
citizen=true
print(age >=18 and citizen == true)

age=25
citizen = true
print(age >=18 and citizen == true)

#or
has_card =false
has_cash = true
print(has_card or has_cash)

is_logged_in = true
print(is_logged_in or has_card)

#atm eligibility check
balence =10000
withdraw_amount =5000
print(withdraw > 0 and withdraw <= balence)

#student eligibility check
marks=float(input("enter your marks:"))
attendance=float(input("enter your attendance percentage:"))
elligible = marks >= 85 and attendance >= 75

print("student is eligible for scholarship:", elligible)

#identity operator
a = None

print(a is None)
print(a is not None)

#bitwise operator
a=5
b=3
print(a & b)
print(a |b)
print(a ^ b)
