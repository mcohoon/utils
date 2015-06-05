import types

mylist = [0, 9279842, "another cat", 'z', 948.989898998]

def delete(mylist):
    print "Original list: ", mylist
    for x in range(len(mylist)):
        item = mylist[x]
        #print type(item)
        if type(item) is types.FloatType: 
            del mylist[x]
    print "Modified List: ", mylist 

delete(mylist)
