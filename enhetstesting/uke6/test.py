from BinaryTree import BinaryTree
from collections import namedtuple
from BinaryTreeNode import BinaryTreeNode

# Declare namedtuple()
Person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

persons = []

def createSmallTree(list,n):
    tree = BinaryTree()
    for p in list[:n]:
        tree.insert(value=p)
        #print(f'satte inn verdi: {p}')
    return tree

def test_getnodes():
    tree_empty = BinaryTree()
    node_none = BinaryTreeNode(None)
    node = BinaryTreeNode(1)
    print(node_none.value)
    tree = BinaryTree()
    # Attempt to reach line 50-51, but if-test is overloaded which prevents it.
    #tree._getnodes(current=None,treenode=node_none,value=None) # Should raise Exception("Attempt to insert an Node into Binary Tree with no key value")
    tree._getnodes(current=None,treenode=node,value=1) # raises Exception("Key inconsistency detected.")
    # Raising exceptions but covering output with pytest.raises:
    #with pytest.raises(Exception):
     #   tree_empty.insert(None)
      #  tree.insert(node_none)
    #try:
     #   tree.insert(value=None)
    #except Exception as exc: 
     #   assert False, f'_getnodes() raised an exception {exc}'
    
def test_delete():
    tupa = ("A","A","vei 3","0003","poststed 3")
    pa = Person(*tupa)
    tupb = ("B","B","vei 4","0004","poststed 4")
    pb = Person(*tupb)
    tupc = ("C","C","vei 1","0001","poststed 1")
    pc = Person(*tupc)
    tupd = ("D","D","vei 1","0001","poststed 1")
    pd = Person(*tupd)
    tupe = ("E","E","vei 2","0002","poststed 2")
    pe = Person(*tupe)
    tupf = ("F","F","vei 2","0002","poststed 2")
    pf = Person(*tupf)
    tree = BinaryTree()
    tree.insert(value=pa)
    tree.insert(value=pc)
    tree.insert(value=pb)
    print(f'root: {tree._root.value}')
    #print(tree._root.right.value)
    #print(tree._root.right.right.value)
    print(f' maks 1: {tree.deleteMax().value}')
    #print(f' minst 2: {tree.deleteMin().value}')
    #print(f' minst 3: {tree.deleteMin().value}')
    return

    tree.insert(value=pa)
    tree.insert(value=pe)
    tree.insert(value=pd)
    print(f'rot: {tree._root.value}')
    print(f'left: {tree._root.left.value}')
    print(f'right: {tree._root.right.value}')
    print(f'right-right: {tree._root.right.right.value}')
    print(f'right-right-left: {tree._root.right.right.left.value}')
    #print(f'pd: {tree.delete(pd).value}') # This is working runs through line 154
    # Trying to delete key which does not exist to reach line 141, but overrides in BinaryTreeNode is faulty.
    print(f'?: {tree.delete(pf).value}') # This is working runs through line 154
    #print(f'rot: {tree._root.value}')
    

#    assert tree.delete(p1) == p1, "delete() did not return NYMANN."
    #assert tree.delete(persons[3]) == node_vestly, "delete() did not return VESTLY."
    #assert tree.delete(persons[6]) == None, "delete() did not return None."

def test_deleteMin():
    # Declare namedtuple()
    Person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

    gjerstad = Person(etternavn='GJERSTAD', fornavn='TORKJELL', adresse='HOSTELAND 2 83', postnummer='1361', poststed='ï¿½STERï¿½S')
    kristiansen = Person(etternavn='KRISTIANSEN', fornavn='MORTEN KRISTIAN', adresse='LEINAHYTTA 36', postnummer='7224', poststed='MELHUS')
    linnerud = Person(etternavn='LINNERUD', fornavn='JOHNNY', adresse='Lï¿½RUM MELLEM 50', postnummer='6507', poststed='KRISTIANSUND N')
    nymann = Person(etternavn='NYMANN', fornavn='ROY-ï¿½YSTEIN', adresse='Hï¿½NESET 77', postnummer='7033', poststed='TRONDHEIM')
    oldervik = Person(etternavn='OLDERVIK', fornavn='SHARI LILL', adresse='KRï¿½KA 84', postnummer='5948', poststed='FEDJE')
    vestly = Person(etternavn='VESTLY SKIVIK', fornavn='JAHN FREDRIK', adresse='LINNGï¿½RD 22', postnummer='1451', poststed='NESODDTANGEN')

    persons = [linnerud,kristiansen,oldervik,nymann,gjerstad,vestly]
    """
    BST from persons list
    linnerud
        kristiansen
            gjerstad
        oldervik
            nymann
            vestly
    """

    print(persons)
    
    tree = BinaryTree()
    
    node_gjerstad = BinaryTreeNode(persons[2])
    tree.insert(value=persons[1]) # Oldervik
    tree.insert(value=persons[2]) # Gjerstad
    tree.insert(value=persons[0]) # Kristiansen
    print(tree)
    print(tree.deleteMin() == node_gjerstad)


#test_delete()
test_deleteMin()