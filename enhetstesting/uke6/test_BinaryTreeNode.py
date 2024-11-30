from BinaryTreeNode import BinaryTreeNode
from collections import namedtuple
import pytest

"""
Unit test av BinaryTreeNode.
Kommentar:
Benytter enkle tekststrenger og tall for testing av noder for å 
være helt sikker på at sammenlikning fungerer.
Kildekoden for klassen har ikke private verdier satt korrekt med
dunder-understreking, så det gir egentlig liten mening å 
teste metodene dekorert med @property, men jeg later som verdiene
er private i denne testen.
"""

# Declare namedtuple()
Person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

gjerstad = Person(etternavn='GJERSTAD', fornavn='TORKJELL', adresse='HOSTELAND 2 83', postnummer='1361', poststed='ï¿½STERï¿½S')
kristiansen = Person(etternavn='KRISTIANSEN', fornavn='MORTEN KRISTIAN', adresse='LEINAHYTTA 36', postnummer='7224', poststed='MELHUS')
linnerud = Person(etternavn='LINNERUD', fornavn='JOHNNY', adresse='Lï¿½RUM MELLEM 50', postnummer='6507', poststed='KRISTIANSUND N')
nymann = Person(etternavn='NYMANN', fornavn='ROY-ï¿½YSTEIN', adresse='Hï¿½NESET 77', postnummer='7033', poststed='TRONDHEIM')
oldervik = Person(etternavn='OLDERVIK', fornavn='SHARI LILL', adresse='KRï¿½KA 84', postnummer='5948', poststed='FEDJE')
vestly = Person(etternavn='VESTLY SKIVIK', fornavn='JAHN FREDRIK', adresse='LINNGï¿½RD 22', postnummer='1451', poststed='NESODDTANGEN')


def createRoot():
    rot = BinaryTreeNode(linnerud)
    rot.left = BinaryTreeNode(kristiansen)
    rot.right = BinaryTreeNode(oldervik)
    rot.left.left = BinaryTreeNode(gjerstad)
    rot.right.left = BinaryTreeNode(nymann)
    rot.right.right = BinaryTreeNode(vestly)
    return rot

def test_init():
    rot = BinaryTreeNode(linnerud)
    assert type(rot).__name__ == "BinaryTreeNode", "Wrong class name."

def test_property_value():
    rot = BinaryTreeNode(linnerud)
    assert rot.value == linnerud, "Wrong node value"

def test_value_setter():
    rot = BinaryTreeNode(linnerud)
    rot.value = gjerstad
    assert rot.value == gjerstad, "Wrong value set."

def test_property_left():
    rot = BinaryTreeNode(linnerud)
    assert rot.left == None, "Left tree not set to None"

def test_left_setter():
    rot = BinaryTreeNode(linnerud)
    rot.left = gjerstad
    assert rot.left == gjerstad, "Wrong value set."

def test_property_right():
    rot = BinaryTreeNode(linnerud)
    assert rot.right == None, "Right tree not set to None"

def test_right_setter():
    rot = BinaryTreeNode(linnerud)
    rot.right = gjerstad
    assert rot.right == gjerstad, "Wrong value set."

def test_property_level():
    rot = BinaryTreeNode(linnerud)
    assert type(rot.level).__name__ == "int", "Level not a number."
    assert rot.level == 0, "Node not set to level 0"

def test_level_setter():
    rot = BinaryTreeNode(linnerud)
    rot.level = 1
    assert rot.level == 1, "Level not set correctly."

def test_str():
    rot = BinaryTreeNode(linnerud)
    assert rot.__str__() == linnerud, "Wrong value set."

def test_hasRight():
    rot = BinaryTreeNode(linnerud)
    assert rot.hasRight() == False, "Conditional expression faulty."
    rot.right = gjerstad
    assert rot.hasRight() == True, "Conditionional expression faulty."

def test_hasLeft():
    rot = BinaryTreeNode(linnerud)
    assert rot.hasLeft() == False, "Conditional expression faulty."
    rot.left = gjerstad
    assert rot.hasLeft() == True, "Conditionional expression faulty."

def test_prefixOrder():
    rot = createRoot()
    try:
        rot.prefixOrder()
    except Exception as exc:
        assert False, f"'prefixorder() raised an exception {exc}"

def test_infixOrder():
    rot = createRoot()
    try:
        rot.infixOrder()
    except Exception as exc:
        assert False, f"'infixorder() raised an exception {exc}"

def test_postfixOrder():
    rot = createRoot()
    try:
        rot.postfixOrder()
    except Exception as exc:
        assert False, f"'postfixorder() raised an exception {exc}"

def test_levelOrder():
    rot = createRoot()
    try:
        rot.levelOrder()
    except Exception as exc:
        assert False, f"'levelorder() raised an exception {exc}"

def test_levelOrderEntry():
    rot = createRoot()
    from queue import SimpleQueue
    FIFOQueue = SimpleQueue()
    FIFOQueue.put(rot)
    try:
        rot.levelOrderEntry(FIFOQueue)
    except Exception as exc:
        assert False, f"'levelOrderEntry() raised an exception {exc}"

def test_eq():
    node1 = BinaryTreeNode(linnerud)
    node2 = BinaryTreeNode(linnerud)
    node_none = BinaryTreeNode(None)
    assert node1 == node2, "Values are not compared correctly."
    assert node_none == None, "None values are not compared correctly."
    assert node1 != None, "Values are not compared correctly."

@pytest.mark.xfail
def test_ne():
    node_linnerud1 = BinaryTreeNode(linnerud)
    node_linnerud2 = BinaryTreeNode(linnerud)
    node_gjerstad = BinaryTreeNode(gjerstad)
    node_none = BinaryTreeNode(None)
    assert not node_linnerud1 != node_linnerud2, "Values are not compared correctly."
    assert node_none != node_linnerud1, "None values are not compared correctly."
    assert node_linnerud1 != node_none, "None values are not compared correctly."
    assert node_linnerud1 != node_gjerstad, "None values are not compared correctly."

def test_lt():
    node1 = BinaryTreeNode(gjerstad)
    node2 = BinaryTreeNode(linnerud)
    node_none = BinaryTreeNode(None)
    assert node1 < node2, "Values are not compared correctly."
    assert not node1 < None, "None values are not compared correctly. Check against None should give False."
    assert not node_none < None, "None values are not compared correctly."


def test_le():
    node_kristiansen = BinaryTreeNode(kristiansen)
    node_linnerud = BinaryTreeNode(linnerud)
    node_linnerud2 = BinaryTreeNode(linnerud)
    node_gjerstad = BinaryTreeNode(gjerstad)
    node_none = BinaryTreeNode(None)
    assert node_kristiansen <= node_linnerud, "Values are not compared correctly."
    assert not node_linnerud <= node_gjerstad, "Values are not compared correctly."
    assert node_linnerud <= node_linnerud2, "Values are not compared correctly."
    assert not node_none <= None, "None values are not compared correctly."
    assert not node_linnerud <= None, "None values are not compared correctly."

def test_gt():
    node1 = BinaryTreeNode(gjerstad)
    node2 = BinaryTreeNode(linnerud)
    node_none = BinaryTreeNode(None)
    assert node2 > node1, "Values are not compared correctly."
    assert not node1 > node2, "Values are not compared correctly."
    assert not node1 > None, "Values are not compared correctly."
    assert not node_none > None, "None values are not compared correctly."

def test_ge():
    node1 = BinaryTreeNode(gjerstad)
    node2 = BinaryTreeNode(gjerstad)
    node3 = BinaryTreeNode(linnerud)
    node_none = BinaryTreeNode(None)
    assert node1 >= node2, "Values are not compared correctly."
    assert not node1 >= node3, "Values are not compared correctly."
    assert node3 >= node1, "Values are not compared correctly."
    assert not node_none >= None, "Values are not compared correctly."
