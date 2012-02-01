/*
 * prob006.h
 * The sum of the squares of the first ten natural numbers is,
 * 1^2 + 2^2 + ... + 10^2 = 385
 *
 * The square of the sum of the first ten natural numbers is,
 * (1 + 2 + ... + 10)^2 = 552 = 3025
 *
 * Hence the difference between the sum of the squares of the first ten natural
 * numbers and the square of the sum is 3025 − 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first one hundred
 * natural numbers and the square of the sum.
 *
 *  Created on: Jan 31, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB006_H_
#define PROB006_H_

#include <math.h>
#include <stdio.h>

unsigned long sumOfSquares(const int limit) {
	unsigned long result = 0;
	int i;
	for (i = 1; i <= limit; ++i) {
		result += i*i;
	}
	return result;
}

unsigned long squareOfSums(const int limit) {
	unsigned long result = 0;
	int i;
	for (i = 1; i <= limit; ++i) {
		result += i;
	}

	return result * result;
}

void problem006(void) {
	const int limit = 100;

	printf("Answer: %lu\n", squareOfSums(limit)-sumOfSquares(limit));
}

#endif /* PROB006_H_ */
