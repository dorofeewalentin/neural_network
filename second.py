file = open('big_data.txt', 'r')
data_list = file.readline()
file.close()
splitted_data = data_list.split(', ')
splitted_data.pop()
#print(splitted_data)
letter_counter = {}
for word in splitted_data:
    #print(word)
    if word[0] in letter_counter:
        letter_counter[word[0]] += 1
    else:
        letter_counter[word[0]] = 1
print(letter_counter)
