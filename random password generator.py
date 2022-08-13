
import string
import random


if __name__ =="__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    sr=int(input("enter the sr_no:"))
    service=str(input("Enter the service name:"))
    plen = int(input("enter the password length"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s)
    # print(s).
    result = "".join(random.sample(s, plen))
    print(result)
    

  