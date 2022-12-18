def minion(string):
  k= 0
  s= 0
  vocal=["a", "e", "i","o","u"]
  for i in range(0,len(string),1)
    letra= string[i]
    if letra[0] in vocal:
      k+= string.count(letra)
    else:
      s += string.count(letra)
  if k<s:
    return("Steven", s)
  else:
    return("Kevin",k)
print(minion("BANANA"))

if __name__ == '__main__'  
  minion("BANANA")
