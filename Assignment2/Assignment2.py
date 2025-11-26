import spacy
import tracery
from tracery.modifiers import base_english

nlp = spacy.load("en_core_web_sm")
text = open("aro.txt").read()
doc = nlp(text)

nouns = list(set([token.lemma_ for token in doc if token.pos_ == "NOUN"]))
adj = list(set([token.lemma_ for token in doc if token.pos_ == "ADJ"]))
verbs = list(set([token.lemma_ for token in doc if token.pos_ == "VERB"]))
adv = list(set([token.lemma_ for token in doc if token.pos_ == "ADV"]))
phrases = list(set([chunk.text for chunk in doc.noun_chunks]))


rules = {
    "origin": [
        "#sentence.capitalize#",
        "#sentence2.capitalize#",
        "#sentence3.capitalize#"
    ],

    "sentence": [
        "#phrase# #verb#",
        "sometimes #phrase# #verb#",
    ],

    "sentence2": [
        "the #adj# #noun# #verb# #phrase#",
        "a #adj# #noun# #verb# #phrase# #adv#"
    ],

    "sentence3": [
        "#phrase# #verb# the #noun#",
        "maybe #phrase# will #verb# the #noun# #adv#"
    ],

    "phrase": phrases,
    "noun": nouns,
    "adj": adj,
    "verb": verbs,
    "adv": adv
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

for i in range(10):
    line = grammar.flatten("#origin#")
    print(line)