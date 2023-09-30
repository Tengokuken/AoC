package goutils

import (
	"strconv"
	"reflect"
	"fmt"
	"math"
)

type Generic struct{reflect.Type}

func ConvArrStrToInt(strArr []string) []int {
	nums := make([]int, 0)
	for _, num := range strArr {
		n, err := strconv.Atoi(num)
		CheckErr(err)
		nums = append(nums, n)
	}
	return nums
}

// TODO: I think you might be able to do it with generics...
func Init2DGrid(t string, rows int, cols int) interface{} {
	if t == "int" {
		grid := make([][]int, rows)
		for i := range grid {
			grid[i] = make([]int, cols)
		}
		return grid
	} else {
		return make([][]string, rows)
	}
	//grid := make([][]any, rows)
	//for i := range grid {
	//	grid[i] = make([]any, cols)
	//}
	
}

// Uses generics wow
func Print2DGrid[T any](grid [][]T) {
	for _, i := range grid {
		for _, j := range i {
			fmt.Print(j, " ")
		}
		fmt.Println("")
	}
}

func GetMaxElement(arr []int) (largest int, ind int) {
	// For ties, don't update ind
	largest = math.MinInt
	for i, e := range arr {
		if e > largest {
			largest = arr[i]
			ind = i
		}
	}
	return
}