/*
 * prob010.h
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million.
 *
 *  Created on: Feb 1, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB010_H_
#define PROB010_H_

#include <stdio.h>

unsigned long long sumOfPrimes(const unsigned long limit) {
	int temp[limit];
	unsigned long i, j;
	unsigned long long sum = 0;

	for (i = 0; i < limit; ++i)
		temp[i] = 1;

	for (i = 2; i < limit; ++i) {
		if (temp[i] != 0) {
			temp[i] = 1;
			sum += i;
			for (j = i+i; j < limit; j+=i) {
				temp[j] = 0;
			}
		}
	}

	return sum;
}

void problem010() {
	printf("Answer: %llu\n", sumOfPrimes(2000000L));
}

#endif /* PROB010_H_ */
