import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")

arg_count = len(sys.argv) - 1

if arg_count == 0:
    print("No arguments provided!")
else:
    print(f"Arguments received: {arg_count}")
    index = 1
    for arg in sys.argv[1:]:
        print(f"Argument {index}: {arg}")
        index += 1

print(f"Total arguments: {len(sys.argv)}")
