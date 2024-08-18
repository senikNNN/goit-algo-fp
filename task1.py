class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елементу в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Виведення списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next  # Збереження наступного вузла
        current.next = prev  # Зміна напрямку посилання
        prev = current  # Переміщення prev та current на один крок вперед
        current = next_node
    linked_list.head = prev

def sorted_insert(sorted_list, new_node):
    if not sorted_list.head or sorted_list.head.data >= new_node.data:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

def insertion_sort(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        next_node = current.next
        sorted_insert(sorted_list, Node(current.data))
        current = next_node
    linked_list.head = sorted_list.head

def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.data <= p2.data:
            merged_list.append(p1.data)
            p1 = p1.next
        else:
            merged_list.append(p2.data)
            p2 = p2.next

    # Додавання залишкових елементів
    while p1:
        merged_list.append(p1.data)
        p1 = p1.next

    while p2:
        merged_list.append(p2.data)
        p2 = p2.next

    return merged_list

# Створення однозв'язного списку
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(5)
ll.append(2)
ll.append(4)

print("Початковий список:")
ll.print_list()

# Реверсування списку
reverse_list(ll)
print("Список після реверсування:")
ll.print_list()

# Сортування списку
insertion_sort(ll)
print("Список після сортування вставками:")
ll.print_list()

# Об'єднання двох відсортованих списків
ll2 = LinkedList()
ll2.append(6)
ll2.append(7)
ll2.append(8)

merged_list = merge_sorted_lists(ll, ll2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
