# The question is more of a reading comprehention but is easier than you think,
# couldn't solve it during the context but a little bit of scribbling makes it a lot easier.
# a-We have to start withdrawing from the largest denominations
# b-We don't actually need a complex logic, its pretty straightforward tbh!
class ATM:
    def __init__(self):
        self.cash = [0 for i in range(5)]
        self.value = [20,50,100,200,500]

    def deposit(self, dep: List[int]) -> None:
        for i in range(len(dep)):
            self.cash[i] += dep[i] 

    def withdraw(self, amount: int) -> List[int]:
        res = [0 for i in range(5)]
        for i in range(4,-1,-1):
            cash = self.cash[i]
            value = self.value[i]
            #no of notes that can be used can never be more than 
            #the number of notes remaining in the 
            #atm machine of that particular denomination
            noOfNotes = min(cash,amount//value)
            res[i] = noOfNotes
            #decrease the amount according to the no. of notes of that
            #denomination withdrawed
            amount -= (noOfNotes*value)
        if amount == 0:
            #we dont actually take out amount from the cash
            #using the deposit function we withdraw the amount using neg vals
            self.deposit([-i for i in res])
            return res
        else:
            return [-1]