/*
 * prob003.h
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 *
 *  Created on: Jan 31, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB003_H_
#define PROB003_H_

#include <stdio.h>

void problem003() {
	unsigned long num = 600851475143;
	unsigned long result = 0;

	unsigned i = 2;
	while (num != 1) {
		if (num % i == 0) {
			num /= i;
			result = i;
		}
		else {
			++i;
		}
	}

	printf("Answer: %lu\n", result);
}


#endif /* PROB003_H_ */
