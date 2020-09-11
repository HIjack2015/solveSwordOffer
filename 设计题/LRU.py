from collections import OrderedDict


class D_link_node:
    def __init__(self, key, value):
        self.prefix = None
        self.next = None
        self.key = key
        self.value = value


class D_link_list:

    def __init__(self):
        self.head = D_link_node(-1, -1)
        self.tail = D_link_node(-1, -1)

        self.head.next = self.tail
        self.tail.prefix = self.head
        self.length = 0

    def remove_node(self, node):
        left_ele = node.prefix
        right_ele = node.next
        left_ele.next = right_ele
        right_ele.prefix = left_ele

        node.prefix.next = node.next
        self.length -= 1

    def add_in_head(self, node: D_link_node):
        last_next = self.head.next
        node.next = last_next
        node.prefix = self.head
        last_next.prefix = node
        self.head.next = node
        self.length += 1

    def remove_tail(self):
        real_tail = self.tail.prefix

        if real_tail == self.head:
            return
        self.remove_node(real_tail)
        return real_tail

    def move_to_left(self, node: D_link_node):
        self.remove_node(node)
        self.add_in_head(node)

    def __len__(self):
        return self.length


class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = dict()
        self.d_link_list = D_link_list()

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self.d_link_list.move_to_left(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self.d_link_list.move_to_left(node)
        else:
            node = D_link_node(key, value)
            self.d_link_list.add_in_head(node)

        self.key_node[key] = node
        if len(self.d_link_list) > self.capacity:
            ele_to_remove = self.d_link_list.remove_tail()
            self.key_node.pop(ele_to_remove.key)

        return


obj = LRUCache(1)
obj.put(2, 1)

print(obj.get(2))
