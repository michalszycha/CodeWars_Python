#https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
import operator
from string import punctuation

new_punctuation = punctuation.replace("'", "")


def top_3_words(text: str):
    words = {}
    top_3 = []
    for char in new_punctuation:
        text = text.replace(char, ' ')
    for word in text.split(" "):
        word = word.lower()
        if word != "" and "".join(set(word)) not in punctuation:
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
    sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(3 if len(sorted_words) >= 3 else len(sorted_words)):
        x = sorted_words[i][0]
        top_3.append(sorted_words[i][0])
    return top_3


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  //wont won't won't "))
print(top_3_words("  '  "))
print(top_3_words("  '''  "))
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
