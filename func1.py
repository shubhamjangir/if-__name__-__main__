def print_name(string):
    return f"My name is {string}"

def add_num(num1,num2):
    return num1+num2

print("Value of __name__ is:", __name__)
if __name__ == '__main__':
    print(print_name('Shubham'))
    print(add_num(10,15))