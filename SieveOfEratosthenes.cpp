#include<bits/stdc++.h>
/*
Primarility check using Sieve of Eratosthenes.
Generate prime numbers upto n*/
int main()
{
    int n=pow(10,6);
    bool isPrime[n];
    memset(isPrime, true, sizeof(isPrime));
    for(int i=2;i<=n;i++)
    {
        if(isPrime[i] == true)
        {
            for(int j=2*i; j<=n; j=j+i)
            {
                isPrime[j]=false;
            }
        }
    }
    //tests
    printf("%d",isPrime[2]);
    printf("%d",isPrime[33]);
    printf("%d",isPrime[41]);
    printf("%d",isPrime[99]);
    return 0;
}
