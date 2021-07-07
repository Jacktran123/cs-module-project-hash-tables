class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    def __init__(self, capacity):
        self.capacity= capacity
        self.storage=[None] * capacity
        self.occupied_slot= 0

    def get_num_slots(self):
    
        return len(self.storage)

    def get_load_factor(self):

        return self.occupied_slot / self.get_num_slots()


    def fnv1(self, key):
        
        offset_basis = 14695981039346656037
        hash = offset_basis
        FNV_prime=1099511628211

        for char in key:
            hash= hash * FNV_prime
            hash= hash ^ ord(char)
        return hash
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        hash_index=self.hash_index(key)
        current=self.storage[hash_index]
        entry=HashTableEntry(key,value)
        if current:
            while current.next and current.key != key :
                current=current.next
            if current.key==key:
                current.value=value
            else:
                current.next=entry
                self.occupied_slot +=1
        else: 
            self.storage[hash_index]=entry
            self.occupied_slot +=1

            

        
    
    

    def delete(self, key):
        hash_index = self.hash_index(key)
        current = self.storage[hash_index]

        if current:
            if current.key == key:
                self.storage[hash_index] = current.next
                self.occupied_slot -= 1
            else:
                prev = current
                current = current.next

                while current:
                    if current.key == key:
                        prev.next = current.next
                        self.occupied_slot -= 1
                        break
                    prev = current
                    current = current.next

            if self.get_load_factor() < 0.2 and self.get_num_slots() > MIN_CAPACITY:
                self.resize(self.capacity // 2)

            if current:
                return current
                


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        hash_index=self.hash_index(key)
        current=self.storage[hash_index]
        if current:
            while current:
                if current.key==key:
                    return current.value
                current=current.next
        
    def reset_storage(self,new_capacity):
        self.capacity=new_capacity
        self.storage=[None] * new_capacity
        self.occupied_slots= 0

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash storage and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        prev_storage=self.storage
        self.reset_storage(new_capacity)
        for l_list in prev_storage:
            while l_list:
                self.put(l_list.key, l_list.value)
                l_list = l_list.next



if __name__ == "__main__":

    ht = Hashstable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.put('line_13', 'something need to be tested')

    

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")

