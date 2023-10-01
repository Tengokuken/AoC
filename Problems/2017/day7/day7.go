package main

import (
	"aoc/goutils"
	"fmt"
	"strings"
	"strconv"
)

type Program struct {
	name string
	weight int32
	programs []string
	parent string
}

func (p Program) String() string {
	return fmt.Sprintf("Program %v with weight %v and the following programs: %v", p.name, p.weight, p.programs)
}

// type Node struct {
// 	self Program
// 	parent Program
// }

func main() {
	// Part 1
	// Take each line as a node in a tree. Create a Program struct for each of the programs in lines.
	// Then, it should be as simple as assigning a parent to all but one Program object. 
	// The one without a parent is the bottom program.
	// Alternatively, you could use a tree data structure?

	// Create an array containing each line as an element, then traverse to see how to get to the end
	lines, err := goutils.ReadLines("./test.txt")
	goutils.CheckErr(err)
	programs := make([]Program, len(lines))
	// fmt.Println(lines)
	for i, line := range lines {
		l := strings.Split(line, " -> ")
		self := strings.Split(l[0], " ")
		weight := strings.TrimFunc(self[1], func(r rune) bool {
			return r == '(' || r == ')'
		})
		v, _ := strconv.Atoi(weight)
		subprograms := make([]string, 0)
		if len(l) > 1 {
			a := strings.Split(l[1], ", ")
			copy(subprograms, a)
		}
		programs[i] = Program{self[0], int32(v), subprograms, ""}
		fmt.Println(programs[i])
	}
}
