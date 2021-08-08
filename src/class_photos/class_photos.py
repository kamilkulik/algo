# all students wearing red shirts need to be in the same row
# all students wearing blue shirts need to be in the same row
# each student in the back row needs to be strictly taller than the student in front in the front row
# two inputs array are always gonna be of the same length, each height will be a positive integer
# check whether the photo can be taken

# "redShirtHeights": [5, 8, 1, 3, 4],
# "blueShirtHeights": [6, 9, 2, 4, 5]


def class_photos(red_shirt_heights, blue_shirt_heights):
    # 1. Sort both arrays with reversed option set to True - the biggest elements will determine comparison direction

    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    # 2. Determine which team should be in first row

    team_in_first_row = "RED" if red_shirt_heights[0] < blue_shirt_heights[0] else "BLUE"

    # 3. Loop over both arrays and check if each student in first row is smaller than student in back row

    for idx in range(len(red_shirt_heights)):
        if team_in_first_row == "RED":
            if red_shirt_heights[idx] >= blue_shirt_heights[idx]:
                return False
        elif team_in_first_row == "BLUE":
            if blue_shirt_heights[idx] >= red_shirt_heights[idx]:
                return False

    return True