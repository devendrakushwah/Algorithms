#include<stdio.h>
int ar[]={12,1,14,2,9,4,0,7,6};
void merge(int a[ ] , int low, int mid, int high) {
int i= low, j=mid+1;
int b[high-low+1] , k=0;
for(int v = low ;v <= high ;v++) {
    if(p>mid)
       b[c++]=a[j++] ;
   else if (q>high)
       b[c++] = a[i++];
   else if(a[p]<a[q])
      b[c++] = a[i++];
   else
      b[c++]= a[ j++];
 }
  for (int x=0;x<c;p++) {
     a[low++]=b[x] ;
  }
}
void merge_sort (int a[ ] , int low , int high )
   {
           if( low < high ) {
           int mid = (low + high ) / 2;
           merge_sort (a, low , mid ) ;
           merge_sort (a,mid+1 , high ) ;
          merge(a,low , mid , high );
   }
}
int main()
{
    merge_sort(ar,0,8);
    for(int i=0;i<9;i++)
    {
        printf("%d,",ar[i]);
    }
    return 0;
}
