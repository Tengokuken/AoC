package goutils

import (
    "bufio"
    "fmt"
    "os"
    "io"
    "io/ioutil"
)

func CheckErr(e error) {
    if e != nil {
        panic(e)
    }
}

// Private because lowercase
func openFile(filepath string) (*os.File, error) {
	f, err := os.Open(filepath)
    CheckErr(err)
	return f, err
}

func ReadFile(filepath string) {
	file, err := openFile(filepath)
    CheckErr(err)
    b, err := ioutil.ReadAll(file)
    fmt.Print(b)
}

func ReadBytes(filepath string, numBytes int) []byte {
	f, err := openFile(filepath)
    defer f.Close() // defer closes the file after the function has executed in LIFO order
	// <make>() makes a dynamically-sized array. Second inits with num zeros, third argument specifies capacity 
	b1 := make([]byte, 0)
    n1, err := f.Read(b1)
    CheckErr(err)
    fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))
    return b1
}

func ReadLines(filepath string) ([]string, error)  {
	f, err := openFile(filepath)
    defer f.Close() // defer closes the file after the function has executed in LIFO order
	CheckErr(err)
	scanner := bufio.NewScanner(f)
    lines := make([]string, 0)
    // optionally, resize scanner's capacity for lines over 64K, see next example
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
	CheckErr(scanner.Err())
    return lines, nil
}

/// Reads the 0-based nth line in a file and returns it. currLine returns the found line, otherwise the EOF
func ReadNthLine(filepath string, lineNum int) (line string, currLine int, err error) {
    f, err := openFile(filepath)
    defer f.Close() // defer closes the file after the function has executed in LIFO order
	CheckErr(err)
	sc := bufio.NewScanner(f)
    for sc.Scan() {
        if currLine == lineNum {
            return sc.Text(), currLine, sc.Err()
        }
        currLine++
    }
    return line, currLine, io.EOF
}