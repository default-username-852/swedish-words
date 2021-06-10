f = open("ord.txt", "r")

g = open("ord2.txt", "w")

f_text = f.read().split("\n")
sorterad = sorted(f_text, key=lambda x: x.lower())
sort_text = "\n".join(sorterad)
print(sorterad[3])

g.write(sort_text)
