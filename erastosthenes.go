package main

import (
	"fmt"
)

func main(){
	Erastosthenes(int64(100))	
}

func Erastosthenes(n int64) ([]int64) {
	shleve := make([]bool, n+1)

	shleve[0] = true
	shleve[1] = true
	var primes []int64
	for i := int64(2); i <= n; i++ {
		if (!shleve[i]) {
			primes = append(primes, i)
			for j := int64(i); i * j < n + 1; j++ {
				shleve[i*j] = true
			}
		}
	}
	fmt.Println(len(primes))

	return primes
}
