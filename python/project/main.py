import MyPackage as my

print (my.foo(3))
print (my.bar([1,2,3]))

from MyPackage import foo
print (foo(4))
from MyPackage import bar 
print (bar([9,8,7]))

from MyPackage import *

print (foo(5))
print (bar([11,12]))





