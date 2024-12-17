input = list()

with open("input/day_13.txt", "r") as file:
    for line in file:
        input.append([x for x in line])

def cost_of_path(turns: int, steps: int) -> int:
    return 1000 * turns + steps

visited: dict[tuple[int,int]: int] = dict()

def maze_race(from_direct, position: tuple[int,int], turns, steps, maze) -> float:
    new_path_cost = cost_of_path(turns, steps)
    
    if maze[position[0]][position[1]] == 'E':
        return new_path_cost
    elif not position in visited:
        visited[position] = new_path_cost
    elif visited[position] > new_path_cost:
        visited[position] = new_path_cost
        
    
    
    dp = [d 
          for d in [(1,0),(0,1),(-1,0),(0,-1)] 
          if d != from_direct]
    
    
    
    return