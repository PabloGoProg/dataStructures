from signly_linked_list import Node 
from signly_linked_list import linked_list
    
def run():
    ll = linked_list()
    ll.append_node('A')
    ll.append_node('B')
    ll.append_node('C')
    ll.append_node('D')
    ll.insert_node(5, 1)
    ll.print_list()


if __name__ == '__main__':
    run()
