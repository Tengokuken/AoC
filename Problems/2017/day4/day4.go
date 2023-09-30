package main

import (
	"aoc/goutils"
	"fmt"
	"sort"
	"strings"
)

func main() {
	// Part 1
	lines, err := goutils.ReadLines("./input.txt")
	goutils.CheckErr(err)
	// fmt.Println(lines)
	total := 0
	for _, line := range lines {
		badPass := false
		// Create set
		phrases := map[string]bool{}
		phasesArr := strings.Fields(line)
		for _, phrase := range phasesArr {
			// btw exist is only in scope in this if with this type of if
			if _, exist := phrases[phrase]; exist {
				badPass = true
				break
			}
			phrases[phrase] = true
		}
		if !badPass {
			total++
		}
	}
	fmt.Println(total)

	// Part 2
	total = 0
	for _, line := range lines {
		badPass := false
		// Create set of sorted string
		phrases := map[string]bool{}
		phasesArr := strings.Fields(line)
		for _, phrase := range phasesArr {
			sortedPhrase := []rune(phrase)
			sort.Slice(sortedPhrase, func(i, j int) bool {
				return sortedPhrase[i] < sortedPhrase[j] //sort the string rune
			})

			if _, exist := phrases[string(sortedPhrase)]; exist {
				badPass = true
				break
			}
			phrases[string(sortedPhrase)] = true
		}
		if !badPass {
			total++
		}
	}
	fmt.Println(total)
}
