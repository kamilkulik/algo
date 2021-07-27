# in sorted array, next coin cannot be greater than
# than the sum of all previous coins + 1

def non_constructible_change(coins):
    current_change_created = 0
    coins.sort()

    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1

        current_change_created += coin
        
    return current_change_created + 1