from anytree import Node, RenderTree
#from anytree.exporter import DotExporter
#import graphviz

##############################################
P1 = Node("P1")
P2 = Node("P2", parent=P1)
P3 = Node("P3", parent=P1)
P4 = Node("P4", parent=P2)
P5 = Node("P5", parent=P2)
P6 = Node("P6", parent=P3)
P7 = Node("P7", parent=P3)
P8 = Node("P8", parent=P4)
P9 = Node("P9", parent=P4)
P10 = Node("P10", parent=P5)
P11 = Node("P11", parent=P5)
P12 = Node("P12", parent=P6)
P13 = Node("P13", parent=P6)
P14 = Node("P14", parent=P7)
P15 = Node("P15", parent=P7)
P16 = Node("P16", parent=P8)
P17 = Node("P17", parent=P8)
P18 = Node("P18", parent=P9)
P19 = Node("P19", parent=P9)
P20 = Node("P20", parent=P10)
P21 = Node("P21", parent=P10)
P22 = Node("P22", parent=P11)
P23 = Node("P23", parent=P11)
P24 = Node("P24", parent=P12)
P25 = Node("P25", parent=P12)
P26 = Node("P26", parent=P13)
P27 = Node("P27", parent=P13)
P28 = Node("P28", parent=P14)
P29 = Node("P29", parent=P14)
P30 = Node("P30", parent=P15)
P31 = Node("P31", parent=P15)

for pre, fill, node in RenderTree(P1):
    print("%s%s" % (pre, node.name))



