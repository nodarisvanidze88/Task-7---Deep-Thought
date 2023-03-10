def main():
    answList = ["42", "fortytwo"]                                                                   # answer's words list
    qtext = "What is the Answer to the Great Question of Life, the Universe, and Everything? "      # question
    question = input(qtext).lower()                                                                 # get user answer in lower case
    result = question.translate({ord(i): None for i in '.,/-_!#@ -+=$13567890"()'})                  # replace in string unwonted symbols
    if result in answList:                                                                          # check result in the list
        print("Yes")                                                                                # if True return yes
    else:
        print("No")                                                                                 # if False return no
main()
