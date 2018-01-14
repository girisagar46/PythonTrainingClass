import helperservice
from mypack.string_helper import *

temp = 97
F = helperservice.get_farheniet(temp)
print(F)

print(getFormattedCurrency(4500))
print(getFormattedCurrency(4500, type="usd"))

