import re
str=r"hello my name is raghav. my rool no. is h1674\17"

result=re.sub(r"h(\d{4})\\(\d{2})",r"\1",str)
print(result)
print(result)
result1=re.findall(r"\d{4}\\\d{2}",str)
print(result1)
result3=re.match(r"hello",str)
print(result3.group())

patt=re.compile(r"r(\w*)")
print(patt)
matches=patt.finditer(str)
for i in matches:
    print(i)
