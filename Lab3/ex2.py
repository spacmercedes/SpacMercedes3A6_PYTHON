# Write a function that receives a string as a parameter and 
# returns a dictionary in which the keys are the characters in the character
# string and the values are the number of occurrences of that character in the
# given text.


def ex2(text):
    #declaram dictionarul freq, loop prin fiecare caracter din text si numara de cate ori acel caracter apare in text
    freq = {char: text.count(char) for char in text} 
    return freq


if __name__ == "__main__":
    print(ex2("Ana has apples."))

