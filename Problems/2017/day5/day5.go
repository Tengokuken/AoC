package main

import (
	"aoc/goutils"
	"fmt"
	"strconv"
)

func traversal(instructions []int, sw bool) (count int) {
	curr, end := 0, len(instructions)
	for curr != end {
		val := instructions[curr]
		//fmt.Println("val", val)
		if sw && val >= 3 {
			instructions[curr] = val - 1
		} else {
			instructions[curr] = val + 1
		}
		curr += val
		count++
		//fmt.Println(instructions)
		//fmt.Println(curr)
	}
	return
}

func main() {
	// Part 1
	// Create an array containing each line as an element, then traverse to see how to get to the end
	lines, err := goutils.ReadLines("./input.txt")
	goutils.CheckErr(err)
	// fmt.Println(lines)
	instructions := make([]int, len(lines))
	// Populate the instructions array
	for i, num := range lines {
		n, err := strconv.Atoi(num)
		goutils.CheckErr(err)
		instructions[i] = n
	}

	count := traversal(instructions, false)
	fmt.Println(instructions)
	fmt.Println("count", count)

	// part 2
	// Repopulate the instructions array
	for i, num := range lines {
		n, err := strconv.Atoi(num)
		goutils.CheckErr(err)
		instructions[i] = n
	}
	count = traversal(instructions, true)
	fmt.Println(instructions)
	fmt.Println("count", count)
}
