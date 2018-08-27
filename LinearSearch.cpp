#include<stdio.h>
int lsearch(int ar[],int n,int item)
{
    for(int i=0;i<n;i++)
    {
        if(ar[i]==item)
        {
            return i;
        }
    }
    return -1;
}
int main()
{
    int ar[]={8,6,7,1,2,3};
    printf("%d\n",lsearch(ar,6,10));
    printf("%d\n",lsearch(ar,6,2));
}
