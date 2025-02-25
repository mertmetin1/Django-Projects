import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','kitap_pazari.settings')

import django
django.setup()

###modellerimize ve django içeriklerine erişebilmek için yukarıdaki gibi module dahil etmemiz lazım 
### sıralama çok önemli



from django.contrib.auth.models import User

from faker import Faker


def set_user():


    fake=Faker(['en_US'])


    f_name =fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name,l_name,email)
     
    user_check= User.objects.filter(username=u_name)
    
    while user_check.exists():
        u_name =u_name +str(random.randrange(1,99))
        user_check= User.objects.filter(username=u_name)
        
        
        
        
    user=User(
        username= u_name,
        first_name = f_name,
        last_name = l_name,
        email = email
        
        
    )
    user.set_password('testing321..')
    user.save()
    
    
for i in range(100):
    set_user()