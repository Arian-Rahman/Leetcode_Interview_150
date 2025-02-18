class Node : # This is for individual nodes
    def __init__(self,value):
        self.value = value # data to store in this node
        self.next =  None # pointer to next node , initially none
        
class LinkedList : # this is for the linked list chain,will link Nodes together 
    def __init__(self):
        self.head = None # Linked list's head , initially none 
        
    # Totorial 1 : Append, prepend , disply , delete by value 
    
    def append(self,value): 
        """
        Appends a value at the end of the LL
        """
        new_node = Node(value) # create the node 
        if not self.head : # if the head of the list is empty, then the list itself is empty 
            self.head = new_node
            return
        node_itr = self.head
        while node_itr.next : # while the iterator has a next value linked  
            node_itr = node_itr.next
        
        node_itr.next = new_node #link the new node to the previous last node's next 
        
    def prepend(self,value): 
        """
        Adds new node at the beginning 
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def display(self): 
        """
        Display all nodes in linked list in order 
        """
        node_itr = self.head
        if node_itr == None:
            print("Linked List is empty")
        else:
            while node_itr:
              print(f"{node_itr.value}-->")
              node_itr=node_itr.next
              
    def delete_by_value(self,value):  
        """
        Deletes the left most node with matching value 
        """
        if not self.head :
            return
        if self.head.value == value:
            self.head = self.head.next # make the previous head node's next , into the new head 
            return
            
        node_itr = self.head
        # ensures that we stop at the node whose next node contains the value to delete.
        while node_itr.next and node_itr.next.value != value:
            node_itr = node_itr.next 
        # since we stopped at the previous node of the node to delete, we need to make a jump to the next next node 
        if node_itr.next : # here node_itr.next is the value we need to delete , not the node_itr itself 
            node_itr.next = node_itr.next.next 
            
    # Tutorial 2 : Display length ,search by value , search by index ,delete by index  
    
    def length(self):
        """_summary_
        Get the length of the entire LL

        """
        if not self.head: return 0
        node_itr = self.head
        length = 0 
        while node_itr:
            length +=1
            node_itr=node_itr.next
            
        return length
    
    def search_by_value(self,value):
        """_summary_
        Searches by value, returns index if found 
        """
        if not self.head: return -1
        index=0
        node_itr = self.head
        
        while node_itr :
            if node_itr.value == value:
                return index 
            node_itr=node_itr.next
            index+=1
            
        return -1 # if not found 
    
    def search_by_index (self,index):
        """
        Searches by index and returns value , else None
        """
        if not self.head :
            return None
        index_counter = 0
        node_itx = self.head
        while node_itx:
            if index_counter==index:
                return node_itx.value
            node_itx= node_itx.next
            index_counter+=1
            
        return None
    
    def delete_by_index(self,index):
        if index<0 or not self.head:
            return
        if index == self.head :
            self.head = self.head.next
            return
        
        node_itr = self.head
        node_index=0
        
        while node_itr.next and node_index< index-1:
            node_itr = node_itr.next
            node_index+=1
            
        if node_itr.next :
            node_itr.next = node_itr.next.next
            
    
    
                
        
                
            

            
            

                
            
            
            
        
        
        