# Assessment 3.2 - Queue
# Adding and Removing Letters Using Queue
# A queue is FIFO (First In, First Out): the first letter enqueued is the first one dequeued.

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


# ---------- Main program ----------
print("=== QUEUE: Adding and Removing Letters ===")      # 1. Start
letters = get_letters()

queue = []                                                 # 2. Create an empty queue
print("\nAn empty queue was created:", queue)

# 3-8. Enqueue each letter (added at the BACK of the queue)
print("\n--- ADDING PROCESS (ENQUEUE) ---")
for letter in letters:
    queue.append(letter)
    print("Enqueued", letter, "->", queue)

# 9. Display all letters in the queue
print("\nAll letters in the queue (front to back):", ", ".join(queue))

# 10-11. Dequeue the first letter, repeat until the queue is empty
print("\n--- REMOVING PROCESS (DEQUEUE) ---")
while len(queue) > 0:
    dequeued = queue.pop(0)                                # removes the FRONT letter
    print("Dequeued", dequeued, "->", queue)

# 12. Display "Queue is Empty"
print("\nQueue is Empty")
print("Final Output: Empty Queue", queue)
print("=== END ===")                                       # 13. Stop
