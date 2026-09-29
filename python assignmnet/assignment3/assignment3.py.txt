sides = sorted([side1, side2, side3]) return (sides[0]**2 + sides[1]**2) == sides[2]**2

def main(): print("--- Right-Angled Triangle Checker ---") try: a = float(input("Enter the length of the first side: ")) b = float(input("Enter the length of the second side: ")) c = float(input("Enter the length of the third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Side lengths must be positive numbers.")
        return

    if is_right_triangle(a, b, c):
        print("The triangle is a right-angled triangle.")
    else:
        print("The triangle is NOT a right-angled triangle.")
        
except ValueError:
    print("Invalid input! Please enter numerical values.")
