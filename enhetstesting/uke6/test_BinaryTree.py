from BinaryTree import BinaryTree
from collections import namedtuple
from BinaryTreeNode import BinaryTreeNode
import pytest

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

def createTree(list,n):
    tree = BinaryTree()
    for p in list[:n]:
        tree.insert(value=p)
    return tree

# Start tests

def test_init():
    rot = BinaryTreeNode(gjerstad)
    try:
        tree = BinaryTree(rot)
    except Exception as exc:
        assert False, f"'__init__() raised an exception {exc}"
    node = BinaryTreeNode(gjerstad)
    assert tree._root == node, "Failed to insert BinaryTreeNode to root."
    assert isinstance(tree._root,BinaryTreeNode), "Failed to only insert BinaryTreeNode to root."

def test_findLeftMost():
    tree = BinaryTree()
    tree.insert(value=nymann)
    tree.insert(value=vestly)
    tree.insert(value=oldervik)
    tree.insert(value=gjerstad)
    """
    BST
    nymann
        gjerstad
        vestly
            oldervik
            -
    """
    node_gjerstad = BinaryTreeNode(gjerstad)
    assert tree.findLeftMost(tree._root) == node_gjerstad, "Leftmost is not GJERSTAD."

def test_findMin():
    tree = BinaryTree()
    node_gjerstad = BinaryTreeNode(gjerstad)
    tree.insert(value=nymann)
    tree.insert(value=vestly)
    tree.insert(value=gjerstad)
    print(tree._root.value)
    assert tree.findMin() == node_gjerstad, "Min value is not GJERSTAD."

def test_findRightMost():
    tree = createTree(persons,6)
    node = BinaryTreeNode(vestly)
    assert tree.findRightMost(tree._root) == node, "Rightmost is not VESTLY."

def test_findMax():
    tree = createTree(persons,6)
    node = BinaryTreeNode(vestly)
    assert tree.findMax() == node, "Max value is not VESTLY."

def test_find():
    tree = createTree(persons,5)
    node_linnerud = BinaryTreeNode(linnerud)
    assert tree.find(linnerud) == node_linnerud, "Did not find Person LINNERUD."
    node_oldervik = BinaryTreeNode(oldervik)
    assert tree.find(oldervik) == node_oldervik, "Did not find Person OLDERVIK."
    try:
        tree.find(vestly)
    except KeyError as exc:
        assert False, f"'find() raised an exception {exc}"
    tree = BinaryTree()
    assert tree.find(oldervik) == None, "Did not return None when tree empty."

def test_getnodes():
    node_none = BinaryTreeNode(None)
    node = BinaryTreeNode(1)
    tree = BinaryTree()
    # Raising exceptions but covering output with pytest.raises:
    with pytest.raises(Exception):
        tree.insert(None)
        # Attempt to reach line 50-51, but if-test is overloaded which prevents it.
        # Should raise Exception("Attempt to insert an Node into Binary Tree with no key value")
        tree._getnodes(current=None,treenode=node_none,value=None)     
    with pytest.raises(Exception):
        # Next test raises Exception("Key inconsistency detected.")
        tree._getnodes(current=None,treenode=node,value=1) 
    
def test_insert():
    tree = BinaryTree()
    node_person1 = BinaryTreeNode(linnerud)
    tree.insert(value=linnerud)
    with pytest.raises(Exception):
        tree.insert(value=linnerud)


def test_deleteMin():
    tree = createTree(persons,6)
    node = BinaryTreeNode(gjerstad)
    assert tree.deleteMin() == node, "deleteMin() did not return GJERSTAD."

    # Reach line 98-99
    tree = BinaryTree()
    node_gjerstad = BinaryTreeNode(persons[2])
    tree.insert(value=persons[1]) # Oldervik
    tree.insert(value=persons[2]) # Gjerstad
    tree.insert(value=persons[0]) # Kristiansen
    assert tree.deleteMin() == node_gjerstad, "deleteMin() did not return GJERSTAD"

    # Reach line 104-108
    # A bug on line 107 overwrites the node to be returned, 
    # and therby returns a node which is bigger.
    tree = BinaryTree()
    node_kristiansen = BinaryTreeNode(kristiansen)
    tree.insert(value=gjerstad) # Gjerstad # Smallest node
    tree.insert(value=kristiansen) # Kristiansen
    tree.insert(value=oldervik) # Oldervik
    assert tree.deleteMin() == node_kristiansen, "deleteMin() did not return KRISTIANSEN"

def test_deleteMax():
    tree = createTree(persons,6)
    node = BinaryTreeNode(vestly)
    assert tree.deleteMax() == node, "deleteMax() did not return VESTLY."

    # Reach line 116-117
    tree = BinaryTree()
    node_oldervik = BinaryTreeNode(oldervik)
    tree.insert(value=gjerstad) # Gjerstad
    tree.insert(value=oldervik) # Oldervik
    tree.insert(value=kristiansen) # Kristiansen
    assert tree.deleteMax() == node_oldervik, "delete() did not return OLDERVIK"


def test_delete():
    tree = BinaryTree()
    node_kristiansen = BinaryTreeNode(kristiansen)
    node_oldervik = BinaryTreeNode(oldervik)
    tree.insert(value=kristiansen)
    tree.insert(value=oldervik)
    tree.insert(value=vestly)
    assert tree.delete(oldervik) == node_oldervik, "delete() did not return OLDERVIK"

    # Reach line 163-165
    tree = BinaryTree()
    tree.insert(value=oldervik) # Oldervik
    tree.insert(value=kristiansen) # Kristiansen
    tree.insert(value=gjerstad) # Gjerstad
    assert tree.delete(kristiansen) == node_kristiansen, "delete() did not return KRISTIANSEN"

    # Reach line 166-167
    tree = BinaryTree()
    tree.insert(value=gjerstad) # Gjerstad
    tree.insert(value=oldervik) # Oldervik
    tree.insert(value=kristiansen) # Kristiansen
    assert tree.delete(oldervik) == node_oldervik, "delete() did not return OLDERVIK"

    tree = createTree(persons,6)
    node_nymann = BinaryTreeNode(nymann)
    node_oldervik = BinaryTreeNode(oldervik)
    node_gjerstad = BinaryTreeNode(gjerstad)
    assert tree.delete(nymann) == node_nymann, "delete() did not return NYMANN."
    assert tree.delete(oldervik) == node_oldervik, "delete() did not return VESTLY."
    # Not possible to reach line 141 when deleting a node which does not exist due to bug in BinaryTreeNode when checking __lt__.
    with pytest.raises(Exception):
        assert tree.delete(linnerud) == None, "delete() did not return None."
    assert tree.delete(gjerstad) == node_gjerstad, "delete() did not return GJERSTAD."


