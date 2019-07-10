print("This is your wack calculator")
def count_spaces(s):
    return s.count(" ")

def count_vowels(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    numY = s.count("y")
    sumVowels = numA + numE + numI + numO + numU + numY

    return sumVowels

def count_total(s):
    return count_spaces(s) + count_vowels(s)

print(count_vowels("wow wow wow, this hurts my soul"))

countNum = count_spaces("wow wow wow, this hurts my soul")
print(countNum)

print(count_total("wow wow wow, this hurts my soul"))
