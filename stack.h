typedef struct Node{
    int data;
    struct Node * prev;
}*stack;

//Constructors
stack newStack(){
    return NULL;
}

stack push(stack mainStack, int newData){
    stack newNode = (stack)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->prev = mainStack;
    return newNode;
}

//Observers
int isNew(stack mainStack){
    return mainStack==NULL;    
}

int top(stack mainStack){
    return mainStack->data;
}

//Destroyers
stack pop(stack mainStack){
    stack bridge = mainStack;
    mainStack = mainStack->prev;
    free(bridge);
    return mainStack;
}

//Special
int amountElementsIterative(stack mainStack){
    stack bridge = mainStack;
    int amountElements = 0;
    while(bridge!=NULL){
        amountElements++;
        bridge=bridge->prev;
    }
    return amountElements;
}

int amountElementsRecursive(stack mainStack){
    if(mainStack == NULL){
        return 0;
    }
    return 1 + amountElementsRecursive(mainStack->prev);
}
