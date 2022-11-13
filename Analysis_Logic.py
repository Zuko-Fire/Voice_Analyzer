import os

import timer
from Functional_module import _processing_text
from Functional_module import add_dict
from Functional_module import search_sentence
import Result_Case
import time
import Voice


# #########################information#######################
#
# this module is used to read words from the buffer,
# stream them using nltk, count and
# add them to the dictionary with the result
#
# ###########################################################

use_special_word = False
use_sentence = False
dict_text_one = {}
sentence_one = []
sentence_two = []
repeats_one = 0
repeats_two = 0


def Step_One(special_word, countChanged):

    global sentence_one
    global dict_text_one
    global repeats_one
    global use_special_word

    text = ''
    try:
        text = Voice.record_volume(countChanged)
        if text == '' or text == 'Error':
            raise ValueError("Error")
    except Exception:
        return 'Error'



    sentence_one = _processing_text(text)
    dict_text_one = add_dict(sentence_one, dict_text_one)

    for i in dict_text_one.values():
        if int(i) > 1:
            repeats_one += i

    print(dict_text_one)

    if special_word[0] in dict_text_one.keys() and special_word[1] in dict_text_one.keys() and special_word[
        2] in dict_text_one.keys():
        use_special_word = True

    print("Please prepare for the retelling")
    print("waiting 10 second...")

    timer.start(countChanged)

    return Step_Two(countChanged)


def Step_Two(countChanged):
    global use_sentence
    global sentence_two
    global dict_text_one
    global repeats_two


    text = ''
    try:
        text = Voice.record_volume(countChanged)
        if text == '' or text == 'Error':
            raise ValueError("Error")
    except:
        return 'Error'


    sentence_two = _processing_text(text)

    dict_text_one = add_dict(sentence_two, dict_text_one)

    use_sentence = search_sentence(sentence_one, sentence_two)

    for i in dict_text_one.values():
        if i > 1:
            repeats_two += i
    return result()


def result():
    global use_special_word
    global use_sentence
    global dict_text_one
    resultText = ''
    if use_special_word != True and use_sentence != True and len(dict_text_one) <= 7 and repeats_one / repeats_two > 2:
        resultText = Result_Case.case1()

    if use_special_word != True and use_sentence != True and len(
            dict_text_one) <= 14 and repeats_one / repeats_two > 1.1:
        resultText = Result_Case.case2()

    if use_special_word != True and use_sentence != True and len(dict_text_one) > 14 and repeats_one / repeats_two <= 1:
        resultText = Result_Case.case3()

    if use_special_word == True and use_sentence != True or use_special_word != True and use_sentence == True and len(
            dict_text_one) > 14 and repeats_one / repeats_two <= 1:
        resultText = Result_Case.case4()

    if use_special_word == True and use_sentence != True or use_special_word != True and use_sentence == True and len(
            dict_text_one) <= 14 and repeats_one / repeats_two >= 1.1 and repeats_one / repeats_two <= 2:
        resultText = Result_Case.case5()

    if use_special_word == True and use_sentence != True or use_special_word != True and use_sentence == True and len(
            dict_text_one) <= 7 and repeats_one / repeats_two > 2:
        resultText = Result_Case.case6()

    if use_special_word == True and use_sentence == True and len(dict_text_one) <= 7 and repeats_one / repeats_two > 2:
        resultText = Result_Case.case7()

    if use_special_word == True and use_sentence == True and len(dict_text_one) <= 7 and repeats_one / repeats_two > 2:
        resultText = Result_Case.case8()

    if use_special_word == True and use_sentence == True and len(
            dict_text_one) >= 14 and repeats_one / repeats_two <= 1:

        resultText = Result_Case.case9()

    else:
        resultText = 'No result to this situation'

    return resultText