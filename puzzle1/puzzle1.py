file = open('./puz1-1.txt')
string_brackets = file.read()
file.close()

#without storing a string in a variable I was not able to get the right answer.
# when I pasted the string through the input it was just 4095 characters long, while in reality it's length was 7000
# print(len(input())) // -> 4095
# print(len(brackets)) // -> 7000
def count_floor(brackets): #part 1
    state = 0
    for i in range(len(brackets)):
        current_symbol = brackets[i]
        if current_symbol == '(':
            state += 1
        elif current_symbol == ')':
            state -= 1
    return state

what_floor = count_floor(string_brackets)
print(f'floor: ${what_floor}')

'''
# this code is less efficient according to its time complexity, but reads nice and looks neat. Big O(2n + 1) => big O (n)
def whichLevel(brackets):
    up = sum(1 for x in brackets if x == '(')
    down = sum(-1 for x in brackets if x == ')')
    return(up + down)

print(whichLevel())
'''
# part 2: find the position of the first character that causes to go negative (enter the basement)
def firstBasmtEntering(instructions):
    state = 0
    for i in range(len(instructions)):
        current_symbol = instructions[i]
        if current_symbol == '(':
            state += 1
        elif current_symbol == ')':
            state -= 1
        if (state < 0):
            return i + 1 #just a task condition

print('firstBasmtEntering', firstBasmtEntering(string_brackets))