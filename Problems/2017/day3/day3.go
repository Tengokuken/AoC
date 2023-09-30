package main

import (
    "fmt"
	"aoc/goutils"
    "math"
)

func sumSurrounding(grid [][]int, i int, j int) int {
	return grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 1][j] + grid[i + 1][j - 1] + grid[i][j - 1] + grid[i - 1][j - 1]
}

func main() {
    // Part 1
    // Get the range of the squares. Find the range between (1+2i)^2
	//input := 277678
	input := 900
	var startRange, endRange, rad int = 1, 3, 1
	for {
		//fmt.Println(math.Pow(float64(startRange), 2), math.Pow(float64(endRange), 2))
		if float64(input) >= math.Pow(float64(startRange), 2) && float64(input) <= math.Pow(float64(endRange), 2) {
			break
		}
		startRange = endRange
		endRange += 2
		rad++
	}
	startRange = int(math.Pow(float64(startRange), 2))
	endRange = int(math.Pow(float64(endRange), 2))
	// In a square, endRange is in grid[rad][rad]. grid[rad-1][rad] = startRange + 1
	// Use this fact to count the spiral
	sideLen := 2*rad + 1
	//fmt.Println("sidelen", sideLen)
	// Get each corner number. The distance to these numbers is always rad ^ 2
	botRight := endRange
	botLeft := botRight - sideLen + 1
	topLeft := botLeft - sideLen + 1
	topRight := topLeft - sideLen + 1
	//fmt.Println(input, botRight, botLeft, topLeft, topRight)
	// Find the distance from the midpoint of each side
	var dist float64
	switch {
		case input == botRight || input == botLeft || input == topLeft || input == topRight: {
			dist = float64(rad)
		}
		case input < botRight && input > botLeft:
			// grid[x][sideLength]
			dist = math.Abs(float64(input - ((botRight + botLeft) / 2)))
			//fmt.Println("Bottom", dist)
		case input < botLeft && input > topLeft:
			// grid[0][x]
			dist = math.Abs(float64(input - ((botLeft + topLeft) / 2)))
			//fmt.Println("Left", dist)
		case input < topLeft && input > topRight:
			// grid[x][0]
			dist = math.Abs(float64(input - ((topLeft + topRight) / 2)))
			//fmt.Println("Top", dist)
		default:
			// grid[sideLength][x]
			dist = math.Abs(float64(input - ((startRange + topRight) / 2)))
			//fmt.Println("Right", dist)
	}
	fmt.Println(float64(rad) + dist)

	

    // Part 2
    // Make 2d square with same radius, the number will be smaller than this array (initialized with 0)
	var grid [][]int
	grid = (goutils.Init2DGrid("int", rad + 10, rad + 10)).([][]int)
	//fmt.Println(rad)
	// Put 1 at the centre of the grid (grid[rad][rad])
	grid[rad][rad] = 1
	// Start summing the spiral. Find the number that fulfils the requirement
	row := rad
	col := rad
	i := 1
	val := 1
	// Spiral algorithm: right 1, up i, left i + 1, down i+1, right i + 1, i += 2, repeat
	found := false
	for {
		col += 1
		val = sumSurrounding(grid, row, col)
		//fmt.Println(row, col, val)
		grid[row][col] = val
		
		if found { break }
		for k := 0; k < i; k++ {
			row--
			val = sumSurrounding(grid, row, col)
			grid[row][col] = val
			//fmt.Println(row, col, val)
			if val > input {
				found = true
				break
			}
		}

		if found { break }
		for k := 0; k < i + 1; k++ {
			col--
			val = sumSurrounding(grid, row, col)
			grid[row][col] = val
			//fmt.Println(row, col, val)
			if val > input {
				found = true
				break
			}
		}

		if found { break }
		for k := 0; k < i + 1; k++ {
			row++
			val = sumSurrounding(grid, row, col)
			grid[row][col] = val
			//fmt.Println(row, col, val)
			if val > input {
				found = true
				break
			}
		}

		if found { break }
		for k := 0; k < i + 1; k++ {
			col++
			val = sumSurrounding(grid, row, col)
			grid[row][col] = val
			//fmt.Println(row, col, val)
			if val > input {
				found = true
				break
			}
		}
		i += 2
	}
	fmt.Println(val)
	goutils.Print2DGrid(grid)
}