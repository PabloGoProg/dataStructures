from re import A
from signly_linked_list import Node 
from signly_linked_list import linked_list
    
def run():
    ll = linked_list()
    ll.append_node('A')
    ll.append_node('B')
    ll.append_node('C')
    ll.append_node('D')
    ll.remove_by_index(2)
    ll.print_list()


if __name__ == '__main__':
    run()
