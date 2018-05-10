#Project Euler #22
# Names scores
with open('p022_names.txt', 'r') as fi:
    raw_names = fi.read().replace('"', '').split(',')
scores = [i * sum([ord(c)-64 for c in name]) for i, name in enumerate(sorted(raw_names), 1)]
print(sum(scores))