package main

import (
	"aoc/goutils"
	"fmt"
	"strings"
	"strconv"
)

func main() {
	// Part 1
	// 16 banks, 1 bank holds as many blocks. Reallocate by balancing the blocks btwn banks.
	// Each cycle, find bank with most blocks (ties are the lower num bank) and redist those blocks.
	// Remove all blocks from selected, then add one to the next index mem bank, until all are gone 16 -> 1
	// Count how many cycles until there is a configuration that was already seen

	// Create an array containing each line as an element, then traverse to see how to get to the end
	line, _, err := goutils.ReadNthLine("./input.txt", 0)
	goutils.CheckErr(err)
	// fmt.Println(lines)
	lineArr := strings.Split(line, "\t")
	banks := goutils.ConvArrStrToInt(lineArr)
	fmt.Println(banks)
	// config stores the banks as well as when they were seen (for part 2)
	configs := map[string]int{}
	count, prev := 0, 0
	for {
		elem, ind := goutils.GetMaxElement(banks)
		banks[ind] = 0
		//fmt.Println(elem, ind)
		for i := 0; i < elem; i++ {
			if ind == len(banks) - 1 {
				ind = 0
			} else {
				ind++
			}
			banks[ind]++
		}
		// Convert banks to its string representation
		var bankStr string
		for _, e := range banks {
			bankStr += strconv.Itoa(e) + " "
		}
		fmt.Println(banks)
		count++
		// Check time
		var exist bool
		if prev, exist = configs[bankStr]; exist {
			fmt.Println("this is bad", bankStr, "exists")
			break
		}
		configs[bankStr] = count
	}
	fmt.Println("part 1", count, "part 2", count-prev)
}
