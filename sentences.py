import random
def main():
    quantity = random.randint(0,2)
    t = ["past", "present"]
    tense = random.choice(t)
    sent1 = make_sentence(quantity,tense)
    sent2 = make_sentence(quantity,tense)
    sent3 = make_sentence(quantity,tense)
    sent4 = make_sentence(quantity,tense)
    sent5 = make_sentence(quantity,tense)
    sent6 = make_sentence(quantity,tense)
    print(f"{sent1}.")
    print(f"{sent2}.")
    print(f"{sent3}.")
    print(f"{sent4}.")
    print(f"{sent5}.")
    print(f"{sent6}.")

def make_sentence(quantity,tense):
    prepositional_phrase = get_prepositional_phrase(quantity)
    prepositional_phrase_2 = get_prepositional_phrase(quantity)
    verb = get_verb(quantity, tense)
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    sentence = f"{determiner.capitalize()} {noun} {prepositional_phrase_2} {verb} {prepositional_phrase}"
    return sentence
def get_prepositional_phrase(quantity):
    noun = get_noun(quantity)
    determiner = get_determiner(quantity)
    preposition = get_preposition()
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase




def get_determiner(quantity):
    if quantity == 1:
        deter_s = ["a","one","the"]
    else:
        deter_s = ["some","many","the"]

    deter = random.choice(deter_s)
    return deter
def get_noun(quantity):
    if quantity == 1:
        noun_s = ["bird","boy","car","cat","child","dog","girl","man","rabbit","woman"]
    else:
        noun_s = ["birds","boys","cars","cats","children","dogs","girls","men","rabbits","women"]

    noun = random.choice(noun_s)
    return noun

def get_verb(quantity, tense):
    if tense == "past" :
        verbs = ["drank","ate","grew","laughed","thought","ran","slept","talked","walked","wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks","eats","grows","laughs","thinks","runs","sleeps","talks","walks","writes"]
        else:
            verbs = ["drink","eat","grow","laugh","think","run","sleep","talk","walk","write"]
    else :
        verbs = [" will drink","will eat","will grow","will laugh","will think","will run","will sleep","will talk","will walk","will write"]
    
    verb = random.choice(verbs)
    return verb

def get_preposition():
    p = ["about","above","across","after","along","around",
    "at","before","behind","below","beyond","by","despite","except","for","from","in","into","near",
    "of","off","on","onto","out","over","past","to","under","with","without"]
    pw = random.choice(p)
    return pw

main()