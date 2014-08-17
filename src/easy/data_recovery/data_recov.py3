import sys

file = open(sys.argv[1], 'r')

for line in file:
    tokens = line.split(';')
    words = tokens[0].split()
    hints = tokens[1].split()
    ord_words = [None] * len(words) 
    unchosen_hints = list(range(1,len(words)+1))

    for i in range(len(words)-1):
        ord_words[int(hints[i])-1] = words[i]
        unchosen_hints.remove(int(hints[i]))
    # Insert missing word
    ord_words[unchosen_hints[0]-1] = words[len(words)-1]
    
    for i in range(len(ord_words)):
        print(ord_words[i], end=' ')
    print('')
    
file.close()
