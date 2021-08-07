from src.class_photos.class_photos import class_photos

def tet_class_photos_1():
    red_shirt_heights = [6]
    blue_shirt_heights = [6]
    
    assert class_photos(red_shirt_heights, blue_shirt_heights) == False
    
def tet_class_photos_2():
    red_shirt_heights = [6, 9, 2, 4, 5, 1]
    blue_shirt_heights = [5, 8, 1, 3, 4, 9]
    
    assert class_photos(red_shirt_heights, blue_shirt_heights) == False

def tet_class_photos_3():
    red_shirt_heights = [1, 2, 3, 4, 5]
    blue_shirt_heights = [2, 3, 4, 5, 6]
    
    assert class_photos(red_shirt_heights, blue_shirt_heights) == False

def tet_class_photos_4():
    red_shirt_heights = [1, 1, 1, 1, 1, 1, 1, 1]
    blue_shirt_heights = [2, 2, 2, 2, 2, 2, 2, 2]
    
    assert class_photos(red_shirt_heights, blue_shirt_heights) == True

def tet_class_photos_5():
    red_shirt_heights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
    blue_shirt_heights = [21, 5, 4, 4, 4, 4, 4, 4, 4]
    
    assert class_photos(red_shirt_heights, blue_shirt_heights) == False
