/*
 * prob001.h
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *  Created on: Jan 31, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB001_H_
#define PROB001_H_

#include <stdio.h>

void problem001(void) {
	unsigned sum = 0;

	int i;
	for (i = 1; i < 1000; ++i) {
		if ((i % 3 == 0) || (i % 5 == 0))
			sum += i;
	}

	printf("Answer: %u\n", sum);
}

#endif /* PROB001_H_ */
