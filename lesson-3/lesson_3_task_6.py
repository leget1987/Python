def int_func(text):
    '''this function returns a string in which the first letter of all words is uppercase'''
    new_text = text[0].upper() + text[1:]
    for i in range(len(text)):
        if text[i] == ' ':
            new_text = new_text[:i + 1] + text[i + 1].upper() + text[i + 2:]
    print(new_text)


int_func('text')
int_func('this text for testing the programm')
