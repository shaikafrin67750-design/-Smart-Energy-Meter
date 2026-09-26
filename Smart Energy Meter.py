# Smart Energy Meter using Python

def calculate_energy(voltage, current, hours, tariff):
# Calculate power in watts
power = voltage * current

```
# Convert power to kW
power_kw = power / 1000

# Calculate energy in kWh
energy = power_kw * hours

# Calculate electricity cost
cost = energy * tariff

print("\n===== SMART ENERGY METER =====")
print(f"Voltage        : {voltage:.2f} V")
print(f"Current        : {current:.2f} A")
print(f"Power          : {power:.2f} W")
print(f"Energy Used    : {energy:.2f} kWh")
print(f"Electricity Cost: ₹{cost:.2f}")
```

while True:
print("\n===== SMART ENERGY METER =====")
print("1. Calculate Energy")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    try:
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        hours = float(input("Enter usage time (hours): "))
        tariff = float(input("Enter electricity tariff (₹/kWh): "))

        if voltage < 0 or current < 0 or hours < 0 or tariff < 0:
            print("Values cannot be negative.")
        else:
            calculate_energy(
                voltage,
                current,
                hours,
                tariff
            )

    except ValueError:
        print("Invalid input! Enter numbers only.")

elif choice == "2":
    print("Smart Energy Meter Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
