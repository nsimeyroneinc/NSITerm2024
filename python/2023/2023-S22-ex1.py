def liste_puissances(a,n):
  puissances = [a]
  for i in range(2,n+1):
    an = puissances[-1]*a
    puissances.append(an)
  return puissances

def liste_puissances_borne(a,borne):
  if a > borne : 
    return []
  else:
    puissances = [a]
    while puissances[-1]*a <= borne:
      an = puissances[-1]*a
      puissances.append(an)
    return puissances
