  def check_username_password():
    print(all(input(f"Enter {field}: ") for field in ["username", "password"]))

def check_equal_numbers():
    print(input("Enter two numbers: ").split()[0] == input().split()[1])

def check_positive_even():
    num = int(input("Enter a number: "))
    print(num > 0 and num % 2 == 0)

def check_all_different():
    nums = list(map(int, input("Enter three numbers: ").split()))
    print(len(set(nums)) == 3)

def check_same_length():
    print(len(input("Enter first string: ")) == len(input("Enter second string: ")))

def divisible_by_3_5():
    num = int(input("Enter a number: "))
    print(num % 3 == 0 and num % 5 == 0)

def sum_greater_50():
    print(sum(map(int, input("Enter two numbers: ").split())) > 50)

def between_10_20():
    num = int(input("Enter a number: "))
    print(10 <= num <= 20)

if __name__ == "__main__":
  check_username_password()
  check_equal_numbers()
  check_positive_even()
  check_all_different()
  check_same_length()
  divisible_by_3_5()
  sum_greater_50()
  between_10_20()
