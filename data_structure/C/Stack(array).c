#include <stdio.h>
#define SIZE 10000
#define INF 99999999

int stack[SIZE];
int top = -1;

void push(int data) {
    if (top == SIZE -1) {
        printf("스택 오버플로우가 발생했습니다. \n");
        return;
    }
    stack[++top] = data;
}

int pop() {
    if (top == -1) {
        printf("stack underflow. \n");
        return - INF;
    }
    return stack[top--];
}

void show() {
    printf("---스택의 최상단 ----\n");
    for (int i = top; i >= 0; i--) {
        printf("%d\n", stack[i]);
    }
    printf("---스택의 최하단 ---\n");
}

int main(void){
    push(7);
    push(5);
    push(4);
    pop();
    push(6);
    pop();
    show();
    return 0;    
}
