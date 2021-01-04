
'''

Advent of Code 2020 - Day 18

'''

formulas = []
with open('day18.txt', 'r') as file:
    for line in file:
        formulas.append( line.strip() )

# Part 1

def custom_eval(expression):
    operators = ['*', '/', '+', '-'] # only + and * will appear

    while any(operator in expression for operator in operators):
        m, d, a, s = len(expression), len(expression), len(expression), len(expression)
        if '*' in expression:
            m = expression.index('*')
        if '/' in expression:
            d = expression.index('/')
        if '+' in expression:
            a = expression.index('+')
        if '-' in expression:
            s = expression.index('-')

        mdas = [m, d, a, s]
        minimum = mdas.index(min(mdas))
        idx = expression.index(operators[minimum])
        right = expression[idx + 2:].split(' ')[0]
        if any(operator in expression[idx + 2:] for operator in operators):
            expression = str(eval(expression[:idx + 1] + right)) + expression[expression.index(' ', idx + 2 + 1):]
        else:
            expression = str(eval(expression[:idx + 1] + right))
            break

    return expression

def calculate(string):
    idx = 0
    while ')' in string:
        if string[idx] == ')':
            new_index = idx - 1 - string[:idx][::-1].index('(')
            operation = string[new_index:idx + 1][1:-1]
            string = string[:new_index] + str(custom_eval(operation)) + string[idx + 1:]
            idx = new_index # should be + 1, but that is taken care of with the += 1 below
        idx += 1
    return custom_eval(string)

total_sum = 0
for formula in formulas:
    total_sum += int(calculate(formula))

print('Advent of Code Day 18 Answer Part 1:', total_sum)

# Part 2 - addition before multiplication

def custom_eval_2(expression):
    while '+' in expression:
        strip_expression = expression.split(' ')
        strip_expression = [se for se in strip_expression if se != ''] # because I am lazy
        if '+' in strip_expression[2:] and len(strip_expression) == 3:
            expression = str(eval(' '.join(strip_expression[:3])))
        elif strip_expression.index('+') == 1: # + is the first sub-expression
            expression = str(eval(' '.join(strip_expression[:3]))) + \
                         ' ' + ' '.join(strip_expression[3:])
        elif strip_expression.index('+') == len(strip_expression) - 2: # second to last element
            expression = ' '.join(strip_expression[:-3]) + \
                         ' ' + str(eval(' '.join(strip_expression[-3:])))
        else: # in the middle
            idx = strip_expression.index('+')
            expression = ' '.join(strip_expression[:idx - 1]) + \
                         ' ' + str(eval(' '.join(strip_expression[idx - 1:idx + 2]))) + \
                         ' ' + ' '.join(strip_expression[idx + 2:])

    while '*' in expression:
        strip_expression = expression.split(' ')
        strip_expression = [se for se in strip_expression if se != '']  # because I am lazy
        if '*' in strip_expression[2:] and len(strip_expression) > 3:
            expression = str(eval(' '.join(strip_expression[:3]))) + \
                         ' ' + ' '.join(strip_expression[3:])
        else:
            expression = str(eval(' '.join(strip_expression)))

    return expression

def calculate_2(string):
    idx = 0
    while ')' in string:
        if string[idx] == ')':
            new_index = idx - 1 - string[:idx][::-1].index('(')
            operation = string[new_index:idx + 1][1:-1] # lazy issue is here
            string = string[:new_index] + str(custom_eval_2(operation)) + string[idx + 1:]
            idx = new_index # should be + 1, but that is taken care of with the += 1 below
        idx += 1
    return custom_eval_2(string)

total_sum_2 = 0
for formula in formulas:
    total_sum_2 += int(calculate_2(formula))

print('Advent of Code Day 18 Answer Part 2:', total_sum_2)

