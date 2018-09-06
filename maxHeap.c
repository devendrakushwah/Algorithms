#include<stdio.h>
int ar[100];
int heap_size=0; //to store the current heap size
void insert(int item)
{
    /*if(heap_size==0)
    {
        ar[0]=item;
        heap_size++;
        return;
    }*/
    ar[heap_size+1]=item; //insert new element at end
    heap_size++;
    int k=heap_size;
    int parent;
    while(k!=1)
    {
        parent=k/2;
        if(ar[k]>ar[parent])
        {
            int temp=ar[parent];
            ar[parent]=ar[k];
            ar[k]=temp;
            k=parent;
        }
        else
        {
            break;
        }
    }
}
int main()
{
    //memset(ar,0,sizeof(ar));
    //tests
    insert(89);
    insert(20);
    insert(1);
    insert(100);
    insert(5);
    insert(110);
    int i;
    for(i=1;i<heap_size+1;i++)
    {
        printf("%d, ",ar[i]);
    }
    return 0;
}
