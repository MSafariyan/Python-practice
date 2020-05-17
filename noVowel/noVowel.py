# |   Mahdi Safarian |   find vowel sound alphabet with regex
# |                  |   and remove them. add "." at the
# |     5/17/2020    |   sart of each non vowel alphabet
# |__________________|   and the output must be in lower case.
#
import re
#str = "aBAcAba"
str = input()
str = str.lower()
print(str)
str = re.sub("[aeiou]","",str)
str.split()
str = ".".join(str)
print("."+str)
