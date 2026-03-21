def warn_the_sheep(queue):
    queue.reverse()
    if queue[0]=="wolf":
        return "Pls go away and stop eating my sheep"
    else:
        for i in queue:
            if i=='wolf':
                return f"Oi! Sheep number {queue.index(i)}! You are about to be eaten by a wolf!"