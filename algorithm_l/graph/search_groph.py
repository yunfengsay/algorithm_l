from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = ["abc-mongo"]
graph["jonny"] = []



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("persion {} is a mango seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
def person_is_seller(name):
    return name[-6:] == '-mongo'
search("you")