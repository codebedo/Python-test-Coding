strs = ["flower", "flow", "flight"]
prefix = ""

for chars in zip(*strs):
    if all(harf == chars[0] for harf in chars):
        prefix += chars[0]
    else:
        break


print(prefix)