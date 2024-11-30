from BinaryTreeNode import BinaryTreeNode
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

def createRoot():
    rot = BinaryTreeNode("x")
    rot.left = BinaryTreeNode("+")
    rot.right = BinaryTreeNode("-")
    rot.left.left = BinaryTreeNode("a")
    rot.left.right = BinaryTreeNode("b")
    rot.right.left = BinaryTreeNode("c")
    rot.right.right = BinaryTreeNode("d")
    return rot

def test_init():
    rot = BinaryTreeNode("x")
    assert type(rot).__name__ == "BinaryTreeNode", "Wrong class name."

def test_property_value():
    rot = BinaryTreeNode("x")
    assert rot.value == "x", "Wrong value set."

def test_value_setter():
    rot = BinaryTreeNode("x")
    rot.value = "y"
    assert rot.value == "y", "Wrong value set."

def test_property_left():
    rot = BinaryTreeNode("x")
    assert rot.left == None, "Left tree not set to None"

def test_left_setter():
    rot = BinaryTreeNode("x")
    rot.left = "y"
    assert rot.left == "y", "Wrong value set."

def test_property_right():
    rot = BinaryTreeNode("x")
    assert rot.right == None, "Right tree not set to None"

def test_right_setter():
    rot = BinaryTreeNode("x")
    rot.right = "z"
    assert rot.right == "z", "Wrong value set."

def test_property_level():
    rot = BinaryTreeNode("x")
    assert type(rot.level).__name__ == "int", "Level not a number."

def test_level_setter():
    rot = BinaryTreeNode("x")
    rot.level = 1
    assert rot.level == 1, "Level not set correctly."

def test_str():
    rot = BinaryTreeNode("x")
    assert rot.__str__() == "x", "Wrong value set."

def test_hasRight():
    rot = BinaryTreeNode("x")
    assert rot.hasRight() == False, "Conditional expression faulty."
    rot.right = "y"
    assert rot.hasRight() == True, "Condition wrong."

def test_hasLeft():
    rot = BinaryTreeNode("x")
    assert rot.hasLeft() == False, "Conditional expression faulty."
    rot.left = "z"
    assert rot.hasLeft() == True, "Condition wrong."

def test_prefixOrder():
    rot = createRoot()
    try:
        rot.prefixOrder()
    except Exception as exc:
        assert False, f"'prefixorder() raised an exception {exc}"

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
    node1 = BinaryTreeNode("x")
    node2 = BinaryTreeNode("x")
    node_none = BinaryTreeNode(None)
    assert node1.__eq__(node2), "Values are not compared correctly."
    assert node_none.__eq__(None) is True, "None values are not compared correctly."
    assert node1.__eq__(None) is False, "Values are not compared correctly."

def test_ne():
    node1 = BinaryTreeNode("x")
    node2 = BinaryTreeNode("x")
    node_none = BinaryTreeNode(None)
    assert node1.__ne__(node2) is False, "Values are not compared correctly."
    assert node_none.__ne__(None) is True, "None values are not compared correctly."
    assert node_none.__ne__(node1) is False, "None values are not compared correctly."
    assert node1.__ne__(None) is True, "Values are not compared correctly."

def test_lt():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node_none = BinaryTreeNode(None)
    assert node1.__lt__(node2) is True, "Values are not compared correctly."
    assert node1.__lt__(None) is False, "None values are not compared correctly."
    assert node_none.__lt__(None) is False, "None values are not compared correctly."

def test_le():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(3)
    node_none = BinaryTreeNode(None)
    assert node1.__le__(node2) is True, "Values are not compared correctly."
    assert node1.__le__(node3) is True, "Values are not compared correctly."
    assert node3.__le__(node1) is False, "Values are not compared correctly."
    assert node_none.__le__(None) is False, "None values are not compared correctly."

def test_gt():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node_none = BinaryTreeNode(None)
    assert node2.__gt__(node1) is True, "Values are not compared correctly."
    assert node1.__gt__(node2) is False, "Values are not compared correctly."
    assert node1.__gt__(None) is False, "Values are not compared correctly."
    assert node_none.__gt__(None) is False, "None values are not compared correctly."

def test_ge():
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(3)
    node_none = BinaryTreeNode(None)
    assert node1.__ge__(node2) is True, "Values are not compared correctly."
    assert node1.__ge__(node3) is False, "Values are not compared correctly."
    assert node3.__ge__(node1) is True, "Values are not compared correctly."
    assert node_none.__ge__(None) is False, "Values are not compared correctly."