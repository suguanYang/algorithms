package main

import "fmt"

var intToRomanDict = map[int]string{
	1000: "M",
	900:  "CM",
	500:  "D",
	400:  "CD",
	100:  "C",
	90:   "XC",
	50:   "L",
	40:   "XL",
	10:   "X",
	9:    "IX",
	5:    "V",
	4:    "IV",
	1:    "I",
}

func intToRoman(num int) string {
	if val, ok := intToRomanDict[num]; ok {
		return val
	}

	ints := [13]int{
		1000,
		900,
		500,
		400,
		100,
		90,
		50,
		40,
		10,
		9,
		5,
		4,
		1,
	}
	pc := 0

	var res = ""
	var count = num

	for count > 0 {
		for pc < 13 {
			if count >= ints[pc] {
				res += intToRomanDict[ints[pc]]
				count -= ints[pc]
			} else {
				pc++
			}
		}
	}

	return res

}

func main() {
	fmt.Println(intToRoman(1994))
}
