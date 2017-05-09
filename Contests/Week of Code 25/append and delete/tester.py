def read_file(filename):
    content = [line.strip('\n') for line in open(filename)]
    return content

input_cases = read_file('input.txt')
expected_output = read_file('output.txt')
user_output = read_file('my_output.txt')

wrong_results = []
n = int(input_cases[0])
j=0
i=1
while n:
    n-=1
    s,t,k = input_cases[i],input_cases[i+1],input_cases[i+2]
    i+=3
    if (expected_output[j]!=user_output[j]):
        wrong_results.append([s,t,k,user_output[j]])
    j+=1
        

print ("All cases passed") if not wrong_results else \
print ("Wrong cases\n",'\n'.join(str(result).replace('\'','') for result in wrong_results))
