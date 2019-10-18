#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rand;

while True:
    sectionInput, start, end, step, numProbs = input("Enter a section title and 4 numbers, commas in between all inputs, or Q to quit: ").split(",")
    
    if sectionInput == 'q' or sectionInput == 'Q':
        break
    else:
        start1 = int(start)
        end1 = int(end)
        step1 = int(step)
        numProbs1 = int(numProbs)
        
        print(sectionInput)
        print (sorted(rand.sample(range(start1,end1,step1), numProbs1)), end=" ")
        print()


# In[ ]:




