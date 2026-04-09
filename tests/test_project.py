from __future__ import annotations

from src.project import (
    ArchiveUndoStack,
    Artifact,
    ArtifactBST,
    ExhibitRoute,
    RestorationQueue,
    RestorationRequest,
    count_artifacts_by_category,
    demo_museum_night,
    linear_search_by_name,
    sort_artifacts_by_age,
    unique_rooms,
)


def make_artifacts() -> list[Artifact]:
    return [
        Artifact(40, "Cursed Mirror", "mirror", 220, "North Hall"),
        Artifact(20, "Clockwork Bird", "machine", 80, "Workshop"),
        Artifact(60, "Whispering Map", "paper", 140, "Archive"),
        Artifact(10, "Glowing Key", "metal", 35, "Vault"),
        Artifact(30, "Moon Dial", "device", 120, "North Hall"),
        Artifact(50, "Silver Mask", "costume", 160, "Gallery"),
        Artifact(70, "Lantern Jar", "glass", 60, "Gallery"),
        Artifact(25, "Ink Compass", "device", 120, "Archive"),
    ]


# ---------------- BST ----------------

def test_bst_empty():
    bst = ArtifactBST()
    assert bst.search_by_id(1) is None
    assert bst.inorder_ids() == []
    assert bst.preorder_ids() == []
    assert bst.postorder_ids() == []


def test_bst_insert_and_search():
    bst = ArtifactBST()
    a = Artifact(10, "Key", "metal", 10, "A")
    assert bst.insert(a) is True
    assert bst.search_by_id(10) == a


def test_bst_duplicate():
    bst = ArtifactBST()
    a1 = Artifact(10, "Key", "metal", 10, "A")
    a2 = Artifact(10, "Fake", "metal", 5, "B")

    assert bst.insert(a1) is True
    assert bst.insert(a2) is False
    assert bst.search_by_id(10) == a1


def test_bst_traversals():
    bst = ArtifactBST()
    for a in make_artifacts():
        bst.insert(a)

    assert bst.inorder_ids() == [10, 20, 25, 30, 40, 50, 60, 70]
    assert bst.preorder_ids() == [40, 20, 10, 30, 25, 60, 50, 70]
    assert bst.postorder_ids() == [10, 25, 30, 20, 50, 70, 60, 40]


# ---------------- Queue ----------------

def test_queue():
    q = RestorationQueue()
    assert q.is_empty()

    r1 = RestorationRequest(1, "Fix")
    r2 = RestorationRequest(2, "Clean")

    q.add_request(r1)
    q.add_request(r2)

    assert q.peek_next_request() == r1
    assert q.process_next_request() == r1
    assert q.process_next_request() == r2
    assert q.process_next_request() is None


# ---------------- Stack ----------------

def test_stack():
    s = ArchiveUndoStack()
    assert s.is_empty()

    s.push_action("A")
    s.push_action("B")

    assert s.peek_last_action() == "B"
    assert s.undo_last_action() == "B"
    assert s.undo_last_action() == "A"
    assert s.undo_last_action() is None


# ---------------- Linked List ----------------

def test_route():
    route = ExhibitRoute()

    route.add_stop("A")
    route.add_stop("B")
    route.add_stop("C")

    assert route.list_stops() == ["A", "B", "C"]

    assert route.remove_stop("B") is True
    assert route.list_stops() == ["A", "C"]

    assert route.remove_stop("A") is True
    assert route.remove_stop("C") is True

    assert route.list_stops() == []


# ---------------- Utilities ----------------

def test_utils():
    artifacts = make_artifacts()

    counts = count_artifacts_by_category(artifacts)
    assert counts["device"] == 2

    rooms = unique_rooms(artifacts)
    assert "Gallery" in rooms

    sorted_list = sort_artifacts_by_age(artifacts)
    assert sorted_list[0].age <= sorted_list[-1].age

    assert linear_search_by_name(artifacts, "Whispering Map") is not None
    assert linear_search_by_name(artifacts, "None") is None


# ---------------- Demo ----------------

def test_demo(capsys):
    demo_museum_night()
    output = capsys.readouterr().out

    assert "Moonlight Museum After Dark" in output
    assert "Inorder IDs:" in output
    assert "Next restoration request:" in output
    assert "Undo action:" in output
    assert "Exhibit route:" in output
    assert "Category counts:" in output