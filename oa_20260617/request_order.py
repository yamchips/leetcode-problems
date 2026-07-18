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
        server = heapq.heappop(heap)
        print(server.id)
        server.load += 1
        heapq.heappush(heap, 
                       (server.load / server.num_workers,
                        server.id,
                        server.num_workers,
                        server.load))
        