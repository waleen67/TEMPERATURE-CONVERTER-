print("=" * 50)
print("*********Welcome to convert temperature*********")
print("=" * 50)
while True:
    while True:
        unit = input("enter a unit(f/c) : ").strip().lower()
        if unit in ["f", "c","celsius", "fahrenheit"]:
         break
        print("enter a valid unit")
    while True:
        try:
            temperature = float(input("enter a temperature : "))
            break
        except ValueError:
            print("enter a valid temperature")
    if unit in ["f", "fahrenheit"]:
            if temperature <= -459.67 :
                print("invalid temperature")
            else:
                c = (temperature - 32) * 5/9
                print(f"the temperature is {c} degrees celsius")
    if unit in ["c", "celsius"]:
            if temperature < -273.15:
                 print("invalid temperature")
            else:
                 f = temperature * 9/5 + 32
                 print(f"the temperature is {f} degrees fahrenheit")
    again = input("Do you want to continue (y/n)? ").lower()
    if again != "y":
        print("Thank you for using this program")
        break

