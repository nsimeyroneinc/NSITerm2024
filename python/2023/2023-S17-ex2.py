def pascal(n):
    triangle= [[1]] #(1)
    for k in range(1,n+1):
        ligne_k = [1] #(2)
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i] ) #(3)
        ligne_k.append(1) #(2)
        triangle.append(ligne_k)
    return triangle

print(pascal(5))