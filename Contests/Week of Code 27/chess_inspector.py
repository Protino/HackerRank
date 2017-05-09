def read_file(filename):
    content = [line.strip('\n') for line in open(filename)]
    return content

input_cases = read_file(input('Enter input_cases file name : ',))
expected_output = read_file(input('Expected output_cases file name : ',))
user_output = read_file(input('Your output file name : '))

wrong_results = []
n = int(input_cases[0])
j=0
i=1
while n:
    pieces = int(input_cases[i][0])+int(input_cases[i][2])
    if expected_output[j]!=user_output[j]:
        wrong_results.append([input_cases[k] for k in range(i,i+pieces+1)])
        wrong_results.append(' Expected-'+expected_output[j])
    j+=1
    i+=pieces+1
    n-=1

print ("All cases passed") if not wrong_results else \
print ("Wrong cases\n",'\n'.join(str(result).replace('\'','') for result in wrong_results))
