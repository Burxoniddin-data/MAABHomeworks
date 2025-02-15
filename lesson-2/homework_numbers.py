def round_number():
    num = float(input("Enter a float number: "))
    print(f"Rounded to 2 decimal places: {round(num, 2)}")

def min_max():
    nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
    print(f"Largest: {max(nums)}, Smallest: {min(nums)}")

def km_to_m_cm():
    km = float(input("Enter distance in kilometers: "))
    print(f"Meters: {km * 1000}, Centimeters: {km * 100000}")

def division_remainder():
    a, b = map(int, input("Enter two numbers: ").split())
    print(f"Integer Division: {a // b}, Remainder: {a % b}")

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Fahrenheit: {celsius * 9/5 + 32}")

def last_digit():
    num = int(input("Enter a number: "))
    print(f"Last digit: {num % 10}")

def is_even():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

if __name__ == "__main__":
  round_number()
  min_max()
  km_to_m_cm()
  division_remainder()
  celsius_to_fahrenheit()
  last_digit()
  is_even()
