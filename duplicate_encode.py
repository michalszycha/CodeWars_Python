
#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    return ''.join([")" if word.lower().count(x.lower()) > 1 else "(" for x in word])


if __name__ == '__main__':
    print(duplicate_encode("din"))
    print(duplicate_encode("recede"))
    print(duplicate_encode("Success"))