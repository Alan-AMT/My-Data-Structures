typedef struct Node{
    int Data;
    struct Node *next;
}*CircularQueue;

//Builders    
CircularQueue newQueue(){
    return NULL;
}

CircularQueue enqueue(CircularQueue mainQueue ,int newData){
    CircularQueue newNode = (CircularQueue)malloc(sizeof(struct Node));
    newNode->Data = newData;
    if(isEmptyQueue(mainQueue)){
        newNode->next = newNode;
    }
    else{
        newNode->next = mainQueue->next;
        mainQueue->next = newNode;
    }
    return newNode;
}

//Observers
int isEmptyQueue(CircularQueue mainQueue){
    return mainQueue == NULL;
}

int first(CircularQueue mainQueue){
    return mainQueue->next->Data;
}

//Destroyer
CircularQueue dequeue(CircularQueue mainQueue){
    if(mainQueue == mainQueue->next){
        free(mainQueue);
        return newQueue();
    }
    else{
        CircularQueue bridgeNode;
        bridgeNode = mainQueue->next;
        mainQueue->next = mainQueue->next->next;
        free(bridgeNode);
    }
    return mainQueue;
}

//Special
CircularQueue rotateQueue(CircularQueue mainQueue){
    return mainQueue->next;
}
