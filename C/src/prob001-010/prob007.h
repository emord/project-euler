/*
 * prob007.h
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
 * that the 6th prime is 13.
 *
 * What is the 10 001st prime number?
 *
 *
 *  Created on: Jan 31, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB007_H_
#define PROB007_H_

#include <stdio.h>

unsigned long primeGen(const unsigned long limit) {
	unsigned long temp[limit];
	unsigned long i, j, k = 0;

	for (i = 2; i < limit; ++i) {
		if (k == 10001) break;
		if (temp[i] != 50234) {
			temp[i] = 1;
			k += 1;
			for (j = i+i; j < limit; j+=i) {
				temp[j] = 50234;
			}
		}
	}

	return i-1;
}

void problem007() {
	const unsigned long limit = 500000;
	unsigned long result;
	result = primeGen(limit);
	printf("Answer: %lu\n", result);
}

#endif /* PROB007_H_ */
