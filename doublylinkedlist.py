class linkedlist:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
    def insert(self,nodedata):
        print("Will do it in sometime\n")
    def printing(self):
        node = self
        while node is not None:
            print(node.data)
            node = node.next
    def deletion(self,nodedata):
        nodes = self
        while nodes is not None:
            if nodes.data == nodedata:
                nodes.prev.next = nodes.next 
                nodes.next.prev = nodes.prev
            nodes = nodes.next



x = linkedlist("Data1")
y = linkedlist("Data2")
z = linkedlist("Data3")
w = linkedlist("Data4")

x.next = y
y.prev = x
y.next = z
z.prev = y
z.next = w
w.prev = z

x.printing()
x.deletion("Data2")
print("After Deletion\n")
x.printing()
