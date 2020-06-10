#not optimal

def expression_matter(a, b, c):
  max = a + b + c

  if a * b * c > max:
    max = a * b * c
  
  if (a + b) * c > max:
    max = (a + b) * c

  if (a * b) + c > max:
    max = (a * b) + c

  if a * (b + c) > max:
    max = a * (b + c)

  if a + (b * c) > max:
    max = a + (b * c)

  return max
