import json

def getQuote():
    # Read quotes from the file
    with open('quotes.json', 'r') as f:
        quotes = json.load(f)
    
    # Check if there are quotes available
    if not quotes:
        return "No quotes found"
    
    # Get the first quote and remove it from the list
    quote = quotes.pop(0)

    # Save the updated list back to 'quotes.json'
    with open('quotes.json', 'w') as f:
        json.dump(quotes, f, indent=4)  # Writing remaining quotes back to the file

    # Add the first quote to 'used_quotes.json'
    try:
        # If the 'used_quotes.json' exists, append the new quote
        with open('used_quotes.json', 'r') as f:
            used_quotes = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        used_quotes = []

    # Append the first quote to the used quotes
    used_quotes.append(quote)

    # Write the updated list to 'used_quotes.json'
    with open('used_quotes.json', 'w') as f:
        json.dump(used_quotes, f, indent=4)

    return quote