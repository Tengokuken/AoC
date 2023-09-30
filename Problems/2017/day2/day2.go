package main

import (
    "fmt"
	"aoc/goutils"
    "strings"
    "slices"
)



func main() {
    // Part 1
    lines, err := goutils.ReadLines("./input.txt")
    goutils.CheckErr(err)
    //fmt.Println(lines)
    total := 0
    // Read each line, add and output
    for _, line := range lines {
        numsString := strings.Split(line, "\t")
        nums := goutils.ConvArrStrToInt(numsString)
        checkSum := slices.Max(nums) - slices.Min(nums)
        // Get the check sum
        total += checkSum
    }    
    fmt.Println(total)

    // Part 2
    //lines, err = goutils.ReadLines("./test2.txt")
    goutils.CheckErr(err)
    total = 0
    // Go through each line
    for _, line := range lines {
        numsString := strings.Split(line, "\t")
        nums := goutils.ConvArrStrToInt(numsString)
        checkSum := 0
        // In each line, check if they are divisible with mod. Keep going until you find it, no need to backtrack
        // Use sliding window to check if some pair of numbers is divisible
        for i, num := range nums {
            for j := i + 1; j < len(nums); j++ {
                maxN := max(num, nums[j])
                minN := min(num, nums[j])
                if (maxN % minN == 0) {
                    checkSum = maxN / minN
                    break
                }
            }
        }
        // Get the check sum
        total += checkSum
    }    
    fmt.Println(total)
}