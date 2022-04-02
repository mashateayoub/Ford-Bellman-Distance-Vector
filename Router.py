
# Classe Router qui simule un Routeur avec une table de routage 
class Router :
    def __init__(self, RoutingTable): 
        self.RoutingTable=RoutingTable
    
    def Ford_Bellman(self,R, DistVect) :
        for i in range(0,len(DistVect)) :
            if DistVect[i] not in self.RoutingTable:
                update=False
                add=True
                for j in range(0,len(self.RoutingTable)):
                    if DistVect[i]["Dest"]==self.RoutingTable[j]["Dest"] :
                        add=False
                        if DistVect[i]["Dist"]<self.RoutingTable[j]["Dist"] :
                            update=True 
                            To_update=j
                
                if add:
                    self.RoutingTable.append(DistVect[i])
                elif update:
                    self.RoutingTable[To_update]["Dist"]=DistVect[i]["Dist"]
                    self.RoutingTable[To_update]["Route"]=R
        print(self.RoutingTable)



if __name__=="__main__":
    RT=[ 
        {
            'Dest': "reseau 2",
            'Dist': 2,
            'Route': "R3"
        },
        {
            'Dest': "reseau 3",
            'Dist': 6,
            'Route': "R6"
       }
       ]

    DV=[ 
        {
            'Dest': "reseau 8",
            'Dist': 2,
            'Route': "R6"
        },
        {
            'Dest': "reseau 3",
            'Dist': 4,
            'Route': "R6"
       }
    ]
        

    test=Router(RT)
    test.Ford_Bellman("R1",DV)
