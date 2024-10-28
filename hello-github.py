print("Hello, GitHub!")

# Compound Interest Calculation
P = 10000 # principal amount
r = 0.05 # interest rate
n = 12
 # compounding monthly
t = 5
 # time in years
A = P * (1 + r / n)**(n * t)
print(f"The total amount after {t} years is: {A:.2f}")