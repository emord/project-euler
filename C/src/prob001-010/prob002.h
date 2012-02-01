/*
 * prob002.h
 * Each new term in the Fibonacci sequence is generated by adding the previous
 * two terms. By starting with 1 and 2, the first 10 terms will be:
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 * By considering the terms in the Fibonacci sequence whose values do not exceed
 * four million, find the sum of the even-valued terms.
 *  Created on: Jan 31, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB002_H_
#define PROB002_H_

#include <stdio.h>

void problem002(void) {
	unsigned a = 1;
	unsigned b = 2;
	unsigned i = 2;
	unsigned sum = 2;

	while (b <= 4000000) {
		b += a;
		a = b - a;
		++i;
		if (b % 2 == 0) {
			sum += b;
		}
	}

	printf("Answer: %u\n", sum);
}

#endif /* PROB002_H_ */