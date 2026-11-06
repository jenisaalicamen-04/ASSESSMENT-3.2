# Assessment 3.2 - Array
# Adding and Removing Letters Using Array

# ---------- Get the letters from the user ----------
def get_letters():
    default = ["R", "O", "S", "I", "M", "A"]
    text = input("Enter your letters (example: ROSIMA) or press Enter to use R, O, S, I, M, A: ")
    letters = []
    for ch in text:
        if ch.isalpha():              # keep letters only (ignore spaces and commas)
            letters.append(ch.upper())
    if len(letters) == 0:             # nothing typed -> use the default letters
        letters = default
    return letters


# ---------- Main program ----------
print("=== ARRAY: Adding and Removing Letters ===")      # 1. Start
letters = get_letters()

array = []                                                 # 2. Create an empty array
print("\nAn empty array was created:", array)

# 3-8. Add each letter to the array
print("\n--- ADDING PROCESS ---")
for letter in letters:
    array.append(letter)
    print("Added", letter, "->", array)

# 9. Display all letters in the array
print("\nAll letters in the array:", ", ".join(array))

# 10-12. Remove the first letter, shift the rest, repeat until empty
print("\n--- REMOVING PROCESS ---")
while len(array) > 0:
    removed = array[0]                        # 10. Take the first letter
    # 11. Move the remaining letters one position to the left
    for i in range(1, len(array)):
        array[i - 1] = array[i]
    array.pop()                               # remove the leftover last slot
    print("Removed", removed, "->", array)

# 13. Display "Array is Empty"
print("\nArray is Empty")
print("Final Output: Empty Array", array)
print("=== END ===")                                       # 14. Stop
