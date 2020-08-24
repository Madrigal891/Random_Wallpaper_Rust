import os
i=719
while i<1000:
    print(i)
    command ='./wallrnd {}'
    command2='convert {} {}.jpg'
    os.system(command.format(i))
    os.system(command2.format(i,i))
    os.remove(str(i))
    i+=1