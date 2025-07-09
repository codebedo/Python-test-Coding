word3 = "interview"
word4 = "internet"

j = 0
dfchar = 0

while j < min(len(word3), len(word4)):
    if word3[j] == word4[j]:
        print(f" aynı karkaterler {word3[j]} vs {word4[j]}")
    else:
        print(f"farklı karkaterler {word3[j]} ve {word4[j]}")

    j += 1

print(f"aynı karkater sözcüğü : {word4[:j]} ve {word3[:j]}")
