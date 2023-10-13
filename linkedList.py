class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def Insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def Display(self):
        if self.head == None:
            print("linked list is empty")
        else:
            head_Itr = self.head
            Node_value = ""
            while head_Itr:
                Node_value += " " + str(head_Itr.data) + " -->"
                head_Itr = head_Itr.next
                print(Node_value)

    def Insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            # pointing at the last element :
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def Insert_New_Values(self, list_of_val):
        self.head = None
        for item in list_of_val:
            self.Insert_at_end(item)

    def Len_linked_list(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_at(self, index):
        if index < 0 and index > self.Len_linked_list():
            raise Exception("index error")
        if index == 0:
            self.head = self.head.next
            return
        counter = 0
        itr = self.head
        while itr:
            if (counter == index-1):
                itr.next = itr.next.next
                break
            counter += 1
            itr = itr.next

    def Insert_At(self, index, value):
        if index < 0 and index > self.Len_linked_list():
            raise Exception("index error")
        if index == 0:
            self.Insert_at_begining(value)
            return
        counter = 0
        itr = self.head
        while itr:
            if (counter == index-1):
                node = Node(value, itr.next)
                itr.next = node
                break
            counter += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        counter = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                break
            itr = itr.next
            counter += 1
        self.Insert_At(counter+1, data_to_insert)
        return

    def remove_by_value(self, data):
        counter = 0
        itr = self.head
        while itr:
            if (itr.data == data):
                self.remove_at(counter)
            counter += 1
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.Insert_at_begining(89)
    ll.Insert_at_begining(22)
    ll.Insert_at_begining(22)
    ll.Insert_at_end(12)
    ll.remove_at(2)
    ll.Insert_At(2, "banana")
    ll.remove_at(3)
    ll.insert_after_value("banana", "fruit")
    ll.remove_by_value("banana")
    print(ll.Len_linked_list())
    ll.Display()
