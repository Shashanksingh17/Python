P = int(input("Enter Principle"))
R = int(input("Enter Rate"))
Y = int(input("Enter Year"))

n = 12 * Y
r = float(R / (12 * 100))
payment = float(P * R / (1 - (1 + r) ** (-n)))
pay=str(payment)
print("Payment is : " + pay)
