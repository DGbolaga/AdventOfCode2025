
def get_path(G, node, dp):
    if G[node] == ['out']:
        return 1
    
    if node in dp:
        return dp[node]
    
    ans = 0
    for x in G[node]:
        ans += get_path(G, x, dp)

    dp[node] = ans
    return dp[node]




if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        input = [x.split() for x in file.readlines()]

    Graph = {x[0][:-1]:x[1:] for x in input}
    dp = {}
    
    print(Graph)
    print(get_path(Graph, 'you', dp))
