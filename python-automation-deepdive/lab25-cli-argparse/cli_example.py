import argparse

# Task 2: Initialize ArgumentParser
parser = argparse.ArgumentParser(description="A simple CLI example using argparse")

# Adding arguments
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('--file', type=str, help='File path to process')

# Task 3: Enhancements
parser.add_argument('--level', type=int, choices=[1, 2, 3], help='Set operation level')
parser.add_argument('--timeout', type=int, default=30, help='Timeout duration in seconds')

# Parse arguments
args = parser.parse_args()

# Logic implementation
if args.verbose:
    print("🔊 Verbose mode is activated.")

if args.file:
    print(f"📄 Processing file: {args.file}")

if args.level:
    print(f"⚙️ Operation level set to: {args.level}")

print(f"⏱ Timeout is set to: {args.timeout} seconds")
