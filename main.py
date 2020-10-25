def matches_at(t, p, w):
    if len(t) < len(w):
        return False
    for i in range(len(w)):
        if w[i] != t[p + i]:
            return False
    return True


# Złożność obliczeniowa:
# czasowa: od 1 do |W | porównań znaków,
# pamięciowa: O(1).

text = "Ala ma kota"
pattern = "ma"

print(matches_at(text, 3, pattern))


################################

def report(p):
    print(f"Znaleziono na {p}")


T = "ala ma kota i tez ma pamasa"
W = "ma"
lastp = {'a': -1, 'l': -1, ' ': -1, 'm': -1, 'k': -1, 'o': -1, 't': -1, 'i': -1, 'e': -1, 'z': -1, 'p': -1, 's': -1}
for i in range(len(W)):
    lastp[W[i]] = i

p = 0
while p <= len(T) - len(W):
    if matches_at(T, p, W):
        report(p)
    p = p + len(W)
    if p < len(T):
        p = p - lastp[T[p]]
