#!/usr/bin/python3
""" find peak """


def find_peak(list_of_integers):
    """ this function for finding peak"""
    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = (left + right) // 2
        middle = list_of_integers[mid]
        before = list_of_integers[mid - 1]
        after = list_of_integers[mid + 1]

        # Check if the middle element is greater than its neighbors
        if ((mid == 0) or (middle > before)) and \
                ((mid == len(list_of_integers) - 1) or (middle > after)):
            return list_of_integers[mid]
        # If the middle element is not a peak,
        # move towards the side where the neighbor is larger
        elif mid != 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Return None if no peak is found
    return None
