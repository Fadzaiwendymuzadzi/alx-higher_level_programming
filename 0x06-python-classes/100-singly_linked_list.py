#!/usr/bin/python3
"""Singley Linked List"""""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Defines a node of LL"""
        self.data = data
        self.next_node = next_node
