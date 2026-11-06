# Assessment 3.2 - Doubly Linked List
# Adding and Removing Letters Using Doubly Linked List

# ---------- Get the letters from the user ----------
def get_letters():
    default = ["R", "O", "S", "I", "M", "A"]
    text = input("Enter your letters (example: ROSIMA) or press Enter to use R, O, S, I, M, A: ")
    letters = []
    for ch in text:
        if ch.isalpha():              # keep letters only (ignore spaces and commas)
            letters.append(ch.upper())
    if len(letters) == 0:
        letters = default
    return letters


# A node holds one letter, a link to the previous node and a link to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None                      # first node
        self.tail = None                      # last node

    # Create a new node and connect it using previous and next pointers
    def add(self, data):
        new_node = Node(data)
        if self.head is None:                 # first node is both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail         # new node points back to the old last node
            self.tail.next = new_node         # old last node points forward to the new node
            self.tail = new_node

    # Delete the first node and update the previous and next pointers
    def remove_first(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next            # head moves to the next node
        if self.head is None:                 # list became empty
            self.tail = None
        else:
            self.head.prev = None             # new head has no previous node
        return removed

    def is_empty(self):
        return self.head is None

    # Return the list as text, example: R ↔ O ↔ S
    def to_text(self):
        if self.head is None:
            return "(empty)"
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return " ↔ ".join(parts)


# ---------- Main program ----------
print("=== DOUBLY LINKED LIST: Adding and Removing Letters ===")   # 1. Start
letters = get_letters()

linked_list = DoublyLinkedList()                                   # 2. Create empty list
print("\nAn empty doubly linked list was created:", linked_list.to_text())

# 3-9. Create nodes and connect them with previous and next pointers
print("\n--- ADDING PROCESS ---")
for letter in letters:
    linked_list.add(letter)
    print("Added node", letter, "->", linked_list.to_text())

# 10. Display all nodes
print("\nAll nodes:", linked_list.to_text())

# 11-13. Delete the first node, update pointers, repeat until empty
print("\n--- REMOVING PROCESS ---")
while not linked_list.is_empty():
    removed = linked_list.remove_first()
    print("Deleted node", removed, "(pointers updated) ->", linked_list.to_text())

# 14. Display "Doubly Linked List is Empty"
print("\nDoubly Linked List is Empty")
print("Final Output: Empty Doubly Linked List")
print("=== END ===")                                               # 15. Stop
