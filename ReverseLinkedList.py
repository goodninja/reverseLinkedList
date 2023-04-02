# Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
# Реализация разворота связного списка на Python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def set_next(self, value):
        self.next = Node(value)
        return self.next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current))
            current = current.next

        return ' -> '.join(values)

    def reverse(self):
        previous = None
        current = self.head

        while current.next:

            tmp = current.next

            current.next = previous

            previous = current
            current = tmp

        current.next = previous

        self.head = current

# Перевернём 1 -> 2 -> 3 -> 4 -> 5, в результате получим 5 -> 4 -> 3 -> 2 -> 1


if __name__ == "__main__":

    head = Node('1')
    head.set_next('2').set_next('3').set_next('4').set_next('5')

    ll = LinkedList(head)
    print(ll)
    ll.reverse()
    print(ll)
