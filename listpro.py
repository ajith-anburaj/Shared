class node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

class llist:
    def __init__(self):
        self.first=None
        self.last=None

    def push(self,data):
        item=node(data)
        if self.first == None:
            self.first=item
            self.last=item
        else:
            item.next=self.first
            self.first=item

    def append(self,data):
        item=node(data)
        if self.last==None and self.first==None:
            self.first=item
            self.last.item

        else:
            self.last.next = item
            self.last = item

    def prlist(self):
        print("\n")
        head=self.first
        while head:
            print("{}".format(head.data), end=' ')
            head=head.next

    def inspos(self, data, pos):
        """if pos=1 wy do u want use this function go to push()"""
        cnt=0
        item=node(data)
        temp=self.first
        while temp :
            cnt+=1
            temp=temp.next

        temp2=self.first
        if pos > 1 and pos < cnt :
            for i in range(1,pos):
                t1=temp2
                temp2=temp2.next

            item.next=temp2
            t1.next=item

            print("list inserted")
        else:
            print("pos outta range!!")

    def search(self,key):
        temp=self.first
        pos=1
        found=False
        while temp:
            if temp.data==key:
                found=True
                break
            else:
                pos+=1
                temp=temp.next

        if found :
            print("\n ur key {} found at pos {}".format(key,pos),end=' ')
        else:
            print("you gotta be kidding me \n sry thr is no such key/data")

    def swap_nodes(self,x,y):
        """dont use end nodes just nodes between 2 to 5(including) if ur list length is 6"""

        tempx=self.first
        while tempx and tempx.data != x:
            prevx=tempx
            tempx=tempx.next

        tempy=self.first
        while tempy and tempy.data != y:
            prevy=tempy
            tempy=tempy.next

        if prevx != None and prevy != None:
            prevx.next=tempy
            prevy.next=tempx

        temp=tempx.next
        tempx.next=tempy.next
        tempy.next=temp

    def rev_nodes(self):
        np=None
        prev=None

        current=self.first
        while current != None:
            np=current.next
            current.next=prev
            prev=current
            current=np

        self.first=prev

    def sort(self):
        tempx=self.first


        while tempx :
            tempy=tempx.next
            while tempy :
                if tempx.data > tempy.data:
                    temp=tempx.data
                    tempx.data=tempy.data
                    tempy.data=temp

                tempy=tempy.next

            tempx=tempx.next


if __name__ == '__main__':
    l=llist()
    l.push(20)
    l.push(10)
    l.push(5)
    l.append(25)
    l.append(30)
    l.inspos(9,3)
    l.search(9)
    l.prlist()
    l.swap_nodes(9,25)
    print("after swapping nodes")
    l.prlist()
    l.sort()
    print("after sorting")
    l.prlist()
    print("after reversing")
    l.rev_nodes()
    l.prlist()