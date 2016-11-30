import random
import string

def ger_activation():
    number=0
    list_activation=[]
    while number<201:
        patter_str=string.digits+string.letters
        activation_code='.join(random.sample(patter_str,16))'
        list_activation.append(activation_code)
        number+=1
    print(list_activation)
ger_activation()
