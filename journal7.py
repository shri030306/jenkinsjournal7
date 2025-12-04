import sys


if len(sys.argv) > 1:
    print("User provided input values:")
    scores = list(map(int, sys.argv[1:]))
else:
    print("No input given - using default scores:")
    scores = [50, 75, 90, 85, 60]   


total = sum(scores)
average = total / len(scores)



print("Scores:", scores)
print("Sum of scores:", total)
print("Average score:", average)