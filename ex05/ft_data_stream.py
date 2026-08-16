import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "move", "climb", "swim", "sleep", "eat", "grab",
           "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Endless generator yielding a random (player, action) tuple."""
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    """Yield a random event out of the list until the list is empty."""
    while len(events) > 0:
        yield events.pop(random.randrange(len(events)))


print("=== Game Data Stream Processor ===")

stream = gen_event()

for index in range(1000):
    player, action = next(stream)
    print(f"Event {index}: Player {player} did action {action}")

ten_events = [next(stream) for _ in range(10)]
print(f"Built list of 10 events: {ten_events}")

for event in consume_event(ten_events):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {ten_events}")
