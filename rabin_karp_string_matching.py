# Rabin Karp String Matching Algoritm

prime=101
def hash(subS,m):
    i=1
    ans=0
    while i<=m:
        ans+=(ord(subS[i-1]))*(prime**(m-i))
        i+=1
    return ans

def rolling_hash(oldHash,rmChar,newChar,m):
    #rmChar = Character to be removed
    #newChar = char to be added
    #m = pattern length

    ans = oldHash - (prime**(m-1))*ord(rmChar)
    ans = ans * prime
    ans = ans + ord(newChar)
    return ans

def rabin_karp(string,n,subString,m):
    pHash=hash(subString,m)
    tempHash = hash(string[:m],m)

    i=0

    while(i< (n-m+1)):
        if(pHash == tempHash and string[i:i+m]==subString):
            print('Found at : '+str(i))
        if(i<(n-m)):
            tempHash=rolling_hash(tempHash,string[i],string[i+m],m)
        i+=1
    return None

if __name__=='__main__':
    s='ababbabbabaab'
    p='aba'
    n=len(s)
    m=len(p)
    rabin_karp(s,n,p,m)


