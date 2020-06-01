P = float(input("Power input in Watt: "))
N = float(input("RPM: "))
n = float(input("efficiency: "))
Sa = float(input("Maximum allowable shear stress in MPA: "))

#Calculations
T = ((P*60)/(2 * 3.14 * N)) * 1000
Tmax = n * T
d = ((Tmax * 16) / (3.14 * Sa)) ** (1 / 3)

print("Torque", T , "n*mm")
print("Maximum allowable torque", Tmax , "n*mm")
print("Diameter of shaft", round(d) , "mm")