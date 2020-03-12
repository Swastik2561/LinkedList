class linkedlist:
    def __init__(self,nodevalue):
        self.nodevalue = nodevalue
        self.nextnode = None
    def printing(self):
        printvalue = self
        while printvalue is not None:
            print(printvalue.nodevalue)
            printvalue = printvalue.nextnode
    def deletion(self,deletenode):
        c = 0
        node = self
        while node is not None:
            if node.nodevalue == deletenode:
                print("Node to be deleted Found\n")
                prevnode.nextnode = node.nextnode
                c = 1
            prevnode = node
            node = node.nextnode
        if c == 0:
            print("Node Not Found\n")


x = linkedlist("Value")
y = linkedlist("Value2")
z = linkedlist("Value3")
w = linkedlist("Value4")
v = linkedlist("Value5")

x.nextnode = y
y.nextnode = z
z.nextnode = w
w.nextnode = v

x.printing()

x.deletion("Value3")
print("After Deletion\n")
x.printing()
