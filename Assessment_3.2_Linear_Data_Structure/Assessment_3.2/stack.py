# Assessment 3.2 - Stack
# Adding and Removing Letters Using Stack
# A stack is LIFO (Last In, First Out): the last letter pushed is the first one popped.

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
print("=== STACK: Adding and Removing Letters ===")      # 1. Start
letters = get_letters()

stack = []                                                 # 2. Create an empty stack
print("\nAn empty stack was created:", stack)

# 3-8. Push each letter into the stack (the end of the list is the TOP)
print("\n--- ADDING PROCESS (PUSH) ---")
for letter in letters:
    stack.append(letter)
    print("Pushed", letter, "->", stack, "(top is", stack[-1] + ")")

# 9. Display all letters in the stack
print("\nAll letters in the stack (bottom to top):", ", ".join(stack))

# 10-11. Pop the top letter, repeat until the stack is empty
print("\n--- REMOVING PROCESS (POP) ---")
while len(stack) > 0:
    popped = stack.pop()                                   # removes the TOP letter
    print("Popped", popped, "->", stack)

# 12. Display "Stack is Empty"
print("\nStack is Empty")
print("Final Output: Empty Stack", stack)
print("=== END ===")                                       # 13. Stop
