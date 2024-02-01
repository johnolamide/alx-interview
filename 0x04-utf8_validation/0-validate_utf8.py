#!/usr/bin/python3
"""
This script contains the validUTF8 function definition
"""


def validUTF8(data):
    """ function determines a given data set represents a valid UTF-8 encoding
        Args:
            data: data to validate
        Return:
            return True if valid else False
    """
    count = 0
    for num in data:
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                return (False)
        else:
            if (num >> 6) != 0b10:
                return (False)
            count -= 1

    return (count == 0)
