# Distance from zero

def distance_from_zero(num):
    if num[0] == '-' or num.isdigit():
        if len(num.split(".")) > 1:
            return abs(float(num))
        return abs(int(num))
    return "Nope"

num = input("Please enter a value: ")
print(distance_from_zero(num))