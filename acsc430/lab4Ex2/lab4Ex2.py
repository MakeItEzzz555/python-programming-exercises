import math


def is_nneg_float(s):
    if s == "" or s.count(".") > 1:
        return False

    if "." in s:
        left, right = s.split(".", 1)
        if left == "" and right == "":
            return False
        return (left == "" or left.isdigit()) and (right == "" or right.isdigit())

    return s.isdigit()


def get_nneg_float(prompt):
    while True:
        value_text = input(prompt).strip()
        if is_nneg_float(value_text):
            return float(value_text)
        print("Must be a float value; please try again.")


def cone_surface_area(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)


def cone_volume(radius, height):
    return (math.pi * radius ** 2 * height) / 3


def main():
    print(
        "This program prompts the user for the radius and height of a cone "
        "and calculates its surface area and volume."
    )

    radius = get_nneg_float("Enter the radius of the cone: ")
    height = get_nneg_float("Enter the height of the cone: ")

    print(f"The surface area of the cone is: {cone_surface_area(radius, height):.2f}")
    print(f"The volume of the cone is: {cone_volume(radius, height):.2f}")


if __name__ == "__main__":
    main()
