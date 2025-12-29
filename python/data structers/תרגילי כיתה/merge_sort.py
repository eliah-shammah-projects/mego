

# def mahrozet (m):

#      if len(m) == 0:
#            return m

#      return m[- 1] +  mahrozet ( m[:-1]) 

# m = "ola"
# m2 = mahrozet (m)
# print (m2)

def is_polindrom (s):
      flag = True
      if len(s) == 1 or len(s) == 0:
            return  
      
      
      return s[0] == s[-1] and is_polindrom (s[1:-1])

s = "ovo"
flag = is_polindrom(s)
print (flag)
      
      