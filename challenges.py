def NestedListSort_Challenge():
  lis = [[[3,[['hi'],'all',1553], Noise('15')],[[12,13,75,12,54,[['all',[[[['apple', 'bannana', 'orange',[[[14,'t','a','zed']]],19]]]],'j',78,91,1,[[['t',14,12,51,621,'u']],13,12,'ah'],'hello',45,32]]],Noise('gafsdge')]]]
  numList, stringList = player().kyechestnut(lis)
  x=0
  y=1   
  while y < len(numList):
    if (numList[x] > numList[y]):
      return (False, "LOL", str(lis))
    x=x+1
    y=y+1
  x=0
  y=1
  while y < len(stringList):
    if (ord(stringList[x][0]) > ord(stringList[y][0])):
      return (False, "LOL", str(lis))
    x=x+1
    y=y+1
  return (True, "LOL", str(lis))
