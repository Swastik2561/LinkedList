class linkedlist:
    def __init__(self,datavalue):
        self.datavalue = datavalue
        self.nextnode = None
    def insert_last(self,insert_node):
        nodevalue = self
        while nodevalue.nextnode is not None:
            nodevalue = nodevalue.nextnode
        nodevalue.nextnode = insert_node
        insert_node.nextnode = None
    def printing(self):
        printvalue = self
        while printvalue is not None:
            print(printvalue.datavalue)
            printvalue = printvalue.nextnode


x = linkedlist("Swastik")
y = linkedlist("Binjola")
z = linkedlist("Is good")

x.insert_last(y)
x.insert_last(z)

x.printing()
