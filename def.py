from collections import OrderedDict

class PoSetObject:
    struture = []
    node_hash = {}
    stack = []
    count = None
    C = None
    def __init__(self, size):
        self.count = [0] * size
        for i in range(0, size):
            self.struture.append([0] * size)

    def create_node_index_hash(self):
        i = 0
        for key in self.C.keys():
            self.node_hash[key] = i
            i+=1
        self.node_hash[self.C.items()[-1][-1][0]] = i

    def generateSet(self, node):
        self.stack.append(node)
        if node not in self.C:
            last = self.stack.pop()
            for n in self.stack:
                if self.struture[self.node_hash[n]][self.node_hash[last]] != 1:
                    self.count[self.node_hash[n]] += 1
                    self.struture[self.node_hash[n]][self.node_hash[last]] = 1
            return
        layer = self.C[node]
        for new_node in layer:
            self.generateSet(new_node)
        last = self.stack.pop()
        for n in self.stack:
                if self.struture[self.node_hash[n]][self.node_hash[last]] != 1:
                    self.count[self.node_hash[n]] += 1
                    self.struture[self.node_hash[n]][self.node_hash[last]] = 1

    def init(self, C):
        self.C = C
        self.create_node_index_hash()
        start_node = self.C.items()[0][0]
        self.generateSet(start_node)

    def DelMin(self, x):
        i =  self.node_hash[x]
        for index in range(0, i):
            if self.struture[index][i] == 1:
                self.struture[index][i] = 0
                self.count[index] -= 1
        for index in range(i+1, len(self.struture[i])):
            if self.struture[i][index] == 1:
                self.count[i] -= 1
                self.struture[i][index] = 0

    def ListMin(self):
        minimum = -1
        nodes = []
        for i in range(0, len(self.struture[0])):
            if self.count == 0:
                continue
            if self.count[i] > minimum:
                minimum = self.count[i]
                nodes = []
                nodes.append(i)
                continue
            if self.count[i] == minimum:
                nodes.append(i)
        mins = []
        for key, value in self.node_hash.items():
            if value in nodes:
                mins.append(key)
        return mins

    def print_structure(self):
        for row in self.struture:
            print(row)



if  __name__ =='__main__':
    C=OrderedDict()
    C['{0}'] = ['{1}', '{2}', '{3}', '{4}'] 
    C['{1}'] = ['{1,2}', '{1,3}', '{1,4}']
    C['{2}'] = ['{1,2}', '{2,3}', '{2,4}']
    C['{3}'] = ['{1,3}', '{2,3}', '{3,4}']
    C['{4}'] = ['{1,4}', '{3,4}', '{2,4}']
    C['{1,2}'] = ['{1,2,3}', '{1,2,4}']
    C['{1,3}'] = ['{1,3,4}', '{1,2,3}']
    C['{1,4}'] = ['{1,3,4}', '{1,2,4}']
    C['{2,3}'] = ['{1,2,3}', '{2,3,4}']
    C['{2,4}'] = ['{1,2,4}', '{2,3,4}']
    C['{3,4}'] = ['{1,3,4}', '{2,3,4}']
    C['{1,2,3}'] = ['{1,2,3,4}']
    C['{1,2,4}'] = ['{1,2,3,4}']
    C['{2,3,4}'] = ['{1,2,3,4}']
    C['{1,3,4}'] = ['{1,2,3,4}']

    poset = PoSetObject(len(C)+1)
    poset.init(C)
    poset.DelMin('{0}')
    poset.DelMin('{3}')
    poset.DelMin('{1}')
    poset.print_structure()
    print(poset.ListMin())

