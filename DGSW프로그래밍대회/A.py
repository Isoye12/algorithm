majorClubs = [ "ALT", "B1ND", "SAMDI", "Louter", "CNS", "MODI", "DUCAMI", "Chatty" ]
freeClubs = [ "DROP", "InD", "8BIT", "C0nnect", "draw", "Scheck", "DGSWFC", "Warriors", "cyclists" ]

def cntMajorClub(lis):
  n = 0
  for i in lis:
    if i in majorClubs:
      n +=1
  return n

def isExistClub(lis):
  for i in lis:
    if i not in majorClubs and i not in freeClubs:
      return False
  return True

cnt = int(input())

for i in range(cnt):
  appliedCnt = int(input())
  appliedList = list(input().split())

  if not isExistClub(appliedList): 
    print("No")
    continue

  if appliedCnt != len(set(appliedList)):
    print("No")
    continue

  if cntMajorClub(appliedList) != 1:
    print("No")
    continue

  print("Yes")