import heapq


def calculate_server_request_order(incoming_requests: int, servers: list) -> None:
    heap = []
    for server in servers:
        ratio = server.load / server.num_workers
        heapq.heappush(heap, 
                       (ratio, 
                        server.id, 
                        server.num_workers, 
                        server.load))
    for _ in range(incoming_requests):
        _, id, num_workers, load = heapq.heappop(heap)
        print(id)
        load += 1
        heapq.heappush(heap, 
                       (load / num_workers,
                        id,
                        num_workers,
                        load))
        