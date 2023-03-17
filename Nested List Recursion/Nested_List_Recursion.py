
def recursiveListfunct(list1):
    '''A function that prints all the values of a list accounting for all the nested lists it may have inside it using recursion
    Expected input: A list with any amount of nested lists
    Expected output: prints all values on their own line
    '''
    for i in list1:
        if type(i)!=list:
            print(i)
        else:
            recursiveListfunct(i)

s=[[1,2],1,3,[5,6,7],[9,10,[11,13]]]
print(recursiveListfunct.__doc__)
recursiveListfunct(s)

