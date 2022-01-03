def template(name, email, product, fh):
    TOD = 'Morning'
    DATE = 'yesterday'
    body = '''
{}
Good {} {},

This is REDACTED from REDACTED, I helped you with your purchase {}. I wanted to thank you for chosing REDACTED
and I hope that your new {} are working well for you.

REDACTED wants you to be happy with your purchase. So should anything come up. Please come into one of our locations.

--------------------------------------------------------------------------------------------------------------------------------'''.format(email,TOD,name,DATE, product)
    fh.write(body)
    fh.write('\n')
    
def dict(val):
    Sidewinder = ['401']
    Reebok = [
        'IB4041', 'IB4043', 'IB4311'
        'IB4315', 'IB4311', 'IB4036'
        'IB4037', 'IB4039', 'IB4249'
        'IB4046', 'IB4142', 'IB6800'
        'IB4607']
    
    items = [[Reebok,'Reebok'], [Sidewinder,'Sidewinder']]
    
    products = dict.fromkeys(Sidewinder, 'Sidewinder')
    
    for i in range(items):
                
        products.update(dict.fromkeys(items[i], items[i][i+1]))
    
    value = products.get(val)
    
    return value