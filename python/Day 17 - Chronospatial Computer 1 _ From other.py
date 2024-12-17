import re

from collections import deque

def run_program(program: list[int], a: int, b: int, c: int) -> list[int]:
  ip = 0

  def combo(operand: int) -> int:
    return (a, b, c)[operand - 4] if operand >= 4 else operand

  out = []
  while ip < len(program) - 1:
    opcode, operand = program[ip], program[ip + 1]

    match opcode:
      case 0:
        a //= 2 ** combo(operand)
      case 1:
        b ^= operand
      case 2:
        b = combo(operand) & 7
      case 3:
        if a:
          ip = operand - 2
      case 4:
        b ^= c
      case 5:
        out.append(combo(operand) & 7)
      case 6:
        b = a // 2 ** combo(operand)
      case 7:
        c = a // 2 ** combo(operand)

    ip += 2

  return out

def self_generate(program: list[int]) -> int:
  candidates = deque([0])
  min_candidate = 2 ** (3 * (len(program) - 1))

  while candidates and candidates[-1] < min_candidate:
    seed = candidates.popleft()
    for a in range(2 ** 6):
      a += seed << 6
      out = run_program(program, a, 0, 0)
      if a < 8:
        out.insert(0, 0)
      if out == program[-(len(out)):]:
        candidates.append(a)
      if out == program:
        break

  return candidates.pop()

def run() -> None:
  with open('input\day_17.txt') as f:
    a, b, c, *program = (int(x) for x in re.findall(r'\d+', f.read()))

  out = run_program(program, a, b, c)
  print(f"Program output: {''.join(str(n) for n in out)}")

  #a = self_generate(program)
  #print(f'Self-generating register A: {a}')

if __name__ == '__main__':
  run()
