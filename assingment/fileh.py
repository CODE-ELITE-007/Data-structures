file1=open('conv.txt','r')
convo= file1.read()
remove_words=[',','.','?',"!","…","’s"]
for i in remove_words:
    convo=convo.replace(i," ")
    
convo=convo.split("\n")
convo=[x for x in convo if x not in " "]
char_talk={}
for i in convo:
    j,k=i.split(":")
    j,k=j.strip(),k.strip()+" "
    if j not in char_talk.keys():
        char_talk[j]=k
    else:
        char_talk[j]+=k
   
   
print(f'The no of unique characters is {len(list(char_talk.keys()))}')   

for i, j in char_talk.items():
   file1=open(i,'w')
   j=list(set(j.split(" ")))
   for words in j :
      file1.write(words+"\n")
   file1.close()
   

   
