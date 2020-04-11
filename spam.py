import pip._vendor.requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://netflxaccntsupports.com/mail1.php'

names = json.loads(open('names.json').read())
mailsites = ['gmail', 'gmail', 'gmail', 'gmail', 'gmail', 'gmail', 'gmail', 'gmail', 'hotmail', 'rogers', 'yahoo', 'outlook']
mailtl = ['com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'com', 'ca', 'co.uk']

surnames = json.loads(open('surnames.json').read())

streets = json.loads(open('streets.json').read())
cities = json.loads(open('cities.json').read())

def phonestyle(p1, p2, p3):
    phone = ''

    roll = random.randint(1,8)
    if roll == 1:
        phone += '+1'
    elif roll == 2:
        phone += '1'

    roll = random.randint(4, 16)
    if roll <= 6:
        if phone == '':
            phone = '{}-{}-{}'.format(p1, p2, p3)
        else:
            phone = '{}-{}-{}-{}'.format(phone, p1, p2, p3)
    elif roll == 7:
        if phone == '':
            phone = '{} {} {}'.format(p1, p2, p3)
        else:
            phone = '{} {} {} {}'.format(phone, p1, p2, p3)
    elif roll == 8:
        if phone == '':
            phone = '({}){}-{}'.format(p1, p2, p3)
        else:
            phone = '{}({}){}-{}'.format(phone, p1, p2, p3)
    elif roll == 9:
        if phone == '':
            phone = '({}) {} {}'.format(p1, p2, p3)
        else:
            phone = '{} ({}) {} {}'.format(phone, p1, p2, p3)
    elif roll == 10:
        if phone == '':
            phone = '{}-{}-{}'.format(p1, p2, p3)
        else:
            phone = '{} {}-{}-{}'.format(phone, p1, p2, p3)
    elif roll == 11:
        if phone == '':
            phone = '({})-{}-{}'.format(p1, p2, p3)
        else:
            phone = '{}({})-{}-{}'.format(phone, p1, p2, p3)
    else:
        if phone == '':
            phone = '{}{}{}'.format(p1, p2, p3)
        else:
            phone = '{}{}{}{}'.format(phone, p1, p2, p3)
    return phone

def postalstyle(l, r):
    code = ''
    
    roll = random.randint(1, 4)
    if roll == 1:
        code = l + ' ' + r
    else:
        code = l + r
    
    roll = random.randint(5, 10)
    if roll == 5:
        code = code.lower()
    return code



random.shuffle(names)

for name in names:
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1,6)))
    mail = ''.join(random.choice(mailsites)) + '.' + ''.join(random.choice(mailtl))
    email = name.lower() + name_extra + '@' + mail

    password = ''.join(random.choice(chars) for i in range(random.randint(6,16)))

    f_name = name
    l_name = ''.join(random.choice(surnames))

    dob = "{:0>2d}/{:0>2d}/19{:2d}".format(random.randint(1, 12), random.randint(1, 31), random.randint(50,99))

    address = str(random.randint(1,1200)) + ' ' + ''.join(random.choice(streets))
    postal = postalstyle(''.join(random.choice(string.ascii_uppercase)) + ''.join(random.choice(string.digits)) + ''.join(random.choice(string.ascii_uppercase)), ''.join(random.choice(string.digits)) + ''.join(random.choice(string.ascii_uppercase)) + ''.join(random.choice(string.digits)))
    pick_loc = cities[random.randint(0, len(cities))]
    city = pick_loc[0]
    province = pick_loc[1]

    phone = phonestyle("{:0>3d}".format(random.randint(100,999)), "{:0>3d}".format(random.randint(0,999)), "{:0>4d}".format(random.randint(0,9999)))

    namecard = f_name + ' ' + l_name
    card = ''.join(random.choice(string.digits) for i in range(16))
    cvv = ''.join(random.choice(string.digits) for i in range(random.randint(3,4)))
    date = '{:0>2d}/{:2d}'.format(random.randint(1,12), random.randint(20,25))

    #print("{} {}. Born: {}. Email: {} Pass: {}. Phone: {}. Address: {}, {}, {} {}. Credit Card: {} {} CVV: {} Exp: {}.".format(f_name, l_name, dob, email, password, phone, address, city, province, postal, namecard, card, cvv, date))

    pip._vendor.requests.post(url, allow_redirects=False, data={
        'email': email,
        'password': password,
        'rememberMe': 'true',
        'flow': 'websiteSignUp',
        'mode': 'login',
        'action': 'loginAction',
        'withFields': ['email','password','rememberMe','nextPage','showPassword'],
        'authURL': '1507547290847.TbSRwMSuuT8M2PX3+bfrCDsl1fE=',
        'nextPage': '',
        'showPassword': '',
        'flow': 'websiteSignUp',
        'mode': 'login',
        'action': 'facebookLoginAction',
        'withFields': ['accessToken','rememberMe','nextPage'],
        'authURL': '1507547290847.TbSRwMSuuT8M2PX3+bfrCDsl1fE=',
        'nextPage': '', 
        'showPassword': '',
        'accessToken': '',
        'f_name': f_name,
        'l_name': l_name,
        'dob': dob,
        'address': address,
        'postal': postal,
        'city': city,
        'province': province,
        'phone': phone,
        'namecard': namecard,
        'card': card,
        'data': date,
        'cvv': cvv
    })

    print("{} {} from {}: {}".format(f_name, l_name, city, email))

"""
email: markusjohnson512@hotmail.com
password: markyoy555
rememberMe: true
flow: websiteSignUp
mode: login
action: loginAction
withFields: email,password,rememberMe,nextPage,showPassword
authURL: 1507547290847.TbSRwMSuuT8M2PX3+bfrCDsl1fE=
nextPage: 
showPassword: 
flow: websiteSignUp
mode: login
action: facebookLoginAction
withFields: accessToken,rememberMe,nextPage
authURL: 1507547290847.TbSRwMSuuT8M2PX3+bfrCDsl1fE=
nextPage: 
showPassword: 
accessToken: 
f_name: Markus
l_name: Johnson
dob: 10/12/1978
address: 104 Chandler Ave
postal: K4L9J8
city: Kingston
province: Ontario
phone: 9532052049
namecard: Markus Johnson
card: 920492042945
date: 09/23
cvv: 698
"""