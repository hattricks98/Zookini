from fuzzywuzzy import fuzz

jawab = "five thousand"
ANSWER = input()
Ratio = fuzz.ratio(jawab.lower(),ANSWER.lower())
print(Ratio)
