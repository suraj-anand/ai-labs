import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There !, I'm Suraj"
# tokens = encoder.encode(text)
# print("Tokens:", tokens)
tokens = [25216, 3274, 1073, 11, 5477, 9568, 1255]

text = encoder.decode(tokens)
print("Text: ", text)