# --- Method 1: Counting characters with a 'for' loop ---

word = input("Enter a word (or any text): ")
count = 0

# Loop through each character in the string
for char in word:
    count = count + 1 # Increment the counter for each character

print(f"The number of letters (using a loop) is: {count}")


### A more efficient way to do it ###

# --- Method 2: Counting characters with the built-in len() function ---

word = input("Enter a word (or any text): ")

# The len() function automatically counts the elements in a sequence
print(f"The number of letters (using len()) is: {len(word)}")


### Another example: Counting words (simple) ###

# --- Method 3: Simple word counting by counting spaces ---

phrase = "Hola Mundo" # "Hello World"
word_count = 1 # Start at 1, assuming there is at least one word

for char in phrase:
    if char == " ": # If the character is a space
        word_count += 1 # Increment the word counter

print(f"The number of words is: {word_count}")