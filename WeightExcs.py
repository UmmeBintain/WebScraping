weight = int(input("Weight: "))
unit = input("(L)lbs or (K)kg? ")
if unit == "L" or "l":
    output = weight * 0.45
elif unit == "K" or "k":
    output = weight / 0.45
print(output)