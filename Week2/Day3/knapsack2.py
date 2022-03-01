import fractions
from signal import valid_signals

class ItemValue:

    def __init__(self,wt,val,ind):
        self.wt = wt
        self.val = val
        self.ind =  ind
        self.ratio = val // wt
    
    def __lt__(self,other):
        return self.ratio < other.ratio
        

class FractionalKnapsack:

    @staticmethod
    def getMaxValue(wt,val,capcity):

        iVal = []

        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i],val[i],i))

        iVal.sort(reverse=True)

        #print(iVal)
        totalValue = 0

        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)

            if capcity - curWt >= 0:
                capcity -=curWt
                totalValue +=curVal
            else:
                fraction = capcity /curWt
                totalValue +=  curVal *fraction
                capcity = int(capcity - (curWt *fraction))
                break
        return totalValue



if __name__== "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    maxVal = FractionalKnapsack.getMaxValue(wt,val,capacity)
    print("Maximum value in Knapsack =", maxVal)