import tracery
from tracery.modifiers import base_english

rules = {
    "origin": [
        "#intro# #scene# #conflict# #dialogue# #twist# #almost_ending# #ending#"],

    "intro": [
        "On a #weather#, #dinosaurs# woke up with a #idea.a#: open the first prehistoric restaurant.",
        "It was a #weather#, and #dinosaurs# dreamed of changing the world one #meal# at a time.",
        "Long before #firstname# lived, #dinosaurs# decided that #politics# were boring — it was time to #cook# instead."],

    "weather": ["sunny day", "stormy morning", "rainy evening", "foggy night", "humid afternoon"],

    "idea": ["brilliant idea", "wild dream", "strange craving", "political vision", "fishy inspiration",
             "delicious plan", "culinary revolution",

             "questionable ambition", "outrageous experiment", "half-baked concept", "bold agenda", "flaky proposal"],

    "firstNames": ["Aaliyah", "Aaron", "Abby", "Abigail", "Abraham", "Adam", "Addison",
                   "Adrian", "Adriana", "Adrianna", "Aidan"],

    "scene": [
        "They set up a #kitchen# in the middle of a #landform#.",
        "With #lavaBubbling# nearby, they began mixing #herbs#, #lavaDust#, and #fish# into a stew.",
        "Soon the smell of roasted #fish# spread across the #setting#, drawing a curious crowd of #hungryCreatures#."],

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
        "‘This isn’t just #food#,’ said #dinosaurs#, ‘this is #culinaryRevolution#!’",
        "‘Politics and fish never mix,’ mumbled #dinosaurs# as they #stirPot#.",
        "‘We shall rebuild under a #governmentForms#,’ shouted #dinosaurs#, holding up a #fork# like a #sword#."],

    "twist": [
        "Suddenly, the #fish# came to life and demanded to be appointed #seafoodOffice#.",
        "A passing #meteorite# landed on their #kitchen#, instantly inventing the concept of #barbecue#.",
        "To everyone’s shock, the #restaurant# became a new #governmentForms#, and customers had to #vote# before #eating#."],

    "almost_ending": [
        "By sunset, #dinosaurs# was hailed as a hero — and the first restaurateur-president of the #governmentForms#.",
        "In the end, all that remained was the smell of grilled #fish# and a legend about #legendThemes#.",
        "They never rebuilt the #restaurant#, but every #weather#, the winds still smell #faintly# of #fish# and ambition."],

    "ending": ["And this was the #topic#, presented by #newspapers# "],

    "topic": ["breaking news", "final broadcast", "tastiest scandal", "latest catastrophe", "top story",
              "prehistoric headline",
              "daily scoop", "midday special", "political meltdown", "meteor update", "fishy revelation",
              "governmental surprise",
              "dinosaurs’ dilemma", "chef’s secret", "culinary crisis", "fossil exclusive"
              ],

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

    "newspapers": ["The Wall Street Journal", "The New York Times", "USA Today", "Los Angeles Times",
                   "San Jose Mercury News",
                   "Daily News", "New York Post", "The Washington Post", "Chicago Sun-Times", "The Denver Post"],

    "meal": [
        "meal", "bite of destiny", "course in nation-building", "midnight tasting",
        "jurassic brunch", "policy snack", "lava-hot entrée", "election-day sampler",
        "trial portion", "chef’s referendum", "diplomatic tasting menu"
    ],

    "politics": [
        "politics", "parliamentary throat-clearing", "committee karaoke",
        "procedural limbo", "ballot gymnastics", "red-tape origami", "law-flavored paperwork"
    ],

    "cook": [
        "cook", "improvise a sauce", "braise the unknown", "whisk the status quo",
        "char the rulebook", "poach a treaty", "sauté the narrative", "steam the dissent",
        "pickle the agenda", "glaze the manifesto", "reduce a scandal"
    ],

    "kitchen": [
        "stone-fired kitchen", "leaf-roofed cookhouse", "mud-brick galley",
        "obsidian prep-hut", "open-air hearth", "lava-warmed pavilion", "basalt test kitchen"
    ],

    "landform": [
        "volcanic valley", "ash-ringed caldera", "smoldering canyon",
        "basalt amphitheater", "igneous plain", "ember-lit ravine"
    ],

    "lavaBubbling": [
        "lava bubbling", "magma burbling", "ember fizzing", "basalt purring", "fire-veins murmuring"
    ],

    "herbs": [
        "ferns and rumors", "wild thyme and wild theories", "stone-mint and budget cuts",
        "cycad fronds and courage", "amber basil and bravado", "sage and signed waivers"
    ],

    "lavaDust": [
        "lava dust", "obsidian grit", "ash powder", "smoke salt", "ember flakes", "meteor seasoning"
    ],

    "hungryCreatures": [
        "hungry creatures", "curious pterosaurs", "polite velociraptors", "gossiping iguanodonts",
        "ambling ammonites", "deadline-driven trilobites", "budget-conscious brachiosaurs"
    ],

    "food": [
        "food", "edible diplomacy", "comfort policy", "spoon-based science",
        "chaos cuisine", "narrative noodles", "existential snacks"
    ],

    "culinaryRevolution": [
        "culinary revolution", "sauce uprising", "menu manifesto",
        "forkspring", "edible insurrection", "the Pantry Spring"
    ],

    "stirPot": [
        "stirred the pot", "filibustered the stew", "whisked the quorum",
        "simmered the agenda", "tasted the motion", "seasoned the minutes"
    ],

    "fork": [
        "fork", "bone-tined fork", "obsidian fork", "antler fork", "two-pronged skewer", "parliamentary spork"
    ],

    "sword": [
        "sword", "ladle-saber", "skewer-blade", "chef’s saber", "fillet-blade", "tasting rapier"
    ],

    "seafoodOffice": [
        "Minister of Seafood", "Secretary of Brine", "Chancellor of Chowder",
        "Commissar of Cod", "Attorney General of Anchovy Affairs", "Controller of Crustaceans"
    ],

    "meteorite": [
        "meteorite", "space rock", "celestial pebble", "starlit boulder", "deadline from the sky"
    ],

    "barbecue": [
        "barbecue", "smokery", "ember cuisine", "firepit gastronomy", "grill doctrine", "char school"
    ],

    "restaurant": [
        "restaurant", "canteen", "cookhouse", "mess hall", "pop-up diner", "tasting tent", "policy bistro"
    ],

    "vote": [
        "vote", "sign a menu ballot", "raise a tasting hand", "submit a spoon proxy",
        "file a flavor motion", "call a savory roll-call"
    ],

    "eating": [
        "eating", "tasting", "sampling", "dining", "feasting", "nibbling with intent"
    ],

    "legendThemes": [
        "cooking, chaos, and courage", "salt, smoke, and sovereignty",
        "broth, ballots, and bravery", "flavor, flame, and freedom",
        "menus, meteors, and mischief"
    ],

    "faintly": [
        "faintly", "softly", "stubbornly", "mischievously", "heroically", "inevitably", "like a rumor"
    ]

}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

for i in range(1):
    (grammar.flatten('#origin#'))
    text = grammar.flatten("#origin#")
    sentences = text.split(".")
    for s in sentences:
        s = s.strip()
        if s:
            print(s + ".\n")
