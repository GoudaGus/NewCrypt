"""Encode and decode text."""

import codecs


def encode(input_str):
    """Encode text to decimal."""
    return int(codecs.encode(bytes(input_str, encoding="utf-8"), "hex"), 16)


def decode(input_int):
    """Decode decimal to text."""
    output_str = str(codecs.decode(str(hex(input_int))[2:], "hex"))
    return output_str[2:len(output_str) - 1]


if __name__ == "__main__":
    print("Please use via UI.py")
