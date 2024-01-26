word = input('type a word: ')
normal_word = []
reversed_word = []


def palindrome_checker(word):
    for i in word:
        # adding every alphabet to an empty list
        normal_word.append(i)

    reversing = word[::-1]
    for i in reversing:
        # after reversing the string, adding every alphabet to another empty list
        reversed_word.append(i)

    # comparing both the lists, if they are same then it is a palindrome
    if normal_word == reversed_word:
        return True


if palindrome_checker(word):
    print('It is a palindrome')
else:
    print("no it isn't")