# https://www.nltk.org/book/ch05.html


import nltk



def main():
    help = nltk.help.upenn_tagset()
    print(help)
    lines = 'lines is some string of words.'
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(lines)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    print (nouns)

    number = 1
    line = ""
    for (word, pos) in nltk.pos_tag(tokenized):

        if is_noun(pos):
            line = line + word + "(K" + str(number) + ") "
            number = number + 1
        else:
            line = line + word + " "
    print(lines)
    print(line)
    lines_tags = nltk.pos_tag(tokenized)
    print(lines_tags)
    for idx in range(1, number+1):
        print("R%d" % (idx))
        print(" - \n")



    lines_tags = nltk.pos_tag(tokenized)
    print(lines)
    print(lines_tags)

    # onk = nltk.pos_tag_sents(tokenized)
    # print(onk)




if __name__ == "__main__":
    main()