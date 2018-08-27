#include<stdio.h>
int bsearch(int ar[],int low,int high,int item)
{
    if(high>=low)
        {
        int mid=(low+high)/2;
        if(item==ar[mid])
        {
            return mid;
        }
        else if(item<ar[mid])
        {
            return bsearch(ar,low,mid-1,item);
        }
        else if(item>ar[mid])
        {
            return bsearch(ar,mid+1,high,item);
        }
    }
    return -1;
}
int main()
{
    int ar[]={1,2,4,6,11,32};
    //tests
    printf("%d\n",bsearch(ar,0,6,10));
    printf("%d\n",bsearch(ar,0,6,32));
}
