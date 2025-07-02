st_score = [1,2,3,4,5,6,70,8,9,10]

#total_score = sum(st_score) 
#print(total_score)
#sum = 0
#for score in st_score:
#    sum += score 
#    print(score )
#print(sum)

max_num = 0
for score in st_score:
    if score > max_num:
        max_num = score
print(max_num)