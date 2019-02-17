from googletrans import Translator
from random import randint
import lan
import sim


# input_sentence = "I'm going to get a scholarship to King's College, I probably wouldn't brag but dang, I amaze and astonish. The problem is I got a lotta brains but no polish. I got to holler just to be heard, with every word I drop knowledge. "

total = 10
lan_paths = 5


def circuit(english_sentence):
    translator = Translator()
    translation = english_sentence
    src_lan = ''
    dest_lan = ''

    circ = "english -> "
    for x in range(lan_paths):

        if (x == 0):
            src_lan = 'en'
        else:
            src_lan = dest_lan

        random_index = randint(0, 105)
        dest_lan = lan.get_language(random_index)

        translation = translator.translate(translation,
                                           src=src_lan, dest=dest_lan).text
        circ += lan.lan_dict[dest_lan] + " -> "
    print(circ + " english.")

    return translator.translate(translation, src=dest_lan, dest='en').text


def get_similarity_score(sentence):
    sum_scores = []

    for x in range(total):
        final_sentence = circuit(sentence)
        sum_scores.append(sim.get_score(sentence, final_sentence))
        print(final_sentence)

    return max(sum_scores)
