"""
Credit where credit is deserved: code obtained from Geeks for Geeks at
https://www.geeksforgeeks.org/readability-index-pythonnlp/
"""
import spacy
from textstat.textstat import textstatistics, easy_word_set, legacy_round
import math

def score(text):
    # Splits the text into sentences, using
    # Spacy's sentence segmentation which can
    # be found at https://spacy.io/usage/spacy-101
    def break_sentences(text):
        nlp = spacy.load('en')
        doc = nlp(unicode(text,encoding="utf-8"))
        return doc.sents

    # Returns Number of Words in the text
    def word_count(text):
        sentences = break_sentences(text)
        words = 0
        for sentence in sentences:
            words += len([token for token in sentence])
        return words

    # Returns the number of sentences in the text
    def sentence_count(text):
        sentences = break_sentences(text)
        length = 0
        for item in sentences:
            length += 1
        return length

    # Returns average sentence length
    def avg_sentence_length(text):
        words = word_count(text)
        sentences = sentence_count(text)
        average_sentence_length = float(words / sentences)
        return average_sentence_length

    # Textstat is a python package, to calculate statistics from
    # text to determine readability,
    # complexity and grade level of a particular corpus.
    # Package can be found at https://pypi.python.org/pypi/textstat
    def syllables_count(word):
        return textstatistics().syllable_count(word)

    # Returns the average number of syllables per
    # word in the text
    def avg_syllables_per_word(text):
        syllable = syllables_count(text)
        words = word_count(text)
        ASPW = float(syllable) / float(words)
        return legacy_round(ASPW, 1)

    # Return total Difficult Words in a text
    def difficult_words(text):

        # Find all words in the text
        words = []
        sentences = break_sentences(text)
        for sentence in sentences:
            words += [str(token) for token in sentence]

        # difficult words are those with syllables >= 2
        # easy_word_set is provide by Textstat as
        # a list of common words
        diff_words_set = set()

        for word in words:
            syllable_count = syllables_count(word)
            if word not in easy_word_set and syllable_count >= 2:
                diff_words_set.add(word)

        return len(diff_words_set)

    # A word is polysyllablic if it has more than 3 syllables
    # this functions returns the number of all such words
    # present in the text
    def poly_syllable_count(text):
        count = 0
        words = []
        sentences = break_sentences(text)
        for sentence in sentences:
            words += [token for token in sentence]


        for word in words:
            syllable_count = syllables_count(word)
            if syllable_count >= 3:
                count += 1
        return count

    def flesch_reading_ease(text):
        """
            Implements Flesch Formula:
            Here,
              ASL = average sentence length (number of words
                    divided by number of sentences)
              ASW = average word length in syllables (number of syllables
                    divided by number of words)
        """
        FRE = 206.835 - float(1.015 * avg_sentence_length(text)) -\
              float(84.6 * avg_syllables_per_word(text))
        return legacy_round(FRE, 2)
    flesch_score = (145 - flesch_reading_ease(text))/145

    def gunning_fog(text):
        per_diff_words = (difficult_words(text) / word_count(text) * 100) + 5
        grade = 0.4 * (avg_sentence_length(text) + per_diff_words)
        return grade
    #fog_score = (gunning_fog(text))/30

    def dale_chall_readability_score(text):
        """
            Implements Dale Challe Formula:
            Raw score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365
            Here,
                PDW = Percentage of difficult words.
                ASL = Average sentence length
        """
        words = word_count(text)
        # Number of words not termed as difficult words
        count = words - difficult_words(text)
        if words > 0:

            # Percentage of words not on difficult word list

            per = float(count) / float(words) * 100

        # diff_words stores percentage of difficult words
        diff_words = 100 - per

        raw_score = (0.1579 * diff_words) + \
                    (0.0496 * avg_sentence_length(text))

        # If Percentage of Difficult Words is greater than 5 %, then;
        # Adjusted Score = Raw Score + 3.6365,
        # otherwise Adjusted Score = Raw Score

        if diff_words > 5:

            raw_score += 3.6365

        return legacy_round(raw_score, 2)
    #dale_score = dale_chall_readability_score(text)/13

    return flesch_score
