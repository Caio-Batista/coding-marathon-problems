
def cat_and_mouse(x, y, z):
    if z - y == y - x:
        return 'Mouse C'
    elif z - y < y - x:
        return 'Mouse B'
    else:
        return 'Mouse A'

if __name__ == '__main__':
    print(cat_and_mouse(1,2,3))