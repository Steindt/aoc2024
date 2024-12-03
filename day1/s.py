def first():
  left = []
  right = []
  sum = 0
  with open("day1/i") as f:
    for line in f:
      line = list(map(int, line.split()))
      left.append(line[0])
      right.append(line[1])
  left.sort()
  right.sort()
  for i in range(len(left)):
    sum += abs(left[i] - right[i])
  print(sum)

def second():
  right = {}
  left = {}
  sum = 0
  with open("day1/i") as f:
    for line in f:
      line = list(map(int, line.split()))
      if line[0] in left:
        left[line[0]] += 1
      else:
        left[line[0]] = 1
      if line[1] in right:
        right[line[1]] += 1
      else:
        right[line[1]] = 1
  for k in left.keys():
    if k in right:
      sum += k * right[k]
  print(sum)

first()
second()