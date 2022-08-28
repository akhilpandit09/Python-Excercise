# defining function

def swaplist(newlist):
    size=len(newlist)

    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp

    return newlist

newlist=[2,6,4,6,8,9]
print(swaplist(newlist))


        