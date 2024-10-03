class Node:
    """Represents a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize the Node with data and next_node.

        Args:
            data (int): The data value for the node.
            next_node (Node): The next node in the list, default is None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node instance.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """Initialize the singly linked list with an empty head."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the entire list.

        One node's data per line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node with the given value in the correct sorted position.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

