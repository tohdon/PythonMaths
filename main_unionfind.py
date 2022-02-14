from unionfind import *
from pprint import pprint as pp
if __name__ == '__main__':
    print("Union find data structure.")
    N = int(input("Enter number of items: "))
    uf = UF(N)
    print(uf)
    print(str(uf.count()) + " components: " + str(uf))
    uf.union(4, 2)
    print(uf.find(0))
    uf.union(4, 0)
    print(uf.find(0))