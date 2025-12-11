"""
Game Rules:
- You're given a target word
- Try to guess words that are semantically similar
- The game shows you how close your guess is (similarity score)
- Get 3 words with similarity > 0.5 to win!

"""

import spacy
import random

# Load spaCy model with word vectors
# Using 'md' (medium) model which includes word vectors
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

    def start_game(self):
        """Start a new game with a random target word"""
        self.target = random.choice(self.target_words)
        self.target_vector = nlp(self.target)
        self.guesses = []
        self.successful_guesses = 0

        print("\n" + "=" * 50)
        print("🎮 WORD VECTOR ASSOCIATION GAME 🎮")
        print("=" * 50)
        print(f"\nTarget word: {self.target.upper()}")
        print("\nFind 3 words similar to the target!")
        print("(Similarity score > 0.5 counts as a match)")
        print("Type 'quit' to exit or 'new' for a new word\n")

    def calculate_similarity(self, guess):
        """Calculate similarity between guess and target using word vectors"""
        guess_vector = nlp(guess)

        # Check if both words have vectors
        if not self.target_vector.has_vector or not guess_vector.has_vector:
            return None

        # Calculate cosine similarity using spaCy's built-in method
        similarity = self.target_vector.similarity(guess_vector)
        return similarity

    def give_feedback(self, similarity):
        # Provide feedback based on similarity score
        if similarity >= 0.7:
            return "🔥 VERY HOT! Extremely close!"
        elif similarity >= 0.5:
            return "✅ MATCH! That's similar enough!"
        elif similarity >= 0.3:
            return "🌡️ Warm... getting there!"
        elif similarity >= 0.1:
            return "❄️ Cold... not very similar"
        else:
            return "🧊 Freezing! Very different"

    def show_top_guesses(self):
        # Show the top 3 closest guesses so far
        if not self.guesses:
            return

        sorted_guesses = sorted(self.guesses, key=lambda x: x[1], reverse=True)
        print("\n📊 Your closest guesses so far:")
        for i, (word, score) in enumerate(sorted_guesses[:3], 1):
            print(f"  {i}. {word}: {score:.3f}")

    def play_round(self, guess):
        # Process a single guess
        guess = guess.lower().strip()

        # Check for same word
        if guess == self.target:
            print("❌ That's the target word itself! Try something similar.")
            return True

        # Calculate similarity
        similarity = self.calculate_similarity(guess)

        if similarity is None:
            print("⚠️ Word not recognized or no vector available. Try another!")
            return True
        self.guesses.append((guess, similarity))

        # Give feedback
        feedback = self.give_feedback(similarity)
        print(f"\n{feedback}")
        print(f"Similarity score: {similarity:.3f}")

        # Check if it's a successful match
        if similarity >= 0.5:
            self.successful_guesses += 1
            print(f"✨ Matches found: {self.successful_guesses}/3")

            if self.successful_guesses >= 3:
                print("\n" + "=" * 50)
                print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
                print("=" * 50)
                self.show_top_guesses()
                return False

        return True

    def run(self):
        # Main game loop
        self.start_game()

        while True:
            try:
                user_input = input("\nYour guess: ").strip().lower()

                if user_input == 'quit':
                    print("\nThanks for playing! 👋")
                    break

                if user_input == 'new':
                    self.start_game()
                    continue

                if user_input == 'hint':
                    self.show_top_guesses()
                    continue

                if not user_input:
                    continue

                # Play the round
                continue_game = self.play_round(user_input)

                if not continue_game:
                    play_again = input("\nPlay again? (yes/no): ").strip().lower()
                    if play_again in ['yes', 'y']:
                        self.start_game()
                    else:
                        print("\nThanks for playing! 👋")
                        break

            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing! 👋")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue


# Run the game
if __name__ == "__main__":
    game = WordVectorGame()
    game.run()