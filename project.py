def list_flatten(liste):
    eleman=len(liste)
    list_flatten=[]
    new_list=[]
    a_list=[]
    b_list=[]
    for i in range(eleman):
        a_list=liste[i]
        if type(a_list)== list:
            for j in range(len(a_list)):
                b_list=a_list[j]
                if type(b_list)==list:
                    for a in range(len(b_list)):
                        new_list=b_list[a]
                        if type(new_list)==list:
                            for b in range(len(new_list)):
                                list_flatten.append(new_list[b])
                        else:
                            list_flatten.append(new_list)
                else:
                    list_flatten.append(b_list)
        else:
            list_flatten.append(a_list)
    return list_flatten

liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(list_flatten(liste))

def list_reverse(liste):
    global reversed_list
    eleman=len(liste)
    reversed_list=[]
    a_list=[]
    for i in(range(eleman)):
        a_list=liste[i]
        if type(a_list)== list:
            a_list.reverse()
            reversed_list.append(a_list)
        else:
            reversed_list.append(a_list)
    reversed_list.reverse()
    return reversed_list
            
  
liste=[[1, 2], [3, 4], [5, 6, 7]]
new_list=list_reverse(liste)
print(new_list)



