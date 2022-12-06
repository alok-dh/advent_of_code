# read given input into python
with open('input.txt') as input_text:
    text = input_text.read()


def offset(buffer, marker) -> int:
    i = 0
    while i < len(buffer):
        chars = buffer[i:i + marker]
        if len(set(chars)) == marker:
            return i + marker
        i += 1


# Part 1
# The start of a packet is indicated by a sequence of four characters that are all different.
# How many characters need to be processed before the first start-of-packet marker is detected?
print(f"Part 1: {offset(text, 4)}")
# Part 2
# A start-of-message marker is just like a start-of-packet marker,
# except it consists of 14 distinct characters rather than 4.
# How many characters need to be processed before the first start-of-message marker is detected?
print(f"Part 2: {offset(text, 14)}")
