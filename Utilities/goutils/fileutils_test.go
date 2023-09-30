package goutils

import (
    "testing"
    "regexp"
	"io"
)

// Not needed bc theres no return
//func TestReadFile(t *testing.T) {
//	want := `The Quick Brown Fox
//	Jumped
//	Over The
	
//	Lazy
//	Dog.`
//	content, err := ReadFile("./test.txt")
//    if !want.MatchString(content) || err != nil {
//        t.Fatalf("this no write")
//    }
//}


func TestReadLines(t *testing.T) {
	text := [6]string{"The Quick Brown Fox","Jumped","Over The","","Lazy","Dog."}
	content, err := ReadLines("./test.txt")
	for a, b := range text {
		want := regexp.MustCompile(b)
		if !want.MatchString(content[a]) || err != nil {
			t.Fatalf("this no write expected " + text[a] + " got " + content[a])
		}
	}
    
}

func TestReadNthLine(t *testing.T) {
    text := "The Quick Brown Fox"
	want := regexp.MustCompile(text)
	content, _, err := ReadNthLine("./test.txt", 0)
    if !want.MatchString(content) || err != nil {
        t.Fatalf("this no write expected " + text + " got " + content)
    }
	text = "Jumped"
	want = regexp.MustCompile(text)
	content, _, err = ReadNthLine("./test.txt", 1)
    if !want.MatchString(content) || err != nil {
        t.Fatalf("this no write expected " + text + " got " + content)
    }
	text = "Over The"
	want = regexp.MustCompile(text)
	content, _, err = ReadNthLine("./test.txt", 2)
    if !want.MatchString(content) || err != nil {
        t.Fatalf("this no write expected " + text + " got " + content)
    }
	text = ""
	want = regexp.MustCompile(text)
	content, _, err = ReadNthLine("./test.txt", 3)
    if !want.MatchString(content) || err != nil {
        t.Fatalf("this no write expected " + text + " got " + content)
    }
	text = "Lazy"
	want = regexp.MustCompile(text)
	content, _, err = ReadNthLine("./test.txt", 4)
    if !want.MatchString(content) || err != nil {
        t.Fatalf("this no write expected " + text + " got " + content)
    }
	text = "Dog."
	want = regexp.MustCompile(text)
	content, _, err = ReadNthLine("./test.txt", 5)
    if !want.MatchString(content) || err != nil {
        t.Fatalf("this no write expected " + text + " got " + content)
    }
}

func TestReadNthPlus1Line(t *testing.T) {
	content, _, err := ReadNthLine("./test.txt", 6)
    if content != "" || err == nil {
        t.Fatalf("this no write should have no")
    }
}

func TestReadEOFLine(t *testing.T) {
	content, eofLine, err := ReadNthLine("./test.txt", 100000)
    if content != "" || err != io.EOF || eofLine != 6 {
        t.Fatalf("this no write should have no")
    }
}