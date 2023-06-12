function solution(cacheSize, cities) {
    let time = 0;
    const cache = new LinkedList(cacheSize);
    
    for (let city of cities) {
        city = city.toUpperCase();
        if (cache.find(city)) {
            // cache hit
            cache.remove(city); // cache에서 city 잘라서 맨 뒤에 붙이기
            cache.insert(city);
            time += 1;
        } else {
            // cache miss
            cache.insert(city);
            time += 5;
        }
    }
    return time;
}

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor(capacity) {
        this.head = null;
        this.tail = null;
        this.size = 0;
        this.capacity = capacity;
    }
    
    find(value) {
        let currentNode = this.head;
        while(currentNode !== null) { // tail까지 갈때까지
            if (currentNode.value === value) { 
                return true;
            }
            currentNode = currentNode.next; // 현재 노드가 찾는 값이 아니라면 다음 노드로 이동
        }
        return false;
    }
    
    insert(value) {
        const newNode = new Node(value); // 새로운 노드 생성 newNode = {value:'Jeju', next: null}
        if (this.head === null) { // 연결리스트가 아예 비어있는 경우
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode; // 연결리스트 마지막에 새로운 노드를 연결해준다.
            this.tail = newNode; // 'a' - 'b' - 'c' - 'jeju'
        }
        this.size++;
        
        if (this.size > this.capacity) {
            // 가장 오래된 노드 삭제
            this.head = this.head.next;
            this.size--;
        }
    }
    
    remove(value) { // 'a' - 'b' - 'c' - 'd'
        let currentNode = this.head; // head부터 시작
        let prevNode = null;
        while (currentNode !== null) { // currentNode가 null이 될때까지 (연결리스트를 끝까지 순회)
            if (currentNode.value === value) { // 삭제할 노드를 찾았을 때
                if (prevNode === null) { // currentNode가 맨 앞인 경우
                    this.head = currentNode.next;
                } else if (currentNode.next === null) { // currentNode가 맨 끝에 있는 경우
                    prevNode.next = null;
                    this.tail = prevNode;
                } else { // currentNode가 중간에 끼어있는 경우
                    prevNode.next = currentNode.next; // 삭제할 노드의 이전 노드가 다음 노드를 가르키도록
                }
                this.size--;
                return true;
            }

            prevNode = currentNode;
            currentNode = currentNode.next; // 못찾았다면 다음 노드로 이동
        }
        
        return false;
    }
}