def bestFit(blockSize, m, processSize, n):  
    allocation = [-1] * n  
    for i in range(n):  
        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j  
        if bestIdx != -1:  
            allocation[i] = bestIdx    
            blockSize[bestIdx] -= processSize[i] 
  
    print("Process No. Process Size     Block no.") 
    for i in range(n): 
        print(i + 1, "       ", processSize[i],  
                                end = "      ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 
  
block_Size = []
process_Size = []
m = int(input("Number of Memory Partitions "))
n = int(input("Number of Processes "))
for i in range(m):
  block_Size.append(int(input("Enter memory block size ")))
for i in range(n):
  process_Size.append(int(input("Enter process ")))
m = len(block_Size)
n = len(process_Size)  
  
bestFit(block_Size, m, process_Size, n) 
