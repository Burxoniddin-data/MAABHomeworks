def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return students, tuitions

def mean(numbers):
    return round(sum(numbers) / len(numbers), 2) if numbers else 0

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return round((numbers[n // 2 - 1] + numbers[n // 2]) / 2, 2)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    f = float(input("Enter a temperature in degrees F: "))
    print(f"{f} degrees F = {convert_far_to_cel(f)} degrees C")
    c = float(input("Enter a temperature in degrees C: "))
    print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")
    
    amount = float(input("Enter the initial amount: "))
    rate = float(input("Enter the annual rate (as decimal): "))
    years = int(input("Enter the number of years: "))
    invest(amount, rate, years)
    
    num = int(input("Enter a positive integer: "))
    factors(num)
    
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    students, tuitions = enrollment_stats(universities)
    print("*" * 30)
    print(f"Total students: {sum(students):,}")
    print(f"Total tuition: $ {sum(tuitions):,}")
    print(f"\nStudent mean: {mean(students)}")
    print(f"Student median: {median(students)}")
    print(f"\nTuition mean: $ {mean(tuitions)}")
    print(f"Tuition median: $ {median(tuitions)}")
    print("*" * 30)
    
    n = int(input("Enter a number to check if it's prime: "))
    print(f"{n} is prime: {is_prime(n)}")
