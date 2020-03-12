class linkedlist:
    def __init__(self,headvalue):
        self.headvalue = headvalue
        self.nextnode = None
    def printing(self):
        printvalue = self
        while printvalue is not None:
            print(printvalue.headvalue)
            printvalue = printvalue.nextnode

x = linkedlist("UmarAbdullah")
y = linkedlist("Amar Akbar Anthony")
z= linkedlist("Abey Aur kitna chahiye")

x.nextnode = y
y.nextnode = z

print(x.nextnode.nextnode.headvalue)

x.printing()
