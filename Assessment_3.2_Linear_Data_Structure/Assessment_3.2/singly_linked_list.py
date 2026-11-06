# Assessment 3.2 - Singly Linked List
# Adding and Removing Letters Using Singly Linked List

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


# A node holds one letter and a link to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None                      # empty list has no head

    # Create a new node and connect it to the last node
    def add(self, data):
        new_node = Node(data)
        if self.head is None:                 # first node becomes the head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:   # go to the last node
                current = current.next
            current.next = new_node           # connect the new node

    # Delete the first node and move the head to the next node
    def remove_first(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def is_empty(self):
        return self.head is None

    # Return the list as text, example: R → O → S
    def to_text(self):
        if self.head is None:
            return "(empty)"
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return " → ".join(parts)


# ---------- Main program ----------
print("=== SINGLY LINKED LIST: Adding and Removing Letters ===")   # 1. Start
letters = get_letters()

linked_list = SinglyLinkedList()                                   # 2. Create empty list
print("\nAn empty singly linked list was created:", linked_list.to_text())

# 3-8. Create nodes and connect them
print("\n--- ADDING PROCESS ---")
for letter in letters:
    linked_list.add(letter)
    print("Added node", letter, "->", linked_list.to_text())

# 9. Display all nodes
print("\nAll nodes:", linked_list.to_text())

# 10-12. Delete the first node, move head, repeat until empty
print("\n--- REMOVING PROCESS ---")
while not linked_list.is_empty():
    removed = linked_list.remove_first()
    print("Deleted node", removed, "(head moved to next node) ->", linked_list.to_text())

# 13. Display "Linked List is Empty"
print("\nLinked List is Empty")
print("Final Output: Empty Linked List")
print("=== END ===")                                               # 14. Stop
