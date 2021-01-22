N = 100000

graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]

def dfs_cycle(u, p, color: list,
			mark: list, par: list):
    
    global cyclenumber

    if color[u] == 2:
        return None

    if color[u] == 1:
        cyclenumber += 1
        cur = p
        mark[cur] = cyclenumber

        while cur != u:
            cur = par[cur]
            mark[cur] = cyclenumber

        return

    par[u] = p

    color[u] = 1


    for v in graph[u]:
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, mark, par)

    color[u] = 2

def add_edge(u, v):
	graph[u].append(v)
	graph[v].append(u)

def print_cycles(edges, mark: list):
	for i in range(1, edges + 1):
		if mark[i] != 0:
			cycles[mark[i]].append(i)

	for i in range(1, cyclenumber + 1):
		print("Cycle Number %d:" % i, end = " ")
		for x in cycles[i]:
			print(x, end = " ")
		print()

# Driver Code
if __name__ == "__main__":

	# add edges
	add_edge(1, 2)
	add_edge(2, 3)
	add_edge(3, 4)
	add_edge(4, 6)
	add_edge(4, 7)
	add_edge(5, 6)
	add_edge(3, 5)
	add_edge(7, 8)
	add_edge(6, 10)
	add_edge(5, 9)
	add_edge(10, 11)
	add_edge(11, 12)
	add_edge(11, 13)
	add_edge(12, 13)

	color = [0] * N
	par = [0] * N

	mark = [0] * N

	cyclenumber = 0
	edges = 13

	dfs_cycle(1, 0, color, mark, par)

	print_cycles(edges, mark)

# This code is contributed by
# sanjeev2552
