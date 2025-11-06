import tracery
from tracery.modifiers import base_english

rules = { "start": ["On a #weather#", ],
    "origin": [
        "Tonight’s special: #dinosaurs#’ signature #fish# served in the style of  #governmentForms.a#.",
        "Chef #dinosaurs# proudly presents ‘#fish# à la #governmentForms#’.",
        "Our prehistoric combo: #fish# with a side of #governmentForms#, fresh from #dinosaurs#’ kitchen.",
        "The #dinosaurs# Diner — where every #fish# is cooked under strict #governmentForms# supervision!"
    ],
        "governmentForms": ["autocracy", "democracy", "oligarchy", "anarchy", "confederation","federation", "unitary state", "demarchy", "electocracy", "republic","absolute monarchy", "dictatorship"],
                "dinosaurs": ["Kangnasaurus", "Lophostropheus", "Spinophorosaurus", "Epachthosaurus", "Coelurosauria", "Lycorhinus", "Adasaurus", "Draconyx", "Ceratops", "Lagerpeton", "Qiaowanlong", "Rhynchosaur", "Ningyuansaurus", "Palaeolimnornis"],
                    "fish": [ "abalone", "Alaska pollock", "American lobster", "American shad", "anchovy",  "Arctic char", "Atlantic Ocean perch", "Atlantic mackerel", "Atlantic salmon", "Chilean sea bass", "Chinese white shrimp", "cod"],
                "weather": ["sunny day", "rainy day", "cloudy day",],

 }

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

print(grammar.flatten("#start#"))
print(grammar.flatten("#origin#"))