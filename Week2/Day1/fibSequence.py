class Fibonacci:
    def __init__(self):
        self.res = [0,1]
    
    def __call__(self, n):
        if not (isinstance(n,int) and n>=0):
            raise ValueError(f'Only positive integer number expected"{n}"')
        
        if n < len(self.res):
            return self.res[n]
        else: 
            fibNumber = self(n-1) + self(n-2)
            self.res.append(fibNumber)

        return self.res[n]
