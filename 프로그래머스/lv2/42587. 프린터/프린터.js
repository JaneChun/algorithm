// Node 생성자
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// Queue 생성자
class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
    
    enqueue(newValue) {
        const newNode = new Node(newValue);
        if (this.head === null) {
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.size++;
    }

    dequeue() {
        const value = this.head.value;
        this.head = this.head.next;
        this.size--;
        return value;
    }

    peek() {
        return this.head.value;
    }
}

function solution(priorities, location) {
    const queue = new Queue();
    for (let i = 0; i < priorities.length; i++) {
        queue.enqueue([priorities[i], i]);
    }
    priorities.sort((a, b) => b - a);
    
    let counter = 0;
    while (queue.size > 0) {
       const currentValue = queue.peek();
        if (currentValue[0] < priorities[counter]) {
            queue.enqueue(queue.dequeue());
        } else {
            const value = queue.dequeue();
            counter++;
            if (value[1] === location) {
                return counter;
            }
        }
    }
    return counter;
}