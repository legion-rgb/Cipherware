#atbash
def atbash_decode(text):
    word=[]
    for c in text:
        if c.isupper():
            total = ord('A') + ord('Z')
            s = chr(total-ord(c))
            word.append(s)
            words = ''.join(word)
        elif c ==' ':
            word.append(' ')
            words = ''.join(word)
        else:
            t = ord('a') + ord('z')
            q = chr(t-ord(c))
            word.append(q)
            words = ''.join(word)
    return words

#rot13
def rot13_decode(text):
    word=[]
    for i in text:
        if i.isupper():
            c_index = ord(i) - ord("A")
            new_index = (c_index - 13) % 26
            s = chr(new_index + ord("A"))
            word.append(s)
            words = ''.join(word)
        elif i ==' ':
            word.append(' ')
            words = ''.join(word)
        else:
            c_index = ord(i) - ord("a")
            new_index = (c_index - 13) % 26
            q = chr(new_index + ord("a"))
            word.append(q)
            words = ''.join(word)
    return words
#caesar
def caesar_decode(text,shift):
    word=[]
    for i in text:
        if i.isupper():
            c_index = ord(i) - ord("A")
            new_index = (c_index - shift) % 26
            q = chr(new_index + ord("A"))
            word.append(q)
            words = ''.join(word)
        elif i ==' ':
            word.append(' ')
            words = ''.join(word)
        else:
            c_index = ord(i) - ord("a")
            new_index = (c_index - shift) % 26
            q = chr(new_index + ord("a"))
            word.append(q)
            words = ''.join(word)

    return words

#railfence
def railfence_decode(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if ((rail[i][j] == '*') and (index < len(text))):
                rail[i][j] = text[index]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(text)):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

#baconian
def baconian_decode(message):
    lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
              'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
              'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
              'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
              'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
    dec = ''
    i = 0
    while True :
        if(i < len(message)-4):
            substr = message[i:i + 5]
            if(substr[0] != ' '):
                dec += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5
            else:
                dec += ' '
                i += 1
        else:
            break
    return dec

