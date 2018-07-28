class daynames:
    def __init__(self, dataval = None):
        self.dataval = dataval;
        self.nextval = None


e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('sun')


e1.nextval = e2
e3.nextval = e2


thisvalue = e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval
