class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    def add_at_first(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def __str__(self):
        temp=self.head
        l=""
        while temp:
            l=l+f"{temp.data}"+"->"
            temp=temp.next
        return l+"None"
    def add_at_last(self,data):
        node=Node(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node
        else:
            self.head=node
    def __len__(self):
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        return c
    def add_in_between(self,prev,data):
        temp=self.head
        if not self.head:
            return "The SLL is empty."
        while temp and temp.data != prev:
            temp=temp.next
        if temp:
            node=Node(data)
            node.next=temp.next
            temp.next=node
        else:
            print("Node doesn't exist")
    def __getitem__(self,pos):
        temp=self.head
        count=0
        while temp:
            if count==pos:
                return temp
            temp=temp.next
            count+=1
        else:
            print("No value found for given position.")
    def add_at_index(self,data,index):
        if index==0:
            self.add_at_first(data)
            return
        last=len(self)
        if index==last:
            self.add_at_last(data)
        elif 0<index<last:
            self.add_in_between(self[index-1],data)
        else:
            print("Index doesn't exist.")
    def delete_first(self):
        temp=self.head
        if temp:
            self.head=temp.next
            temp.next=None
            del temp
        else:
            print("The SLL is empty.")
    def delete_last(self):
        if not self.head:
            print("The SLL is empty.")
        elif not self.head.next:
            self.head=None
        else:
            temp=self.head
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            del temp
        #last=len(self)
        #get_item=self[last-2]
        #get_item.next=None
    def delete_in_between(self,pos):
        if pos==0:
            self.delete_first()
            return
        last=len(self)
        if pos==last:
            self.delete_last()
        elif 0<pos<last:
            get_prev=self[pos-1]
            get_prev.next=self[pos+1]
            self[pos].next=None
        else:
            print("Index doesn't exist.")
    def linear_search(self,data):
        index=0
        if not self.head:
            return "The SLL is empty."
        temp=self.head
        while temp:
            if temp.data==data:
                return index
            else:
                temp=temp.next
                index+=1
        else:
            print("Element not found.")
    def bubble_sort(self):
        i=0
        last=len(self)
        while i<last:
            j=0
            while j<last-(i+1):
                if self[j].data>self[j+1].data:
                    self[j].data,self[j+1].data=self[j+1].data,self[j].data
                j+=1
            j+=1
    def update(self,old,new):
        temp=self.head
        while temp:
            if temp.data==old:
                temp.data=new
                return
            temp=temp.next
        print("Node doesn't exist")
    def binary_search(self,t):
        l=0
        r=len(self)-1
        while l<=r:
            mid=(l+r)//2
            mid_node=self[mid]
            if not mid_node:
                return -1
            if mid_node.data==t:
                return mid
            elif mid_node.data<t:
                l=mid+1
            else:
                r=mid-1
        return -1
    def reverse(self):
##        temp=self.head
##        res=SLL()
##        while temp:
##            res.add_at_first(temp.data)
##            temp=temp.next
##        return str(res)
        temp=self.head
        prev=None
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        self.head=prev

    def middle_element(self):
        mid=len(self)//2
        print(self[mid].data)

    def remove_duplicate(self):
        temp=self.head
        seen=set()
        while temp:
            if temp.data in seen:
                prev.next=temp.next
            seen.add(temp.data)
            prev=temp
            temp=temp.next            
        print(self)

    def nth_element(self,n):
        length=len(self)
        x=length-n
        print(self[x].data)
        
obj=SLL()
obj.add_at_last(10)
obj.add_at_last(20)
obj.add_at_last(30)
obj.add_at_last(40)
obj.add_at_last(50)
