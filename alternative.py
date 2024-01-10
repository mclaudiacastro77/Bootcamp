# Write a program that reads in a string and makes each alternate
# character into an upper case character and each other alternate character a lower case character.

string = "Hello World! I am learning to code."
final_string = ""

for i in range(len(string)):
    if i % 2 == 0:
        final_string += string[i].upper()
    else:
        final_string += string[i].lower()
print(final_string)

# Start with the same string but making each alternative word lower and upper case.

sentence = "Hello World! I am learning to code."
words = sentence.split()  # Split the sentence into a list of words
modified_words = [] 

for i in range(len(words)):
    if i % 2 == 1: 
        modified_words.append(words[i].upper()) # If the index is odd, append the word in uppercase
    else:
        modified_words.append(words[i].lower())
print(modified_words)

text = " ".join(modified_words) # Join the modified words into a single string
print(text)
