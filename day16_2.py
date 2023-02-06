
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        self.llink = None

def print_nodes(start):
        current = start
        if current == None:
            return
        print(current.data, end=' ')
        while current.link != start:
            current = current.link
            print(current.data, end=' ')
        print()


# def print_nodes2(start):
#     current = start
#     if current == None:
#         return
#     print(current.data, end=' ')
#     while current.llink != start:
#         current = current.llink
#         print(current.data, end=' ')
#     print()

data_array = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == "__main__":
    node = Node(data_array[0])
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print_nodes(head)

    node = Node(data_array[-1])
    head = node
    node.link = head

    for data in data_array[len(data_array) - 2::-1]:
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print_nodes(head)