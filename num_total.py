def two_sum(nums,target):
    output = []
    num_len = len(nums)
    for i in range(num_len):
        for j in range(num_len):
             total = nums[i] + nums[j]
             if total == target and i != j and i not in output and j not in output:
                 output.append(i)
                 output.append(j)
    return output 


nums = [3,2,4]
target = 6
p = two_sum(nums,target)
print (p)


        



    
    
       
        
        
            
            
          
            
        


            
            
                
                
        