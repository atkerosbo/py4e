from PyDictionary import PyDictionary

dictionary = PyDictionary
while True
    word = input("Neter your word: ")
    if word == "":
        break
    print(dictionary.meaning(word))


#hard coded
#def main():
#    word_dictionary = {
#        'hi': 'A way of greeting',
#        'eyes': 'An organ to see with',
#        'earth': 'planet in space',


#    }
#    while True:
#        word = input("enter a word to define: ")
#        if word =="":
#            break
#        if word in word_dictionary:
#            print(word, ":", word_dictionary[word])
#main()