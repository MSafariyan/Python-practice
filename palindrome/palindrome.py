# |      Mahdi Safarian    |  palindrome:
# |                        |  word, phrase, or sequence                                                                             # |                        |  that reads the same backwards
# |        5/17/2020       |  as forwards, e.g. madam.
# |________________________|
#
name=input("Enter a name: ")
eman = name[::-1]
if eman in name:
    print("palindrome")
else:
    print("not palindrome")
