from util import Queue
# data structure = (parent, child)
def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    path = [starting_node]
    
    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()
        print("Current Path: ", current_path)

        new_path = []
        updated = False

        for node in current_path:
            for prev_node in ancestors:
                if prev_node[1] == node:
                    new_path.append(prev_node[0])
                    updated = True
                    print("New Path: ", new_path)
                    q.enqueue(new_path)

        if updated == False:
            if current_path[0] == starting_node:
                print(-1)
                return -1
            else:
                return current_path[0]
