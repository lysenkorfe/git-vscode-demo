
def remove_punctuation(str):
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # remove punctuation from the string
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    # display the unpunctuated string
    print(no_punct)

if __name__=='__main__':
    # To take input from the user
    # my_str = input("Enter a string: ")
    my_str = "Hello!!!, he said ---and went."
    remove_punctuation(my_str)
