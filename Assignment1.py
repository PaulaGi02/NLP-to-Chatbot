import tracery
from tracery.modifiers import base_english

rules = {
    "origin": [
        "#intro# #scene# #conflict# #dialogue# #twist# #almost_ending# #ending#"],

    "intro": [
        "On a #weather#, #dinosaurs# woke up with a brilliant idea: open the first prehistoric restaurant.",
        "It was a #weather#, and #dinosaurs# dreamed of changing the world one meal at a time.",
        "Long before #firstname# lived, #dinosaurs# decided that politics were boring — it was time to cook instead." ],


    "firstNames": ["Aaliyah","Aaron", "Abby", "Abigail",  "Abraham", "Adam",  "Addison",
                   "Adrian", "Adriana", "Adrianna","Aidan"],

    "scene": [
        "They set up a kitchen in the middle of a volcanic valley.",
        "With lava bubbling nearby, they began mixing herbs, lava dust, and #fish# into a stew.",
        "Soon the smell of roasted #fish# spread across the #setting#, drawing a curious crowd of hungry creatures."],

    "setting": [
        "primeval jungle",
        "ancient swamp",
        "crystal cave",
        "sandy coast",
        "muddy crater"],

    "conflict": [
        "But disaster struck when a group of rival #dinosaurs# from the neighboring #governmentForms# demanded free samples.",
        "However, their cooking license was revoked by the #governmentForms#, claiming ‘improper use of abalone.’",
        "Unfortunately, the head chef burned the #fish# after arguing about whether #dinosaurs# should live in a #governmentForms#."],

    "dialogue": [
        "‘This isn’t just food,’ said #dinosaurs#, ‘this is culinary revolution!’",
        "‘Politics and fish never mix,’ mumbled #dinosaurs# as they stirred the pot.",
        "‘We shall rebuild under a #governmentForms#,’ shouted #dinosaurs#, holding up a fork like a sword."],

    "twist": [
        "Suddenly, the #fish# came to life and demanded to be appointed Minister of Seafood.",
        "A passing meteorite landed on their kitchen, instantly inventing the concept of barbecue.",
        "To everyone’s shock, the restaurant became a new #governmentForms#, and customers had to vote before eating."],

    "almost_ending": [
        "By sunset, #dinosaurs# was hailed as a hero — and the first restaurateur-president of the #governmentForms#.",
        "In the end, all that remained was the smell of grilled #fish# and a legend about cooking, chaos, and courage.",
        "They never rebuilt the restaurant, but every #weather#, the winds still smell faintly of #fish# and ambition."],

    "ending": ["And this was the breaking news today, presented by #newspapers# "],

    "dinosaurs": [
        "Kangnasaurus", "Lophostropheus", "Spinophorosaurus", "Epachthosaurus", "Coelurosauria",
        "Lycorhinus", "Adasaurus", "Draconyx", "Ceratops", "Lagerpeton",
        "Qiaowanlong", "Rhynchosaur", "Ningyuansaurus", "Palaeolimnornis"],

    "governmentForms": [
        "autocracy", "democracy", "oligarchy", "anarchy", "confederation", "federation",
        "unitary state", "demarchy", "electocracy", "republic", "absolute monarchy", "dictatorship"],

    "fish": [
        "abalone", "Alaska pollock", "anchovy", "Atlantic salmon", "Chilean sea bass", "cod",
        "catfish", "halibut", "sardine", "tuna", "rainbow trout", "red snapper", "pike", "flounder"],

    "weather": ["sunny day", "stormy morning", "rainy evening", "foggy night", "humid afternoon"],

    "newspapers": [ "The Wall Street Journal", "The New York Times","USA Today","Los Angeles Times","San Jose Mercury News",
        "Daily News", "New York Post", "The Washington Post", "Chicago Sun-Times", "The Denver Post"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

for i in range(1):
    (grammar.flatten('#origin#').split("\n"))
    text = grammar.flatten("#origin#")
    sentences = text.split(".")
    for s in sentences:
        s = s.strip()
        if s:
            print(s + ".\n")