word_a = "foash"
word_b = "fish"

len_a = len(word_a)
len_b = len(word_b)

table = [[0 for m in range(len_a + 1)]for n in range(len_b + 1)]

for i in range(1,len_b + 1):
    for j in range(1,len_a + 1):
        if word_b[i-1] == word_a[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j],table[i][j-1])


print (table)