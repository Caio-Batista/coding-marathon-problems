def min_sum_of_max_elems_from_d_cuts(L, d):
    assert len(L) >= d
    def find_best_cut(i, cuts):
        if len(cuts) == d and i == len(L):
            return sum(cuts)
        elif len(cuts) > d or i >= len(L):
            return float("inf")

        best = float("inf")

        if cuts: 
            new_cuts = cuts[:-1] + (max(cuts[-1], L[i]),)
            best = min(best, find_best_cut(i + 1, new_cuts))

        return min(best, find_best_cut(i + 1, cuts + (L[i],)))

    return find_best_cut(i=0, cuts=tuple())

if __name__ == "__main__":
    tests = [
        dict(L=[10,2,20,5,15,10,1], d=3, result=31),
        dict(L=[10,2,20,5,15,10,1], d=5, result=43),
    ]

    for test in tests:
        assert min_sum_of_max_elems_from_d_cuts(test["L"], test["d"]) == test["result"]
        print(min_sum_of_max_elems_from_d_cuts(test["L"], test["d"]))
