from double_linked_list import DoubleLinkedList
    
def run():
    ll = DoubleLinkedList()
    ll.append_node(1)
    ll.append_node(2)
    ll.append_node(3)
    ll.pop()
    ll.pop()
    ll.pop()
    ll.print()

if __name__ == '__main__':
    run()
