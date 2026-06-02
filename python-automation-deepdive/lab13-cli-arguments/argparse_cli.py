import argparse

# Create parser
parser = argparse.ArgumentParser(description="CLI Arguments Demo")

# Positional argument
parser.add_argument("name", type=str, help="Name of the user")

# Optional argument
parser.add_argument("--age", type=int, default=25, help="Age of the user")

# Parse arguments
args = parser.parse_args()

print("👤 Name:", args.name)
print("🎂 Age:", args.age)
