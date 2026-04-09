# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Moonlight Coders
- Members: Sushant Thapa
- Repository name: project-2-moonlight-museum-after-dark-sushant913

---

## Project summary
Our project builds a system for organizing strange museum artifacts after dark. The system uses multiple data structures such as a binary search tree, queue, stack, and linked list to manage artifacts, restoration requests, exhibit routes, and reports. It allows efficient searching, sorting, and tracking of museum activities.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note (150-250 words)
This project uses different data structures based on their strengths. A Binary Search Tree (BST) is used to store artifacts because it allows efficient searching, insertion, and traversal based on artifact IDs. Since IDs are unique, BST is a natural choice for organizing them in sorted order.

A queue is used for restoration requests because it follows the First-In-First-Out (FIFO) principle, which matches real-world scenarios where requests should be processed in the order they are received. A stack is used for undo operations because it follows Last-In-First-Out (LIFO), making it ideal for reversing recent actions.

A singly linked list is used for the exhibit route because it allows flexible insertion and removal of stops without shifting elements like in an array. This makes it efficient for managing routes.

The system is organized into separate classes for each structure, improving readability and modularity. Helper functions are used for reporting and searching tasks, keeping logic clean and reusable. Overall, the design focuses on clarity, efficiency, and matching the correct data structure to each problem.

---

## Complexity reasoning

- `ArtifactBST.insert`: O(h), where h is the height of the tree, because insertion follows one path from root to leaf.
- `ArtifactBST.search_by_id`: O(h), since it traverses down one branch of the tree.
- `ArtifactBST.inorder_ids`: O(n), because every node is visited once.
- `RestorationQueue.process_next_request`: O(1), since deque removal from the front is constant time.
- `ArchiveUndoStack.undo_last_action`: O(1), because popping from a list is constant time.
- `ExhibitRoute.remove_stop`: O(n), since it may traverse the entire list to find the stop.
- `sort_artifacts_by_age`: O(n log n), due to Python's sorting algorithm.
- `linear_search_by_name`: O(n), since it may check each artifact once.

---

## Edge-case checklist

### BST
- [x] insert into empty tree → root is assigned
- [x] search for missing ID → returns None
- [x] empty traversals → return empty lists
- [x] duplicate ID → ignored and returns False

### Queue
- [x] process empty queue → returns None
- [x] peek empty queue → returns None

### Stack
- [x] undo empty stack → returns None
- [x] peek empty stack → returns None

### Exhibit route linked list
- [x] empty route → returns empty list
- [x] remove missing stop → returns False
- [x] remove first stop → head updated
- [x] remove middle stop → links updated correctly
- [x] remove last stop → tail removed
- [x] one-stop route → becomes empty

### Reports
- [x] empty artifact list → returns empty dict/set/list
- [x] repeated categories → counted correctly
- [x] repeated rooms → duplicates removed via set
- [x] missing artifact name → returns None
- [x] same-age artifacts → sorting still works correctly

---

## Demo plan / how to run

Run tests:
```bash
pytest -q