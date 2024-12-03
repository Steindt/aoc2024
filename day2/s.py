def first():
  with open("day2/i") as f:
    sum = 0
    for line in f:
      line = list(map(int, line.split()))
      interval = [0, 4] if line[1] - line[0] > 0 else [-4, 0]
      ok = True 
      for i in range(1, len(line)):
        diff = line[i] - line[i-1]
        if diff <= interval[0] or diff >= interval[1]:
          ok = False
          continue
      if ok:
        sum += 1
    print(sum)

def second():
  with open("day2/i") as f:
    sum = 0
    for line in f:
      line = list(map(int, line.split()))
      interval = [[0, 4], [-4, 0]]
      errors1 = 0
      errors2 = 0
      for i in range(1, len(line)):
        diff = line[i] - line[i-1]
        if diff <= interval[0][0] or diff >= interval[0][1]:
          errors1 += 1
        if diff <= interval[1][0] or diff >= interval[1][1]:
          errors2 += 1
      if errors1 <= 1 or errors2 <= 1:
        sum += 1
    print(sum)

first()
second()