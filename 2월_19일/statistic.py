from collections import Counter

def get_freq(sorted_list):
    result = Counter(sorted_list)
    freq_result = list(result.values()) #key와 values
#유일하다면
        
    max_value = max(freq_result)#같은 값이 있을때 처음 값
    
    same_value = 0
    for i in range(len(result)): #key값을 뽑아내는거지
        if result[list(result.keys())[i]] == max_value:
            same_value+=1
            same_index = list(result.keys())[i]
            if same_value ==2:
                freq_value = list(result.keys())[i]
                break
    if same_value ==1:
        freq_value = same_index #key
        
    return freq_value

n = int(input())
#lstrip rstrip 개행 없애는것
list = []
b = 0

for i in range(n):
    b = int(input())
    list.append(b)

list = sorted(list)
#print(sum(list)//5)
mean = int(round(sum(list)/n))
#index가 0 1 2 3 4 즉 len-1/2
# 0 1-1/2
index = int((len(list)-1)/2)
median = list[index]
freq = get_freq(list)
length = list[-1] - list[0]

print(mean)
print(median)
print(freq)
print(length)

#print(list)







