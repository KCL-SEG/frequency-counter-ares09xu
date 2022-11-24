"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        itemStr = str(item)
        if not itemStr in frequencies:
            frequencies[itemStr] = 1
        else:
            up_frequencies = {itemStr : frequencies[itemStr] + 1}
            frequencies.update(up_frequencies)
    return frequencies
