#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
list_ = []
n = random.randint(1,10000)
list_.append(n)
def mergeSort(list_):
    print("Splitting ",list_)
    if len(list_)>1:
        mid = len(list_)//2
        lefthalf = list_[:mid]
        righthalf = list_[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",list_)


mergeSort(list_)
print(list_)


# In[ ]:





# In[ ]:




