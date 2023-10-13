import hypothesis.strategies as st
from hypothesis import given

from node import *

NodeValue = st.integers(0)
TerminalNodeStrategy = st.builds(Node, NodeValue)
NodeStrategy = st.deferred(lambda: TreeStrategy | TerminalNodeStrategy)
TreeStrategy = st.builds(Node, NodeValue, NodeStrategy, NodeStrategy)

# TODO: Find a way to define a strategy, parametrized by another strategy (TreeStrategy parametrized by NodeValue)
PositiveNodeValue = st.integers(1)
PositiveTerminalNodeStrategy = st.builds(Node, PositiveNodeValue)
PositiveNodeStrategy = st.deferred(lambda: PositiveTreeStrategy | PositiveTerminalNodeStrategy)
PositiveTreeStrategy = st.builds(Node, PositiveNodeValue, PositiveNodeStrategy, PositiveNodeStrategy)


@given(TreeStrategy)
def test_positive_height(node: Node) -> None:
    assert node_height(node) > 0


@given(TreeStrategy)
def test_positive_size(node: Node) -> None:
    assert node_size(node) > 0


# In a binary tree of the height n, the number of nodes is at most 2^n
@given(TreeStrategy)
def test_size_le_2_to_the_nth(node: Node) -> None:
    assert node_size(node) <= 2 ** node_height(node)


# In a binary tree with non-negative values in the nodes, the sum of the values is non-negative
@given(TreeStrategy)
def test_sum_ge_0(node: Node) -> None:
    assert node_sum(node) >= 0


# In a binary tree with positive values in the nodes, the sum of the values is positive
@given(PositiveTreeStrategy)
def test_positive_sum(node: Node) -> None:
    assert node_sum(node) > 0


# In a binary tree with positive values in the nodes, the sum of the values is at least the number of nodes
@given(PositiveTreeStrategy)
def test_positive_sum_ge_size(node: Node) -> None:
    assert node_sum(node) >= node_size(node)
