from Assets import template

with open('raw.txt') as f:
    data = f.read()
    
a = open('formatted.txt', 'a')
    
    
data = data.split()

names = []
emails = []
product = []

for i in range(len(data)):
    if(data[i].startswith('S123')):
        names.append(data[i+1])
    #elif(data[i].endswith('.COM') or data[i].endswith('.CA')):
    elif('@' in data[i]):
        emails.append(data[i])
    elif(data[i]=='S23'):
        product.append(data[i+1])
  
             
j = 0
prod_spec = []
while(j<len(product)):
    print(product[j])
    var = input('Prod name: ')
    prod_spec.append(var)
    j+=1
    

j=0 
while(j<len(names)):
    template(names[j],emails[j],prod_spec[j],a)
    j+=1

a.close()
        
        