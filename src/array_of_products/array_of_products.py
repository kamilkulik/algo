# BRUTE FORCE

def array_of_products_brute(array):
    products = []
    for i in range(len(array)):
        running_product = 1
        for j in range(len(array)):
            if i != j:
                running_product *= array[j]
        products.append(running_product)
    return products

def array_of_products(array):
    products = [1 for _ in range(len(array))]
    left_array = [1 for _ in range(len(array))]
    right_array = [1 for _ in range(len(array))]

    running_product_left = 1
    for i in range(len(array)):
        left_array[i] = running_product_left
        running_product_left *= array[i]

    running_product_right = 1
    for i in reversed(range(len(array))):
        right_array[i] = running_product_right
        running_product_right *= array[i]

    for i in range(len(array)):
        products[i] = left_array[i] * right_array[i]

    return products


def array_of_products_optimised(array):
    products = [1 for _ in range(len(array))]

    running_product_left = 1
    for i in range(len(array)):
        products[i] *= running_product_left
        running_product_left *= array[i]

    running_product_right = 1
    for i in reversed(range(len(array))):
        products[i] *= running_product_right
        running_product_right *= array[i]

    return products