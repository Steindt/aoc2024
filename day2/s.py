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
  with open("day2/iex") as f:
    sum = 0
    for line in f:
      line = list(map(int, line.split()))
      interval = [0, 4] if line[1] - line[0] > 0 else [-4, 0]
      errors = 0 
      index = 1
      for i in range(1, len(line)):
        diff = line[index] - line[index-1]
        if diff <= interval[0] or diff >= interval[1]:
          line.pop(index-1)
          index -= 1
          errors += 1
          if errors > 1:
            break
        index += 1
      if errors <= 1:
        print(line)
        sum += 1
    print(sum)

first()
second()