# 15-16 l: klfbblslvjclmlnqklvg
# 6-13 h: pghjchdxhnjhjd
# 4-13 n: nnznntzznqnzbtzj

minChar = 15
maxChar = 16
char = 'l'
password = 'klfbblslvjclmlnqklvg'



def valid_pass():
    charCounter = 0
    for letter in password:
        #print(letter)
        if letter == char:
            charCounter = charCounter + 1
    print(charCounter)
    return minChar <= charCounter <= maxChar

valid_pass()