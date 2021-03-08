class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing=set()
        cities=set()
        for i in paths:
            outgoing.add(list(i)[0])
            cities.add(list(i)[0])
            cities.add(list(i)[1])
        for j in cities:
            if(j not in outgoing):
                return j
        return ""
        
