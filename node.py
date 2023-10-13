from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True, slots=True, match_args=True)
class Node:
    value: int
    left: Optional["Node"] = field(default=None)
    right: Optional["Node"] = field(default=None)


def __post_init__(self) -> None:
    if self.value < 0:
        raise ValueError("Value must be a positive number")


def node_height(node: Node) -> int:
    height = 1
    if node.left is not None:
        height = max(height, node_height(node.left) + 1)
    if node.right is not None:
        height = max(height, node_height(node.right) + 1)
    return height


def node_size(node: Node) -> int:
    size = 1
    if node.left is not None:
        size += node_size(node.left)
    if node.right is not None:
        size += node_size(node.right)
    return size


def node_sum(node: Node) -> int:
    value_sum = 0
    stack = [node]
    while stack:
        node = stack.pop()
        value_sum += node.value
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return value_sum
