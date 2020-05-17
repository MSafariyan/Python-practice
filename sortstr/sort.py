# |  mahdi safarian |       sort numbers from 1 to 3 for
# |                 |       students.
# |     5/17/20     |       e.g: input = 3+2+1+2+3+2+1
# |_________________|           output = 1+1+2+2+2+3+3
#
numbers = input()
s = numbers.split("+")
s.sort()
print("+".join(s))
