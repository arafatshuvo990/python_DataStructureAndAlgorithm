my_favourite_quote = "The only limit to our realization of tomorrow is our doubts of today."

print(my_favourite_quote)
print(f"Length of the quote: {len(my_favourite_quote)} characters")
print(f"Letter finding : {my_favourite_quote [3:48]}")

#encode
spaninsh_quote = "La única limitación para nuestra realización del mañana son nuestras dudas de hoy."
encode = spaninsh_quote.encode("utf-8")
decode = encode.decode("utf-8")
print(f"Original quote: {spaninsh_quote}")
print(f"Encoded quote: {encode}")
print(f"Decoded quote: {decode}")