def count_while(s, value):
    """Count the number of occurrence of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if value == s[index]:
            total += 1
        index += 1
    return total

def count_for(s, value):
    total = 0
    for item in s:
        if item == value:
            total += 1
    return total
