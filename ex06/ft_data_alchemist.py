import random

MIN_SCORE = 50
MAX_SCORE = 1000

players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
           "kevin", "Liam"]

all_capitalized = [name.capitalize() for name in players]
already_capitalized = [name for name in players if name.istitle()]

scores = {name: random.randint(MIN_SCORE, MAX_SCORE)
          for name in all_capitalized}
average = sum(scores.values()) / len(scores)
high_scores = {name: score for name, score in scores.items()
               if score > average}

print("=== Game Data Alchemist ===")

print(f"\nInitial list of players: {players}")
print(f"New list with all names capitalized: {all_capitalized}")
print(f"New list of capitalized names only: {already_capitalized}")

print(f"\nScore dict: {scores}")
print(f"Score average is {round(average, 2)}")
print(f"High scores: {high_scores}")
