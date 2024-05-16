Pseudocode:

```
graph:
    ways = { "1":[ ["2", [u1, ... ]], ... ], ... }
    keys = { "1":[u1, ...], ... }

host0

ways_queue = queue(graph.ways[host0])
additional_host_parameters

while queue not empty:
    
    next_path_queue = queue()
    keys_to_add = {}
    while not checked ways in path_queue:
        way = ways_queue.get_unchecked()
        if way is reachable by comparing keys we have and keys needed:
            
            host = way[0]
            w = get_waight(host)
            
            remember_iteration_of_host(host)
            mark_chacked(host)
            
            waight_host(host, w)
            
            keys_to_add.append(graph.keys(host))
            new_ways = graph.ways[host]
            path_queue.append(new_ways)
```