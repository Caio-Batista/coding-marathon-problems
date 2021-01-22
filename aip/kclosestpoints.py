def kclosest_points(points, K):
    points.sort(key = lambda K: K[0]**2 + K[1]**2)
    return points[:K]
 
if __name__ == "__main__":
    print(kclosest_points([[3, 3], [6, 1], [-2, 4], [5, -1],], 2))
