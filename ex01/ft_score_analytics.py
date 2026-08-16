import sys

print("=== Player Score Analytics ===")

valid_scores = []

for arg in sys.argv[1:]:
    try:
        valid_scores.append(int(arg))
    except ValueError:
        print(f"Invalid parameter: '{arg}'")

if len(valid_scores) == 0:
    print("No scores provided. Usage: python3 ft_score_analytics.py"
          " <score1> <score2> ...")
else:
    total = sum(valid_scores)
    high = max(valid_scores)
    low = min(valid_scores)

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(valid_scores)}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")
