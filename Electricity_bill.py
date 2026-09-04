A = input("Enter your name : ")
B = input("Enter your ID : ")
Previous_Meter_Reading = float(input("Enter your Previous_Meter_Reading : "))
Current_Meter_Reading = float(input("Enter your Current_Meter_Reading : "))
Cost_per_unit = 5

Units = Current_Meter_Reading - Previous_Meter_Reading
Energy_Charge = Units * Cost_per_unit
Electricity_Duty = 0.05 * Energy_Charge   # Corrected line
Fixed_Meter_Charge = 100
Net_Bill = Energy_Charge + Electricity_Duty + Fixed_Meter_Charge

print("Units Consumed:", Units)
print("Energy Charge:", Energy_Charge)
print("Electricity Duty (5%):", Electricity_Duty)
print("Fixed Meter Charge:", Fixed_Meter_Charge)
print("Net Bill:", Net_Bill)