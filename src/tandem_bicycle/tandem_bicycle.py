# COMPLEXITY
# TIME: O(nlog(n))
# SPACE: O(1)

def tandem_bicycle(blue_shirt_speeds, red_shirt_speeds, fastest):
    blue_shirt_speeds.sort() # smallest to greatest
    red_shirt_speeds.sort(reverse=True) # greatest to smallest
    tandem_speed = 0

    for idx in range(len(blue_shirt_speeds)):
        blue_shirt = blue_shirt_speeds[idx]
        red_shirt = red_shirt_speeds[idx] if fastest else red_shirt_speeds[len(red_shirt_speeds) -1 - idx]

        tandem_speed += max(red_shirt, blue_shirt)

    return tandem_speed

def tandem_bicycle_with_reverse(blue_shirt_speeds, red_shirt_speeds, fastest):
    blue_shirt_speeds.sort()
    red_shirt_speeds.sort()
    cumulative_speed = 0

    if fastest:
        reverse_array_in_place(red_shirt_speeds)

    for idx in range(len(blue_shirt_speeds)):
        blue_shirt_speed = blue_shirt_speeds[idx]
        red_shirt_speed = red_shirt_speeds[idx]

        cumulative_speed += max(blue_shirt_speed, red_shirt_speed)
    
    return cumulative_speed


def reverse_array_in_place(array):
    start = 0
    end = len(array) -1
        
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1