import math
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None :
        return
    print(f'{current.data[0]}, 거리 : {math.sqrt((current.data[1]**2 + current.data[2]**2))}', end='\n')
    while current.link != start:
        current = current.link
        print(f'{current.data[0]}, 거리 : {math.sqrt((current.data[1]**2 + current.data[2]**2))}', end='\n')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre
    while True:
        if math.sqrt((head.data[1]**2 + head.data[2]**2)) > find_data:
            node = Node(insert_data)
            node.link = head
            last = head
            while last.link != head:
                last = last.link
            last.link = node
            head = node
            return


        current = head
        while current.link != head:
            pre = current
            current = current.link
            if math.sqrt((current.data[1]**2 + current.data[2]**2)) > find_data:
                node = Node(insert_data)
                node.link = current
                pre.link = node
                return

        node = Node(insert_data)
        current.link = node
        node.link = head
        break


head, current, pre = None, None, None
store_name = 'A'
dataArray = []
for i in range(0, 10):
    dataArray.insert(i, (f"{chr(ord(store_name) + i)} 편의점", random.randint(1, 100), random.randint(1, 100)))

print(dataArray)

if __name__ == "__main__":
    node = Node(dataArray)
    node.data = dataArray[0]
    head = node
    node.link = head

    for i in (range(1, len(dataArray))):
        insert_nodes(math.sqrt((dataArray[i][1]**2 + dataArray[i][2]**2)), dataArray[i])

    print_nodes(head)