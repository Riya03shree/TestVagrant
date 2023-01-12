def solutionTable():
    # Making a dictionary of each newspaper's weekly subscription values as summation
    # Data taken from the shared table in email attachment
    tableValues={"TOI":26,"Hindu":20.5,"ET":34,"BM":10.5,"HT":18}
    return(tableValues)
    
if __name__=="__main__":
    intputValue=int(input("Enter the weekly budget/amount:"))
    sol={}
    s={}
    lst=[]
    l=set()
    Table=solutionTable()
    for x,y in Table.items():
        if y < intputValue:
            sol.update({x:y})
    for x,y in sol.items():
        if y < (intputValue/2)or y<(intputValue/2+7):
            s.update({x:y})
    for x in s.keys():
        lst.append(x)
    for i in lst:
        l.add(i)
    print(l)