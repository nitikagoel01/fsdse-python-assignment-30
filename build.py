
def solution(d1, d2):
    d3 ={}
    for x,y in d1.items():
        if x in d2.keys():
            d3[x]=d1[x]+d2[x]
        else:
            d3[x]=d1[x]
    for x,y in d2.items():
        if x not in d1.keys():
            d3[x]=d2[x]
    return (d3)
