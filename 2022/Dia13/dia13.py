with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

def count_right_order_pairs(pairs):
  def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
      return left < right
    elif isinstance(left, list) and isinstance(right, list):
      for l, r in zip(left, right):
        if compare(l, r) != 0:
          return compare(l, r)
      return 0
    else:
      return compare(left, [right])

  count = 0
  for left, right in pairs:
    if compare(left, right) == 1:
      count += 1
  return count



