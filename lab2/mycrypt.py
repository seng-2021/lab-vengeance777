import codecs

# Maps digits to special chars and vice versa
digitmapping = dict(zip('1234567890!"#€%&/()=', '!"#€%&/()=1234567890'))
rev_digitmapping = {v: k for k, v in digitmapping.items()}


def encode(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    origlen = len(s)
    if origlen > 1000:
        raise ValueError("Input length exceeds 1000 characters")

    # Pad the string to length 1000 with 'A's for constant-time operation
    padded_string = s.ljust(1000, 'A')

    crypted_chars = []
    for c in padded_string:
        if not c.isascii():
            raise ValueError("Non-ASCII character detected")

        # Perform uniform operations
        upper_c = c.upper()
        rot13_c = codecs.encode(upper_c, 'rot13')
        mapped_char = digitmapping.get(c, None)

        if c.isalpha():
            crypted_chars.append(rot13_c)  # Use ROT13 result for letters
        elif mapped_char:
            crypted_chars.append(mapped_char)  # Use mapped result for digits/special chars
        else:
            raise ValueError(f"Invalid character detected: {c}")

    # Truncate the result to the original input length
    return ''.join(crypted_chars[:origlen])


def decode(s):
    return ''.join(
        codecs.encode(c, 'rot13').lower() if c.isalpha() else rev_digitmapping[c] for c in s)
