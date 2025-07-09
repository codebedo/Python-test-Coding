word1 = "flower"
word2 = "flow"


for i in range(len(word1), len(word2)):
    print(f"{word1[i]} vs {word2[i]}")
    if word1[i] != word2[i]:
        print("Farkli karakter bulundu!")
        break