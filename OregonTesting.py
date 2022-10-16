import random
import keyboard

location = "Independence, Missouri"
day = 1
month = 0
year = 1848

oxenTotalCost = 0.00
foodTotalCost = 0.00
clothingTotalCost = 0.00
ammoTotalCost = 0.00
partsTotalCost = 0.00
totalCost = oxenTotalCost + foodTotalCost + clothingTotalCost + ammoTotalCost + partsTotalCost

money = 800

print("\n-----------------------------------")
print(f"Matts General Store".center(35))
print(f"{location:^35}\n".center(35))
print(f"{month} {day}, {year}".center(35))
print(f"-----------------------------------")
print(f"1. Oxen             ${oxenTotalCost:.2f}".center(35))
print(f"2. Food             ${foodTotalCost:.2f}".center(35))
print(f"3. Clothing         ${clothingTotalCost:.2f}".center(35))
print(f"4. Ammuntion        ${ammoTotalCost:.2f}".center(35))
print(f"5. Spare parts      ${partsTotalCost:.2f}".center(35))
print("-----------------------------------")
print(f"Total bill:           ${totalCost:.2f}")
print(f"\nAmount you have:     ${money:.2f}")

