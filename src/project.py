from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


class TreeNode:
    def __init__(self, artifact: Artifact):
        self.artifact = artifact
        self.left = None
        self.right = None


class ArtifactBST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, artifact: Artifact) -> bool:
        if self.root is None:
            self.root = TreeNode(artifact)
            return True

        current = self.root
        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False  # duplicate

            elif artifact.artifact_id < current.artifact.artifact_id:
                if current.left is None:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left

            else:
                if current.right is None:
                    current.right = TreeNode(artifact)
                    return True
                current = current.right

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        current = self.root
        while current:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.artifact.artifact_id)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node:
                result.append(node.artifact.artifact_id)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.artifact.artifact_id)

        traverse(self.root)
        return result


class RestorationQueue:
    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek_next_request(self) -> RestorationRequest | None:
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        if self.is_empty():
            return None
        return self._items.pop()

    def peek_last_action(self) -> str | None:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    def __init__(self, stop_name: str):
        self.stop_name = stop_name
        self.next = None


class ExhibitRoute:
    def __init__(self) -> None:
        self.head = None

    def add_stop(self, stop_name: str) -> None:
        new_node = ExhibitNode(stop_name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        current = self.head
        prev = None

        while current:
            if current.stop_name == stop_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True

            prev = current
            current = current.next

        return False

    def list_stops(self) -> list[str]:
        result = []
        current = self.head

        while current:
            result.append(current.stop_name)
            current = current.next

        return result

    def count_stops(self) -> int:
        return len(self.list_stops())


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    result = {}
    for a in artifacts:
        result[a.category] = result.get(a.category, 0) + 1
    return result


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    return {a.room for a in artifacts}


def sort_artifacts_by_age(
    artifacts: list[Artifact],
    descending: bool = False,
) -> list[Artifact]:
    return sorted(artifacts, key=lambda a: a.age, reverse=descending)


def linear_search_by_name(
    artifacts: list[Artifact],
    name: str,
) -> Artifact | None:
    for a in artifacts:
        if a.name == name:
            return a
    return None


def demo_museum_night() -> None:
    bst = ArtifactBST()

    artifacts = [
        Artifact(5, "Mirror", "Cursed", 200, "A"),
        Artifact(2, "Bird", "Clockwork", 150, "B"),
        Artifact(8, "Map", "Magic", 300, "C"),
        Artifact(1, "Key", "Mystic", 100, "A"),
        Artifact(3, "Lantern", "Light", 80, "D"),
        Artifact(7, "Book", "Ancient", 500, "E"),
        Artifact(6, "Mask", "Spirit", 220, "B"),
        Artifact(4, "Orb", "Magic", 180, "C"),
    ]

    for a in artifacts:
        bst.insert(a)

    print("Inorder:", bst.inorder_ids())
    print("Search 3:", bst.search_by_id(3))
    print("Search 99:", bst.search_by_id(99))

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(1, "Fix mirror"))
    queue.add_request(RestorationRequest(2, "Repair bird"))
    print("Processing:", queue.process_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added artifact")
    stack.push_action("Removed artifact")
    print("Undo:", stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Hall A")
    route.add_stop("Vault")
    print("Route:", route.list_stops())

    print("Categories:", count_artifacts_by_category(artifacts))
    print("Rooms:", unique_rooms(artifacts))