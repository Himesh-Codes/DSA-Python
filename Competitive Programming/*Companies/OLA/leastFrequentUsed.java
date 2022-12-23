import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
class DoubleLinkedList{
    DLLNode head, tail; 
    int listSize;

    public DoubleLinkedList(){
        this.head = this.tail = new DLLNode(0, 0);
        this.listSize = 0;
        this.head.next = tail;
        tail.previous = head;
    }

    public void addNodeInFront(DLLNode node){
        DLLNode nextnode = head.next;
        node.next = head.next;
        node.previous = head;
        head.next = node;
        nextnode.previous = node;
        listSize ++;
    }
    public void removeNode(DLLNode node){
        node.next.previous  = node.previous;
        node.previous.next = node.next;
        listSize --;
       
    }
}

class DLLNode{  
    int item;  
    int key;
    DLLNode previous;  
    DLLNode next;  
    int frequency;

    public DLLNode(int key, int item) {  
        this.item = item;  
        this.key = key;  
        this.frequency = 1;
    }  
}  

class LFUCache {
    // max capacity
    final int capacity;
    // current size/capacity
    int currentSize;
    int minfrequency;
    Map<Integer, DLLNode> cache;
    Map<Integer, DoubleLinkedList>  frequencymap;
    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minfrequency = 0;
        this.cache = new HashMap<>();
        this.frequencymap = new HashMap<>();
    }
    
    public int get(int key) {
        DLLNode node = cache.get(key);
        if(node == null){
            return -1;
        }
        this.updateNode(node);
        return node.item;
    }

    private void updateNode(DLLNode node){
        int currentFrequency = node.frequency;
        DoubleLinkedList list = frequencymap.get(currentFrequency);
        list.removeNode(node);
        if(currentFrequency == minfrequency && list.listSize == 0){
            minfrequency ++;
        }
        node.frequency ++;
        DoubleLinkedList newlist = frequencymap.getOrDefault(node.frequency, new DoubleLinkedList());
        newlist.addNodeInFront(node);
        frequencymap.put(node.frequency, newlist);
    }
    
    public void put(int key, int value) {
        if (capacity == 0) return;
        if(cache.containsKey(key)){
            DLLNode node = cache.get(key);
            node.item = value;
            this.updateNode(node);
        } else {
            currentSize ++;
            if (currentSize > capacity) {
                //get minim freq used list
                DoubleLinkedList list = frequencymap.get(this.minfrequency);
                // 
                cache.remove(list.tail.previous.key);
                list.removeNode(list.tail.previous);
                currentSize--;
            }
            // reset min frequency to 1 since new node create
            this.minfrequency = 1;
            DLLNode node = new DLLNode(key, value);

            DoubleLinkedList list = frequencymap.getOrDefault(key, new DoubleLinkedList());
            list.addNodeInFront(node);
            frequencymap.put(1, list);
            cache.put(key, node);
        }
    }
}