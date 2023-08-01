d={'roll':[],'name':[],'marks':[]}
n=int(input())
for i in range(n):
    ip=input().split()
    d['roll'].append(int(ip[0]))
    d['name'].append(ip[1])
    d['marks'].append(int(ip[2]))
r=int(input())
print('roll \t name \t marks')
for i in range(len(d['roll'])):
    print(d['roll'][i],' \t ',d['name'][i],' \t ',d['marks'][i])
#on the basis of roll number
if r in d['roll']:
    i=d['roll'].index(r)
    print(d['roll'][i],' \t ',d['name'][i],' \t ',d['marks'][i])
else:
    print('roll not found')
