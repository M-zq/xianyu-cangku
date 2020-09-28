words = ''
with open('C:\\Users\\admin\\Desktop\\Walden.txt','r') as p:
    all_list = p.readlines()
    for pargam in all_list:
        words = pargam+words
words_1 = words.split()
words_2 = []
for i in words_1:
    if i not in words_2:
        words_2.append(i)
words_3 = {}
for x in words_2:
    words_3[x]= words_1.count(x)
new_dict = sorted(words_3.items(),key=lambda x:x[1],reverse= True)
for word in new_dict:
    print('{0}  {1}'.format(word[0],word[1]))