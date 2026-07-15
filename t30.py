def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest:", si)

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time: "))

simple_interest(principal, rate, time)