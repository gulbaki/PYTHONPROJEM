boy = float(input("Boyunuzu metre cinsinden girin: "))
kilo = float(input("Kilonuzu kilogram cinsinden girin: "))

vki = kilo / (boy ** 2)
print(f"VKİ: {vki:.1f}")

if vki < 18.5:
    print("You are underweight!")
elif vki < 24:
    print("Your body shape is great!")
elif vki < 27:
    print("You are overweight!")
elif vki < 30:
    print("You are mildly obese!")
elif vki < 35:
    print("You are moderately obese!")
else:
    print("You are severely obese!")
