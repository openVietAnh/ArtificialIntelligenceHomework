"""
    Given 3 bottles of capacities 3, 5, and 9 liters, 
    count number of all possible solutions to get 7 liters
"""

current_path = [[0, 0, 0]]
CAPACITIES = (3, 5, 9)
solutions_count = 0

def move_to_new_state(current_state):
    global solutions_count, current_path
    if 7 in current_state:
        solutions_count += 1
    else:
        # Empty bottle
        for i in range(3):
            if current_state[i] != 0:
                new_state = list(current_state)
                new_state[i] = 0
                if new_state not in current_path:
                    current_path.append(new_state)
                    move_to_new_state(new_state)
                    current_path.pop()
        # Fill bottle
        for i in range(3):
            if current_state[i] != CAPACITIES[i]:
                new_state = list(current_state)
                new_state[i] = CAPACITIES[i]
                if new_state not in current_path:
                    current_path.append(new_state)
                    move_to_new_state(new_state)
                    current_path.pop()
        # Pour from one bottle to another
        for i in range(3):
            for j in range(3):
                if i != j and current_state[i] != 0 and current_state[j] != CAPACITIES[j]:
                    new_state = list(current_state)
                    liters_change = min(CAPACITIES[j] - current_state[j], current_state[i])
                    new_state[j] += liters_change
                    new_state[i] -= liters_change
                    if new_state not in current_path:
                        current_path.append(new_state)
                        move_to_new_state(new_state)
                        current_path.pop()

if __name__ == "__main__":
    try:
        current_state = [0, 0, 0]
        move_to_new_state(current_state)
        print(solutions_count)
    except KeyboardInterrupt:
        print(solutions_count)
    
# Result: at least 44900799 solution
