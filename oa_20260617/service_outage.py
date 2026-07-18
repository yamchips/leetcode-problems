from collections import defaultdict


def service_outage(services: list, service_outages: list[str], target_service: str) -> str:
    # build a map, key: parent, value: [child1, child2]
    parent_children = defaultdict(list)
    for service in services:
        child, parents = service
        if parents:
            for parent in parents:
                parent_children[str(parent)].append(str(child))
    
    # check each outaged service
    outages = set(service_outages)
    for outage in service_outages:
        stack = parent_children[outage].copy()
        while stack:
            node = stack.pop()
            if node in outages:
                continue
            outages.add(node)
            stack.extend(parent_children[node])

    # given target, check whether it's in outages
    if target_service in outages:
        return "Full Outage"
    # if not, check its all direct children
    for child in parent_children[target_service]:
        if child in outages:
            return "Partial Outage"
    # if not, it's Operational
    return "Operational"