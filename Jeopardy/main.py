import random
import time
class JeopardyGame:
    def __init__(self):
        self.categories = {}
        self.players = []
        self.current_player = None

    def add_category(self, category, questions):
        self.categories[category] = questions

    def add_player(self, player):
        self.players.append(player)

    def select_question(self):
        print("\nAvailable categories:")
        for category in self.categories.keys():
            print(category)

        category = input("\nWhich category would you like to choose from? (Enter the category name): ")

        if category not in self.categories:
            print("Invalid category.")
            return None, None

        print(f"\nAvailable questions in {category}:")
        available_questions = self.categories[category]
        for question in available_questions:
            print(f"Value: {question['value']}, Difficulty: {question['difficulty']}")

        difficulty_choice = input("\nSelect difficulty (easy/medium/hard): ").lower()
        filtered_questions = [q for q in available_questions if q['difficulty'] == difficulty_choice]
        if not filtered_questions:
            print("No question available for selected category and difficulty.")
            return None, None

        question = random.choice(filtered_questions)
        available_questions.remove(question)
        self.categories[category] = available_questions
        return category, question

    def display_board(self):
        print("\nCategories:")
        for category, _ in self.categories.items():
            print(category)
        print("\nPlayers:")
        for player in self.players:
            print(player.name + ": $" + str(player.score))

    def play(self):
        print("Welcome to Jeopardy!")
        for category, questions in self.categories.items():
            print(f"\nCategory: {category}")
            for question in questions:
                print(f"Value: {question['value']}, Difficulty: {question['difficulty']}")

        while True:
            for player in self.players:
                self.current_player = player
                self.display_board()
                category, question = self.select_question()
                if category is None:
                    continue

                print(f"\n{self.current_player.name}, choose a question from {category}: ")
                print(question["prompt"])
                answer = input("Your answer: ")
                if answer.lower() == question["answer"].lower():
                    print("Correct!")
                    self.current_player.score += question["value"]
                else:
                    print("Incorrect!")

                if all(player.score > 0 for player in self.players):
                    lowest_score = min(player.score for player in self.players)
                    if self.current_player.score == lowest_score:
                        choice = input("Double or nothing? (yes/no): ")
                        if choice.lower() == "yes":
                            self.current_player.score *= 2

                if input("Continue? (yes/no): ").lower() == "no":
                    return


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


def main():
    game = JeopardyGame()

    categories = {
        "Maths": [
            {"value": 100, "prompt": "What is 12 divided by 3", "answer": "4", "difficulty": "easy"},
            {"value": 200, "prompt": "A farmer has 27 eggs. He wants to pack them into cartons, each containing 6 eggs. How many cartons can he fill?", "answer": "4.5", "difficulty": "easy"},
            {"value": 300, "prompt": "A garden is 24 meters long and 18 meters wide. What is the area of the garden?", "answer": "432 squared cm", "difficulty": "medium"},
            {"value": 400, "prompt": "What is the value of pi (to 3 decimal places)?", "answer": "3.141", "difficulty": "medium"},
            {"value": 500, "prompt": "If a recipe calls for 3/4 cup of sugar and you want to make 5 times the amount, how much sugar do you need in total?", "answer": "3 3/4", "difficulty": "hard"}
        ],
        "History": [
            {"value": 100, "prompt": "Who was the first president of the United States?", "answer": "George Washington", "difficulty": "easy"},
            {"value": 200, "prompt": "What ancient civilization built the pyramids in Egypt?", "answer": "The ancient egyptians", "difficulty": "easy"},
            {"value": 300, "prompt": "Who is the king of England?", "answer": "King Charles", "difficulty": "medium"},
            {"value": 400, "prompt": "What was the purpose of the Great Wall of China?", "answer": "To protect China from invaders.", "difficulty": "medium"},
            {"value": 500, "prompt": "What year was the Magna Carta signed?", "answer": "1215", "difficulty": "hard"}
        ],
        "Sports": [
            {"value": 100, "prompt": "Which country won the 2022 FIFA World Cup?", "answer": "Argentina", "difficulty": "easy"},
            {"value": 200, "prompt": "In basketball, how many points is a three-point shot worth?", "answer": "Three Points", "difficulty": "easy"},
            {"value": 300, "prompt": "What sport involves throwing a disc to a teammate with the objective of advancing the disc down the field to score points?", "answer": "Ultimate frisbee", "difficulty": "medium"},
            {"value": 400, "prompt": "In which sport would you perform a 'slam dunk'?", "answer": "Basketball", "difficulty": "medium"},
            {"value": 500, "prompt": "In baseball, how many strikes does a batter get before they are out?", "answer": "Three strikes", "difficulty": "hard"}
        ],
        "Famous Landmarks": [
            {"value": 100, "prompt": "Which ancient landmark of the world is located in Giza, Egypt?", "answer": "Great Pyramid of Giza", "difficulty": "easy"},
            {"value": 200, "prompt": "Which architectural building is located in India?", "answer": "Taj Mahal", "difficulty": "easy"},
            {"value": 300, "prompt": "Which landmark in Paris, France?", "answer": "Robert Plant", "difficulty": "medium"},
            {"value": 400, "prompt": "What is the name of the famous tower in Pisa, Italy, known for its unintentional tilt?", "answer": "Leaning tower of Pisa", "difficulty": "medium"},
            {"value": 500, "prompt": "Which famous bridge spans the Golden Gate Strait, connecting San Francisco to Marin County in California, USA?", "answer": "Golden state bridge", "difficulty": "hard"}
        ],
        "Food/Drinks": [
            {"value": 100, "prompt": "What is the primary ingredient in guacamole?", "answer": "Avocado", "difficulty": "easy"},
            {"value": 200, "prompt": "What type of pasta is shaped like small rice grains?", "answer": "Orzo", "difficulty": "easy"},
            {"value": 300, "prompt": "What is the main ingredient in a traditional Greek salad?", "answer": "Feta cheese", "difficulty": "medium"},
            {"value": 400, "prompt": "What is the national dish of Spain?", "answer": "Paella", "difficulty": "medium"},
            {"value": 500, "prompt": "Which fruit is known as the 'king of fruits'?", "answer": "Durian", "difficulty": "hard"}
        ]
    }

    # Add categories to the game with pauses in between
    import time
    for category, questions in categories.items():
        game.add_category(category, questions)
        time.sleep(1)  # Pause after adding each category

    player_name = input("What is your name? ")
    player1 = Player(player_name)

    player2_choice = input("Who is Player 2? (Enter 'bot' for a bot player): ")
    if player2_choice.lower() == "bot":
        player2 = Player("Bot")
    else:
        player2_name = input("Enter Player 2's name: ")
        player2 = Player(player2_name)

    game.add_player(player1)
    game.add_player(player2)

    game.play()

if __name__ == "__main__":
    main()
