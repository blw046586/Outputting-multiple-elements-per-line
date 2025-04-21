import sys

# Read all input at once and convert to integers
yearly_values = list(map(int, sys.stdin.read().split()))

# Output 4 items per line
for i in range(0, len(yearly_values), 4):
    print(yearly_values[i], yearly_values[i+1], yearly_values[i+2], yearly_values[i+3])
