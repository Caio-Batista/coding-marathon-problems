def best_glass(G1, G2, order):
    choice = G1
    if G1[1] > order and G2[1] < order:
        choice = G1
    elif G2[1] > order and G1[1] < order:
        choice = G2
    elif G1[1] - order < 0 and G2[1] - order < 0:
        return choice
    elif G1[1] - order < 0 and G2[1] - order >= 0:
        choice = G2
    elif G1[1] - order >= 0 and G2[1] - order < 0:
        choice = G1
    elif  G2[1] - order < G1[1] - order and G1[1] - order >= 0 and G2[1] - order >= 0:
        choice = G2
    else:
        choice = G1
    return choice 

def best_type(type1, type2, orders):
    type1_waste,type2_waste = type1[1],type2[1]
    best_waste = type1_waste
    best_type = type1[0]

    if type1_waste < 0 and type2_waste < 0:
        return [-1, -1]
    elif type1_waste >= 0 and type2_waste < 0:
        best_waste = type1_waste
        best_type = type1[0]
    elif type1_waste < 0 and type2_waste >= 0:
        best_waste = type2_waste
        best_type = type2[0]
    elif type1_waste > type2_waste and type1_waste >= 0 and type2_waste >= 0:
        best_waste = type2_waste
        best_type = type2[0]
    elif type1_waste == type2_waste:
        best_waste = type1_waste
        best_type = min(type1[0], type2[0])
    else:
        best_waste = type1_waste
        best_type = type1[0]

    return [best_type, best_waste]

def get_indexes(marks):
    indexes = {}
    for i in range(len(marks)):
        if indexes.get(f'{marks[i][0]}') is None:
            indexes[f'{marks[i][0]}'] = [i,i]
        if i > 0 and marks[i - 1][0] !=  marks[i][0]:
            indexes[f'{marks[i - 1][0]}'][1] = i - 1
    return indexes

def calculate_waste(glasses, orders):
    waste = 0
    for i in range(len(glasses)):
        waste += glasses[i][1] - orders[i]
        if glasses[i][1] - orders[i] < 0:
            waste = -1
    if waste < 0:
        waste = -1

    return [glasses[0][0], waste]

def choose_a_flask_h(orders, req, types, total_marks, marks, dict_glasses, type_index=0, temp2=[]):

    def mount(marks, last_index, order, glass_index=0):
        
        if glass_index == last_index:
            return marks[glass_index]

        current_glass = marks[glass_index]
        best = best_glass(current_glass, mount(marks, last_index, order, glass_index + 1), order)
             
        return best 

    if type_index == types - 1:
        
        temp3 = []
        for el in req:
            temp3.append(mount(marks, dict_glasses.get(f'{type_index}')[1], el, dict_glasses.get(f'{type_index}')[0]))
        return calculate_waste(temp3, req)

    
    temp = []
    for e in req:
        temp.append(mount(marks, dict_glasses.get(f'{type_index}')[1], e, dict_glasses.get(f'{type_index}')[0]))
    current_waste = calculate_waste(temp, req)
    best = best_type(
        current_waste,
        choose_a_flask_h(orders, req, types, total_marks, marks, dict_glasses, type_index + 1),
        req
    )

    temp2.append(best)
    return best


def choose_a_flask(orders, req, types, total_marks, marks):
    indexes = get_indexes(marks)

    return choose_a_flask_h(orders, req, types, total_marks, marks, indexes)[0]

if __name__ == "__main__":
    print(choose_a_flask(4, [4,6,6,7], 5, 9, [
        [0,3],
        [0,5],
        [1,7],
        [1,6],
        [2,8],
        [2,9],
        [3,3],
        [3,5],
        [4,6]
    ]))

    print(choose_a_flask(4, [4,6,6,7], 3, 9, [
        [0,3],
        [0,5],
        [0,7],
        [1,6],
        [1,8],
        [1,9],
        [2,3],
        [2,5],
        [2,6]
    ]))