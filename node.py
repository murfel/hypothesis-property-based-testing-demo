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
    h = 1
    if node.left is not None:
        h = max(h, node_height(node.left) + 1)
    if node.right is not None:
        h = max(h, node_height(node.right) + 1)
    return h


def node_size(node: Node) -> int:
    s = 1
    if node.left is not None:
        s += node_size(node.left)
    if node.right is not None:
        s += node_size(node.right)
    return s


def node_sum(node: Node) -> int:
    sum = 0
    st = [node]
    while st:
        cur = st.pop()
        sum += cur.value
        if cur.left is not None:
            st.append(cur.left)
        if cur.right is not None:
            st.append(cur.right)

    return sum
