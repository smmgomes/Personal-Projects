from math import sqrt

# This function prints the polynomial of a function

def print_polynomial(coefficients: list) -> None:
    output = ''
    degree = len(coefficients) - 1
    i = 0
    while (degree != -1):
        if (coefficients[i] <= 0):
            output += '-'
        elif (i != 0):
            output += '+' 
        output += str(abs(coefficients[i]))
        if (degree != 0):
            output += 'x^' + str(degree)
        degree -= 1 
        i += 1
    print(output)


# This function uses the quadratic formula to calculate the solutions to the problem
# Works for 2 degree polynomial functions only
def quadratic_formula(coefficients: list) -> list:
    output = []
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    result1 = ((-1 * b) + sqrt((b**2) - (4*a*c))) / (2*a)
    result2 = ((-1 * b) - sqrt((b**2) - (4*a*c))) / (2*a)
    if (result1 == result2):
        print('There is only one output')
        print('x = ' + str(result1))
        return output 
    output.append('x = ' + str(result1))
    output.append('x = ' + str(result2))
    return output

# This method does the synthetic division
# It first finds the factors of the coefficient of the highest degree and the lowest degree
# Using the factors of those 2 and the division between the factors of those 2 coefficients
# we try and calculate all possible values that has the solution
def polynomial_division(coefficients:list) -> list:
    final_result = []
    degree = len(coefficients) - 1
    factors_of_first_coefficient = []
    factors_of_last_coefficient = []
    all_factors = []
    for i in range(1, max(abs(coefficients[0]), abs(coefficients[len(coefficients)-1]))):
        if (abs(coefficients[0])%i == 0 and i <= abs(coefficients[0])):
            factors_of_first_coefficient.append(i)
            factors_of_first_coefficient.append(-1*i)
        if (abs(coefficients[len(coefficients)-1])%i == 0 and i <= abs(coefficients[len(coefficients)-1])):
            factors_of_last_coefficient.append(i)
            factors_of_last_coefficient.append(-1*i)
    for i in factors_of_last_coefficient:
        for j in factors_of_first_coefficient:
            result = 0
            for k in range(len(coefficients)):
                result += coefficients[k]*((i/j)**(degree-k))
            if (result == 0):
                if ((i/j) not in all_factors):
                    all_factors.append(i/j)
                    final_result.append('x = ' + str(i/j))
    return final_result
            
if __name__ == '__main__':
    # Get the degree of the function from the user
    degree = int(input("Degree of the function: ")) + 1
    print('Enter the coefficients (Highest degree first): ')
    # Get the array of user inputs for the coefficients starting from highest degree to lowest degree
    coefficients = [int(input('> ')) for i in range(degree)]
    print('The polynomial is ')
    # Print the polynomial function
    print_polynomial(coefficients)
    # Initialize the variable for the answers
    answers = []
    if (degree - 1 == 2): answers = quadratic_formula(coefficients)
    else: answers = polynomial_division(coefficients)
    # Print all the answers accordingly
    for i in answers:
        print(i)
