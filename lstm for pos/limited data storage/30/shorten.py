f = open("en-ud-tag.v2.train.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()

f = open("en-ud-tag.v2.train.txt", "w", encoding='utf-8')
for i in range(65200):
    f.write(lines[i])
f.close()



f = open("en-ud-tag.v2.dev.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()

f = open("en-ud-tag.v2.dev.txt", "w", encoding='utf-8')
for i in range(8200):
    f.write(lines[i])
f.close()