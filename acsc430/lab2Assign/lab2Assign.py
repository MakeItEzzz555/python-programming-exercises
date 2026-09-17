import math
sidelength = float(input("Enter length of side of garden (meters): "))
sideSquare = float(input("Enter side of the square meter each plant will occupy (meters):  "))
flowerDepth = float(input("Enter depth of garden soil (meters): "))
filledDepth = float(input("Enter depth of fill (meters): "))

radius = sidelength/4
circleArea = math.pi * radius ** 2
semiCircleArea = 4 * (circleArea/2)
area_total_flowerbeds = circleArea + semiCircleArea
gardenArea = sidelength ** 2
filledArea = gardenArea - area_total_flowerbeds

plantsCircle = int(circleArea/sideSquare)
plantsSemiCircle = int(semiCircleArea/sideSquare)
plantsTotal = int(plantsCircle + plantsSemiCircle)

circleVol = round(circleArea*flowerDepth, 1)
semicirclesVol = round(semiCircleArea * flowerDepth, 1)
totalSoilVol = round(area_total_flowerbeds * flowerDepth, 1)
filledVol = round(filledArea * filledDepth, 1)
# ----- OUTPUT -----
print("\n--- Garden Requirements ---")

print("\nPlants Needed:")
print("Semicircle flowerbeds:", plantsSemiCircle)
print("Central circle flowerbed:", plantsCircle)
print("Total plants:", plantsTotal)

print("\nSoil Volume (cubic meters):")
print("Semicircle flowerbeds:", semicirclesVol)
print("Central circle flowerbed:", circleVol)
print("Total soil needed:", totalSoilVol)

print("\nFill Material Volume (cubic meters):")
print("Total fill needed:", filledVol)