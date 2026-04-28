temperatura = float(input(""))

if temperatura < 36.0:
    print("Hypothermia")
elif temperatura >= 36.0 and temperatura <= 37.5:
    print("Normal")
else: 
    print("Fever")