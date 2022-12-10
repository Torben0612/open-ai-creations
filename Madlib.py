# List of words to prompt the user for
words = ["noun", "adjective", "verb"]

# Story template with placeholder words (in angle brackets)
story = "The <noun> was very <adjective> and liked to <verb> all day."

# Prompt the user for each of the words in the list and store their responses
responses = {}
for word in words:
  response = input(f"Enter a {word}: ")
  responses[word] = response

# Insert the user's responses into the story template
madlib = story
for word, response in responses.items():
  madlib = madlib.replace(f"<{word}>", response)

# Print the completed madlib
print(madlib)
