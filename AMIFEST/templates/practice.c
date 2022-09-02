#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;

};

int main()
{
    struct node* head,*temp;
    head=(struct node*)malloc(sizeof(struct node));
    printf("Enter data  : ");
    scanf("%d",head->data);
    head->next=NULL;
    head=temp;
    return 0;
}