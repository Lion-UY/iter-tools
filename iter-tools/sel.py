class Sel:
    cmp = None
    bst_indx: int = 0
    cur_indx: int = 0
    bst_val = None

    def __init__(self, cmp):
        self.cmp = cmp

    def update(self, val):
        if self.bst_val == None:
            self.bst_val = val
        else:
            if self.cmp(val, self.bst_val):
                self.bst_val = val
                self.bst_indx = self.cur_indx
        self.cur_indx += 1
    
    def bstindx(self):
        return self.bst_indx
    
    def bstval(self):
        return self.bst_val


def cmp(x, y):
    return x > y

max = Sel(cmp)
min = Sel(lambda x,y: x < y)

max.update(2)
min.update(2)

max.update(3)
min.update(3)

max.update(-1)
min.update(-1)

print(max.bstval())
print(max.bstindx())

print(min.bstval())
print(min.bstindx())

lambda x: x+1 # anonymous function / lambda function

def foo(x):
    return x+1




cmp