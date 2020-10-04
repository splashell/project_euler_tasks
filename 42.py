'''Open word.txt, read them into a string and split the string into a list of words.'''
words = open('words.txt', 'r').read()
wordlist = words.split(",")
triangle_words = 0

'''Alphabet key-value dictionary.'''
alphabet_values = {'A':'1' , 'B':'2' , 'C':'3' , 'D':'4' , 'E':'5' , 'F':'6',
'G':'7' , 'H':'8' , 'I':'9' , 'J':'10' , 'K':'11' , 'L':'12' , 'M':'13',
'N':'14' , 'O':'15' , 'P':'16' , 'Q':'17' , 'R':'18' , 'S':'19' , 'T':'20',
'U':'21' , 'V':'22' , 'W':'23' , 'X':'24' , 'Y':'25' , 'Z':'26'}


'''Loop the list of words, create a list of alphabets, get the number value from the alphabet dictionary,
calculate the word value and compare the word value to the function values in a given range. Calculate and
print out the number of triangle words.'''
for item in wordlist:
    word_alphabets = []
    word_sum = 0

    for alphabet in item:
        word_alphabets.append(alphabet)

    for i in word_alphabets:
        if i in alphabet_values:
            word_sum += float(alphabet_values[i])
    for i in range(500):
        function_sum = 0.5*(i)*(i+1)
        if function_sum/word_sum == 1:
            print("Triangle word!")
            print(function_sum)
            print(word_alphabets)
            triangle_words += 1

print(f"{triangle_words} words were triangle words.")
