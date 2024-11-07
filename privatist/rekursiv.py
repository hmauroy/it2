def rekursiv_sum(n):
  if n <= 1:
    return n
  else:
    return n + rekursiv_sum(n-1)

print(rekursiv_sum(10))