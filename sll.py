class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        llstr =''
        while temp:
            llstr += str(temp.data) + '-->'
            temp = temp.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None)

    #function that will take a list of values as input and create a new linked list
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    #function to get the length of the linked list
    def get_length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count

    #function to remove an element at a given index
    def remove_at(self,index):
        if index<0 or index>=self.get_length():#check if the index is valid
            raise Exception("Not a valid index")
        if index==0:    #suppose you are trying to remove the head
            self.head=self.head.next #make the next node the head node
            return #At this point, the old head node no longer has any references pointing to it, so it becomes eligible for garbage collection.
        count=0
        temp=self.head
        while temp:
            if count == index-1:
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():#check if the index is valid
            raise Exception("Not a valid index")
        if index==0:
            self.insert_at_beginning(data)
            return
        count = 0
        temp = self.head
        while temp:
            if count == index-1:
                node = Node(data,temp.next)
                temp.next= node
                break
            temp=temp.next
            count+=1

    def insert_after_value(self,data_after,data_to_insert):
        temp=self.head
        while temp:
            if data_after == temp.data:
                node = Node(data_to_insert,temp.next)
                temp.next=node
                break
            temp=temp.next
        else:
            raise Exception(f"Value {data_after} not found in th linked list")

    def remove_by_value(self,data):
        if self.head is None:
            print("Linked list is Empty")
            return

        if self.head.data == data:
            # If the data to remove is in the head node, update the head.
            self.head=self.head.next
            return

        temp=self.head
        while temp.next is not None and temp.next.data!=data:
            temp=temp.next

        if temp.next is not None:
            # Found the data in the next node; remove it by skipping it.
            temp.next = temp.next.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(20)
    ll.print()
    ll.insert_at_end(99)
    ll.print()
    ll.insert_at_beginning(1)
    ll.print()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    length = ll.get_length()
    print(length)
    ll.remove_at(2)
    ll.print()
    ll.insert_at(0,"figs")
    ll.print()
    newlength = ll.get_length()
    print(newlength)
    ll.insert_at(3,"jackfruit")
    ll.print()
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
