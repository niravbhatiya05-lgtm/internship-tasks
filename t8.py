def check_temperature(temp):
    if temp >= 35:
        print("Hot")
    elif temp >= 20:
        print("Warm")
    else:
        print("Cold")

def main():
    temperature = float(input("Enter temperature: "))
    check_temperature(temperature)

main()