import sys



def Encapsulation(word):
	
    keepWord = len(word)
    keepIndex = []
    keepNewIndex = []

    key = input('What key : ')
    wordKey = ''
    wordEncap = ""
    keepWordIndex = []


    listWord = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for i in range(keepWord):
        if count < len(key):
            wordKey = wordKey + key[count]
            count = count + 1
        else:
            count = 0
            wordKey = wordKey + key[count]
            count = count + 1

    print('Encap : ', wordKey)

    for i in range(len(word)): #keep index to encap
        for j in range(len(listWord)):
            if word[i] == listWord[j] :
                keepWordIndex.append(j)
                
    #print(keepWordIndex)

    for i in range(len(wordKey)):
        for j in range(len(listWord)):
            if wordKey[i] == listWord[j]:
                keepIndex.append(j)
                

    for k in range(len(keepIndex)):
        keepIndex[k] = keepIndex[k] + 1 #shift ถูกตำแหน่ง
        keepWordIndex[k] = keepIndex[k] + keepWordIndex[k] #Index save word input + Index save word key
        if keepWordIndex[k] > 26 :
            keepWordIndex[k] = keepWordIndex[k] - 26
            wordEncap = wordEncap + listWord[keepWordIndex[k]]
            
        else:
            wordEncap = wordEncap + listWord[keepWordIndex[k]]
            
        
        

    print('Encapsulation word : ', wordEncap)

    checkDecap = input('You need to see Originel word ? [True/False] : ')
	
    if ((checkDecap == 'True') or (checkDecap == 'true')) :
	    Decapsulation(listWord, keepIndex, keepNewIndex, keepWord, keepWordIndex)

    elif ((checkDecap == 'False') or (checkDecap == 'false')) :
	    print('Good bye')
	    sys.exit()
	
	
	
def Decapsulation(listWord, keepIndex, keepNewIndex, keepWord, keepWordIndex):

    wordDencap = ''


    for i in range(len(keepIndex)):
        keepWordIndex[i] = keepWordIndex[i] + 26
        keepWordIndex[i] = keepWordIndex[i] - keepIndex[i]
        if keepWordIndex[i] > 26 :
            keepWordIndex[i] = keepWordIndex[i] - 26
        else:
            keepWordIndex[i]
            
        wordDencap = wordDencap + listWord[keepWordIndex[i]]
        

    print('Decapsulation : ', wordDencap)
    
            


    
        
        
    
                
                





Encapsulation(input('What word ? : '))

