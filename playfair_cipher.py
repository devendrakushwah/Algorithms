def make_matrix(key):
    key=key.replace('j','i')
    added=[False]*26
    s=[0 for x in range(25)]
    j=0
    for i in key:
        if(not added[ord(i)-97]):
            s[j]=i
            added[ord(i)-97]=True
            j+=1

    for i in 'abcdefghiklmnopqrstuvwxyz':
        if(not added[ord(i)-97]):
            s[j]=i
            added[ord(i)-97]=True
            j+=1
    mtx=[['' for x in range(5)]for y in range(5)]
    k=0
    for i in range(5):
        for j in range(5):
            mtx[i][j]=s[k]
            k+=1
    #print(mtx)
    return mtx,s

def get_row_column(value,matrix):
    for e in matrix:
        if value in e:
            return matrix.index(e),e.index(value)

def encrypt(key,message):
    ans=''
    message=message.replace(' ','')
    message=message.lower()
    matrix,string = make_matrix(key)
    if(len(message)%2)==1:
        message+='x'
    for i in range(0,len(message),2):
        e1,e2=message[i],message[i+1]
        row1,col1=get_row_column(e1,matrix)
        row2,col2=get_row_column(e2,matrix)

        if(row1==row2):
            if(col1==4):
                ans+=matrix[row1][0]
            else:
                ans+=matrix[row1][col1+1]
            if(col2==4):
                ans += matrix[row2][0]
            else:
                ans += matrix[row2][col2+1]

        elif(col1==col2):
            if(row1==4):
                ans+=matrix[0][col1]
            else:
                ans+=matrix[row1+1][col1]
            if(row2==4):
                ans += matrix[0][col2]
            else:
                ans += matrix[row2+1][col2]
        else:
            ans+=matrix[row1][col2]
            ans+=matrix[row2][col1]
    return ans

def decrypt(key,message):
    ans = ''
    message = message.replace(' ', '')
    message = message.lower()
    matrix, string = make_matrix(key)
    if (len(message) % 2) == 1:
        message += 'x'
    for i in range(0, len(message), 2):
        e1, e2 = message[i], message[i + 1]
        row1, col1 = get_row_column(e1, matrix)
        row2, col2 = get_row_column(e2, matrix)

        if (row1 == row2):
            if (col1 == 0):
                ans += matrix[row1][4]
            else:
                ans += matrix[row1][col1 - 1]
            if (col2 == 0):
                ans += matrix[row2][4]
            else:
                ans += matrix[row2][col2 - 1]

        elif (col1 == col2):
            if (row1 == 0):
                ans += matrix[4][col1]
            else:
                ans += matrix[row1 - 1][col1]
            if (row2 == 0):
                ans += matrix[4][col2]
            else:
                ans += matrix[row2 - 1][col2]
        else:
            ans += matrix[row1][col2]
            ans += matrix[row2][col1]
    return ans

def print_matrix():
    matrix=make_matrix('security')[0]
    for i in range(5):
        for j in range(5):
            print(matrix[i][j]+' ',end='')
        print()

if __name__ == '__main__':
    key='security'
    while(True):
        print('Enter Choice : 1.Encrypt 2.Decrypt')
        ch=input()
        if(ch=='1'):
            print('Enter Message to be encrypted')
            message=input()
            print('Encrypted message = ',end='')
            print(encrypt(key,message))
            print_matrix()
        elif(ch=='2'):
            print('Enter Message to be decrypted')
            message=input()
            print('Decrypted message = ',end='')
            print(decrypt(key,message))
            print_matrix()
        else:
            break




