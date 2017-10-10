# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 13:15:37 2017

@author: User
"""
"""this logic is not working"""
List=[12,24,35,24,88,120,155,88,120,155]
length = len(List)
for x in range(0,length):
    for j in range(x+1,length):
        if (List[x]==List[j]):
            List.remove(List[j])
        
    print List
    


#List=[12,24,35,24,88,120,155,88,120,155]
#newList=[]
#
#for items in List:
#    if items not in newList:
#        newList.append(items)
#        
#    print newList

        
            
        
          