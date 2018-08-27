/*
Quick sort Algorithm
Partition using Hoare's partition scheme*/
#include<stdio.h>

int partition(int ar[], int l, int h)
{
    int pivot=ar[l];
    int i=l-1;
    int j=h+1;
   while(true){
        do{
            i++;
        }while(ar[i]<pivot);

        do{
            j--;
        }while(ar[j]>pivot);

        if(i>=j){
            return j;
        }
        //swap
        ar[i]=ar[i]+ar[j];
        ar[j]=ar[i]-ar[j];
        ar[i]=ar[i]-ar[j];
   }
}

void QuickSort(int ar[],int l,int h)
{
    if(l<h)
    {
        int pivot=partition(ar,l,h);
        QuickSort(ar,l,pivot);
        QuickSort(ar,pivot+1,h);
    }
}

int main()
{
    int ar[]={12,2,8,-24,0,1};
    QuickSort(ar,0,5);
    for(int i=0;i<6;i++)
    {
        printf("%d ",ar[i]);
    }
    return 0;
}
