"""
Game Rules:
- You're given a target word
- Try to guess words that are semantically similar
- The game shows you how close your guess is (similarity score)
- Get 3 words with similarity above the mode-dependent threshold to win!
"""

import spacy
import random

# Load spaCy model with word vectors
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    print("Please install the large English model:")
    exit()


class WordVectorGame:
    def __init__(self):
        self.target_words = [
            "ocean", "mountain", "forest", "desert", "river",
            "happiness", "anger", "love", "fear", "joy",
            "computer", "phone", "internet", "robot", "technology",
            "pizza", "burger", "pasta", "sushi", "salad"
        ]

        self.target = None
        self.target_vector = None
        self.guesses = []
        self.successful_guesses = 0

        # POS modes and corresponding tags
        self.pos_modes = {
            "nouns": {"NOUN"},
            "verbs": {"VERB"},
            "adjectives": {"ADJ"}
        }

        # Mode-specific similarity thresholds
        self.mode_thresholds = {
            "nouns": 0.5,
            "verbs": 0.4,
            "adjectives": 0.3
        }

        self.current_mode = None

    def start_game(self):
        """Start a new game with a random target word"""
        self.target = random.choice(self.target_words)
        self.target_vector = nlp(self.target)[0]
        self.guesses = []
        self.successful_guesses = 0

        self.current_mode = random.choice(list(self.pos_modes.keys()))
        current_threshold = self.mode_thresholds[self.current_mode]

        print("\n" + "=" * 50)
        print("WORD VECTOR ASSOCIATION GAME")
        print("=" * 50)
        print(f"\nTarget word: {self.target.upper()}")
        print("Find 3 words similar to the target!")
        print(
            f"(Similarity score > {current_threshold:.2f} "
            f"counts as a match in {self.current_mode[:-1]} mode.)"
        )
        print(f"ONLY {self.current_mode.upper()} allowed this round!")
        print("Type 'quit' to exit or 'new' for a new word\n")

    def calculate_similarity(self, guess_token):
        """Calculate similarity between guess and target using word vectors"""
        if not self.target_vector.has_vector or not guess_token.has_vector:
            return None

        similarity = self.target_vector.similarity(guess_token)
        return similarity

    def give_feedback(self, similarity):
        """
        Feedback scales relative to the active mode's threshold:
        - >= threshold + 0.2  -> VERY HOT
        - >= threshold        -> MATCH
        - >= threshold - 0.1  -> Warm
        - >= 0.1              -> Cold
        - else                -> Freezing
        """
        threshold = self.mode_thresholds[self.current_mode]

        if similarity >= threshold + 0.2:
            return "🔥 VERY HOT! Extremely close!"
        elif similarity >= threshold:
            return "✅ MATCH! That's similar enough!"
        elif similarity >= threshold - 0.1:
            return "🌡️ Warm... getting there!"
        elif similarity >= 0.1:
            return "❄️ Cold... not very similar"
        else:
            return "🧊 Freezing! Very different"

    def show_top_guesses(self):
        if not self.guesses:
            return

        sorted_guesses = sorted(self.guesses, key=lambda x: x[1], reverse=True)
        print("\n📊 Your closest guesses so far:")
        for i, (word, score) in enumerate(sorted_guesses[:3], 1):
            print(f"  {i}. {word}: {score:.3f}")

    def play_round(self, guess):
        guess = guess.lower().strip()

        if guess == self.target:
            print("That is the target word itself. Try another.")
            return True

        guess_doc = nlp(guess)

        # Get first alphabetical token
        main_token = None
        for token in guess_doc:
            if token.is_alpha:
                main_token = token
                break

        if main_token is None:
            print("I could not understand that guess. Enter a single word.")
            return True

        # POS constraint
        allowed_tags = self.pos_modes[self.current_mode]
        if main_token.pos_ not in allowed_tags:
            print(
                f"This round you must guess {self.current_mode[:-1]}s "
                f"(allowed POS: {allowed_tags}). "
                f"Your word '{main_token.text}' is tagged as '{main_token.pos_}'."
            )
            return True

        similarity = self.calculate_similarity(main_token)

        if similarity is None:
            print("Word not recognized or no vector available. Try again.")
            return True

        self.guesses.append((guess, similarity))

        feedback = self.give_feedback(similarity)
        print(f"\n{feedback}")
        print(f"Similarity score: {similarity:.3f}")

        # Use mode-specific threshold for counting matches
        threshold = self.mode_thresholds[self.current_mode]
        if similarity >= threshold:
            self.successful_guesses += 1
            print(f"Matches found: {self.successful_guesses}/3")

            if self.successful_guesses >= 3:
                print("\n" + "=" * 50)
                print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
                print("=" * 50)
                self.show_top_guesses()
                return False

        return True

    def run(self):
        self.start_game()

        while True:
            try:
                user_input = input("\nYour guess: ").strip().lower()

                if user_input == 'quit':
                    print("\nThanks for playing!")
                    break

                if user_input == 'new':
                    self.start_game()
                    continue

                if user_input == 'hint':
                    self.show_top_guesses()
                    continue

                if not user_input:
                    continue

                continue_game = self.play_round(user_input)

                if not continue_game:
                    again = input("Play again? (yes/no): ").strip().lower()
                    if again in ["yes", "y"]:
                        self.start_game()
                    else:
                        print("\nThanks for playing!")
                        break

            except KeyboardInterrupt:
                print("\nGame interrupted. Bye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue


if __name__ == "__main__":
    game = WordVectorGame()
    game.run()
