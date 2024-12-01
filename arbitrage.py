import math

def bellman_ford(graph, source):
    """
    Bellman-Ford algorithm to find shortest paths and detect negative weight cycles.
    """
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return True, predecessors  # Negative cycle detected

    return False, predecessors


def find_negative_cycle(predecessors, start):
    """
    Extract the negative cycle from the predecessors.
    """
    cycle = []
    visited = set()
    node = start

    # Find a cycle
    for _ in range(len(predecessors)):
        node = predecessors[node]

    # Record the cycle
    start_cycle = node
    while True:
        cycle.append(node)
        node = predecessors[node]
        if node == start_cycle:
            cycle.append(node)
            break

    return cycle[::-1]  # Reverse the cycle for correct order


def arbitrage(currencies, rates):
    """
    Detect arbitrage opportunities in currency exchange rates.
    """
    # Build graph with negative log weights
    graph = {currency: [] for currency in currencies}
    for i, src in enumerate(currencies):
        for j, dst in enumerate(currencies):
            if i != j:
                rate = rates[i][j]
                graph[src].append((dst, -math.log(rate)))

    # Run Bellman-Ford from any starting node
    for currency in currencies:
        has_cycle, predecessors = bellman_ford(graph, currency)
        if has_cycle:
            # Find and return the negative cycle
            cycle = find_negative_cycle(predecessors, currency)
            return cycle

    return None


if __name__ == "__main__":
    # Example currencies and exchange rates (rates[i][j] = rate from currencies[i] to currencies[j])
    currencies = ["USD", "EUR", "GBP", "JPY"]
    rates = [
        [1, 0.85, 0.75, 110],
        [1.18, 1, 0.88, 129],
        [1.33, 1.14, 1, 146],
        [0.0091, 0.0078, 0.0068, 1]
    ]

    # Find arbitrage
    cycle = arbitrage(currencies, rates)

    if cycle:
        print("Arbitrage opportunity detected!")
        print("Cycle:", " -> ".join(cycle))
    else:
        print("No arbitrage opportunity found.")
