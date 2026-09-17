mssg = print(" prompts the user for the radius and height of a 3-dimensional cone and then"+
"calculates and prints the surface area and volume of the cone. The calculation of the surface area and "+
"the volume will be done in functions, as will the gathering of the inputs.")

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

print_radius=print(f"The surface area of the cone is: {3.14 * radius * (radius + (height**2 + radius**2)**0.5):.2f}")
print_volume=print(f"The volume of the cone is: {(1/3) * 3.14 * radius**2 * height:.2f}")

mssg
radius
height
print_radius
print_volume
