#!/usr/bin/python3


def canUnlockAll(boxes):
    '''function takes a list of lists of boxes that contain keys
    and determines whether all boxes can be opened.

    returns True if all boxes can be opened or False otherwise
    '''

    unlocked_boxes = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes \
               and key != box_id:
                unlocked_boxes.append(key)

    if len(unlocked_boxes) == len(boxes):
        return True
    return False
