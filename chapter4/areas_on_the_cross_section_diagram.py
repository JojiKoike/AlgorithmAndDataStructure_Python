from typing import List, Tuple

sections: str = input()
stack1: List[int] = []
stack2: List[Tuple[int, int]] = []
total_area: int = 0
for i, section in enumerate(sections):
    if section == '\\':
        stack1.append(i)
    elif section == '/' and len(stack1) > 0:
        j: int = stack1.pop()
        total_area += i - j
        one_pond_area: int = i - j
        while len(stack2) > 0 and stack2[-1][0] > j:
            pond_part: Tuple[int, int] = stack2.pop()
            one_pond_area += pond_part[1]
        stack2.append((j, one_pond_area))

ans: List[int] = []
for pond in stack2:
    ans.append(pond[1])
print(total_area)
print(len(ans), end=" ")
for area in ans:
    print(area, end=" ")
print()
