def talk_like_yoda():
    sentence=str(input("Enter a Sentence: "))
    words = sentence.split()
    sentence_new = " ".join(reversed(words))
    return sentence_new
print(talk_like_yoda())

'''sentence = input("Enter a Sentence")
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print (sentence_rev)
'''


