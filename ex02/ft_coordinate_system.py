import math

PROMPT = "Enter new coordinates as floats in format 'x,y,z': "


def get_player_pos() -> tuple[float, float, float]:
    """Ask the user for x,y,z until a valid triplet is given.

    Returns a tuple (x, y, z) of floats.
    """
    while True:
        parts = input(PROMPT).split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []
        for part in parts:
            value = part.strip()
            try:
                coords.append(float(value))
            except ValueError as error:
                print(f"Error on parameter '{value}': {error}")
                break

        if len(coords) == 3:
            return (coords[0], coords[1], coords[2])


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")
pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

dist_to_center = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
print(f"Distance to center: {round(dist_to_center, 4)}")

print("\nGet a second set of coordinates")
pos2 = get_player_pos()

dx = pos2[0] - pos1[0]
dy = pos2[1] - pos1[1]
dz = pos2[2] - pos1[2]
dist_between = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

print(f"Distance between the 2 sets of coordinates: "
      f"{round(dist_between, 4)}")
