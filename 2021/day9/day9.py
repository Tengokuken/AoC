height_map = []
basin_map = []
def low_lows(lines):
    # First, generate the 2d array
    risk_level_val = 0
    height_map = []
    for line in lines:
        row = [int(x) for x in line]
        height_map.append(row)
    num_rows = len(height_map)
    num_cols = len(height_map[0])
    # Find risk areas - numbers where adjacent numbers are all higher
    for row in range(num_rows):
        for col in range(num_cols):
            cur = height_map[row][col]
            if cur == 9:
                continue
            # Check if not in parameter
            if row != 0 and row != num_rows - 1 and col != 0 and col != num_cols - 1:
                # check surroundings
                if cur < height_map[row-1][col] and cur < height_map[row+1][col] and cur < height_map[row][col-1]\
                        and cur < height_map[row][col+1]:
                    risk_level_val += cur + 1
            # else check parameter cases
            elif row == 0:
                if col != 0 and col != num_cols - 1:
                    if cur < height_map[row+1][col] and cur < height_map[row][col-1] and cur < height_map[row][col+1]:
                        risk_level_val += cur + 1
                elif col == 0:
                    if cur < height_map[row+1][col] and cur < height_map[row][col+1]:
                        risk_level_val += cur + 1
                elif col == num_cols - 1:
                    if cur < height_map[row+1][col] and cur < height_map[row][col-1]:
                        risk_level_val += cur + 1
            elif row == num_rows - 1:
                if col != 0 and col != num_cols - 1:
                    if cur < height_map[row-1][col] and cur < height_map[row][col-1] and cur < height_map[row][col+1]:
                        risk_level_val += cur + 1
                elif col == 0:
                    if cur < height_map[row-1][col] and cur < height_map[row][col+1]:
                        risk_level_val += cur + 1
                elif col == num_cols - 1:
                    if cur < height_map[row-1][col] and cur < height_map[row][col-1]:
                        risk_level_val += cur + 1
            # for cols, dont need to check corners
            elif col == 0:
                if row != 0 and row != num_rows - 1:
                    if cur < height_map[row][col+1] and cur < height_map[row-1][col] and cur < height_map[row+1][col]:
                        risk_level_val += cur + 1
            elif col == num_cols - 1:
                if row != 0 and row != num_rows - 1:
                    if cur < height_map[row][col-1] and cur < height_map[row-1][col] and cur < height_map[row+1][col]:
                        risk_level_val += cur + 1
    return risk_level_val

# To prevent double counting
def surrounded_larger(x, y):
    count = 0
    cur = height_map[x][y]
    if cur < height_map[x-1][y]:
        count += 1
    if cur < height_map[x+1][y]:
        count += 1
    if cur < height_map[x][y-1]:
        count += 1 
    if cur < height_map[x][y-1]:
        count += 1
    if cur == 2:
        print(count)
    return 1 if count > 0 else 0
    
def update_basin(x, y, blocked):
    # If adjacent is smaller, give it val + 1.
    # Else if larger, give it val - 1 maybe??
    cur = height_map[x][y]
    #vals = [1]
    #if 'up' not in blocked: # not upper tile
    #    if cur < height_map[x-1][y]:
    #        vals.append(basin_map[x-1][y] + 1)
    #if 'down' not in blocked: # not bottom tile
    #    if cur < height_map[x+1][y]:
    #        vals.append(basin_map[x+1][y] + 1)
    #if 'left' not in blocked: # not left tile
    #    if cur < height_map[x][y-1]:
    #        vals.append(basin_map[x][y-1] + 1)
    #if 'right' not in blocked: # not right tile
    #    if cur < height_map[x][y+1]:
    #        vals.append(basin_map[x][y+1] + 1)
    val = 0
    
    #if 'up' not in blocked and height_map[x-1][y] != 9 and cur < height_map[x-1][y]:
    #    basin_map[x-1][y] = val - 1
    #if 'down' not in blocked and height_map[x+1][y] != 9 and cur < height_map[x+1][y]:
    #    basin_map[x+1][y] = val - 1
    #if 'left' not in blocked and height_map[x][y-1] != 9 and cur < height_map[x][y-1]:
    #    basin_map[x][y-1] = val - 1
    #if 'right' not in blocked and height_map[x][y+1] != 9 and cur < height_map[x][y+1]:
    #    basin_map[x][y+1] = val - 1
    double_counting = 0
    if height_map[x-1][y] != 9 and cur < height_map[x-1][y]:
        val += basin_map[x-1][y]
        double_counting += surrounded_larger(x-1, y)
    if height_map[x+1][y] != 9 and cur < height_map[x+1][y]:
        val += basin_map[x+1][y]
        double_counting += surrounded_larger(x+1, y)
    if height_map[x][y-1] != 9 and cur < height_map[x][y-1]:
        val += basin_map[x][y-1]
        double_counting += surrounded_larger(x, y-1)
    if height_map[x][y+1] != 9 and cur < height_map[x][y+1]:
        val += basin_map[x][y+1]
        double_counting += surrounded_larger(x, y+1)
    if cur != 9 and double_counting <= 1:
        val += 1
    basin_map[x][y] = val

def basculin(lines):
    # TODO: just use dfs lol
    # First, generate the 2d array
    risk_level_val = 0
    top_bot = [9] * (len(lines[0]) + 2)
    height_map.append(top_bot)
    basin_map.append([1] * (len(lines[0]) + 2))
    for line in lines:
        row = [int(x) for x in line]
        basin_map.append([1] * (len(row) + 2))
        row.insert(0, 9)
        row.append(9)
        height_map.append(row)
    height_map.append(top_bot)
    basin_map.append([1] * (len(lines[0]) + 2))
    print(height_map)
    num_rows = len(height_map)
    num_cols = len(height_map[0])

    # If ANY of the adjacent tiles are smaller, this tile flows into a basin
    for i in range(8, -1, -1):
        for row in range(num_rows):
            for col in range(num_cols):
                blocked = []
                cur = height_map[row][col]
                if cur == 9:
                    basin_map[row][col] = 0
                    continue
                elif cur == i:
                    update_basin(row, col, blocked)
    print(basin_map)
    return risk_level_val

if __name__ == "__main__":
    with open("test.txt") as f:
        lines = f.read().splitlines()
    danger = low_lows(lines)
    print(danger)
    numbers = basculin(lines)
    print(numbers)