n = int(input("Enter the number of rows: "))  
k = 2 * n - 2  
for i in range(n, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("*", end=" ")  
    print("")  
    ###############output*******
    #Enter the number of rows: 4
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       *