import random

ACHIEVEMENTS = [
    "Iron",
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Emerald",
    "Diamond",
    "Master",
    "Grandmaster",
    "Challenger",
    "Professional",
    "Elite",
    "Hunter",
    "Lane Domination",
    "EasterEgg",
]


def gen_player_achievements() -> set[str]:
    """Pick a random amount of achievements and return them as a set."""
    amount = random.randint(7, 11)
    return set(random.sample(ACHIEVEMENTS, amount))


tom = gen_player_achievements()
mellanie = gen_player_achievements()
lukas = gen_player_achievements()
luca = gen_player_achievements()

all_catalog = set(ACHIEVEMENTS)
all_distinct = tom.union(mellanie, lukas, luca)
common = tom.intersection(mellanie, lukas, luca)

print("=== Achievement Tracker System ===")

print(f"\nPlayer Tom: {tom}")
print(f"Player Mellanie: {mellanie}")
print(f"Player Lukas: {lukas}")
print(f"Player Luca: {luca}")

print(f"\nAll distinct achievements: {all_distinct}")

print(f"\nCommon achievements: {common}")

print(f"\nOnly Tom has: {tom.difference(mellanie, lukas, luca)}")
print(f"Only Mellanie has: {mellanie.difference(tom, lukas, luca)}")
print(f"Only Lukas has: {lukas.difference(tom, mellanie, luca)}")
print(f"Only Luca has: {luca.difference(tom, mellanie, lukas)}")

print(f"\nTom is missing: {all_catalog.difference(tom)}")
print(f"Mellanie is missing: {all_catalog.difference(mellanie)}")
print(f"Lukas is missing: {all_catalog.difference(lukas)}")
print(f"Luca is missing: {all_catalog.difference(luca)}")
