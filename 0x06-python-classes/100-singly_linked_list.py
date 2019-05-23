#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        if type(data) == int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if type(next_node) == Node or not next_node:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        if type(value) == Node or not value:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value)
        else:
            if value < self.__head.data:
                self.temp = Node(value, self.__head)
                self.__head = self.temp
            else:
                self.temp = self.__head
                while(self.temp.next_node):
                    if value < self.temp.next_node.data:
                        self.new = Node(value, self.temp.next_node)
                        self.temp.next_node = self.new
                        return
                    self.temp = self.temp.next_node
                self.new = Node(value)
                self.temp.next_node = self.new

    def __str__(self):
        self.temp = self.__head
        while (self.temp):
            print(self.temp.data, end="")
            if self.temp.next_node:
                print()
            self.temp = self.temp.next_node
        return ""
