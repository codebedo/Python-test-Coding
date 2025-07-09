word1 = "flower"
word2 = "flow"


for i in range(min(len(word1), len(word2))):
    print(f"{word1[i]} vs {word2[i]}")
    if word1[i] != word2[i]:
        print("Farkli karakter bulundu!")
    break


word3 = "aplle"
word4 = "apricot"


for i in range(max(len(word3), len(word4))):
    print(f"{word3[i]} vs {word4[i]}")
    if word3[i] != word4[i]:
        print("What we have here")

    break