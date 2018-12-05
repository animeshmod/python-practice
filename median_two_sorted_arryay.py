def medianofarray(n1,n2):
    merged_list = n1 + n2

    merged_list.sort()

##    for l in n1:
##        merged_list.append(n1)

##    for l in n2:
##        merged_list.append(n2)

    list_length = len(merged_list)

    
    print (*merged_list)
    print ("list_lenght is {}" .format(list_length))
    a = list_length%2
    print(a)

    if a == 0:
        median_index1 = list_length//2
        median_index2 = median_index1 - 1
        print ("median_index1 is {}" .format(median_index1))
        print ("median_index2 is {}" .format(median_index2))
        val1 = merged_list[int(median_index1)]
        val2 = merged_list[int(median_index2)]
        median1 = val1 + val2
        median = median1/2
    else:
        median_index = list_length//2
        print ("median_index1 is {}" .format(median_index))
        median = merged_list[median_index]

    return median


nums1 = [1,2]
nums2 = [3,4]

s = medianofarray(nums1,nums2)
print (s)



