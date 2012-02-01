/*
 * prob004.h
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 *
 *
 *  Created on: Jan 31, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB004_H_
#define PROB004_H_

#include <stdio.h>
#include <math.h>

int isPalindrome(unsigned long num) {
	char buffer[256];
	int x = sprintf(buffer, "%lu", num);
	int i;

	for (i = 0; i < x / 2; ++i) {
		if (buffer[i] != buffer[x-i-1]) {
			return 0;
		}
	}

	return 1;
}

void problem004(void) {
	unsigned long palindrome;
	unsigned long temp;
	unsigned i, j;

	for (i = 999; i >= 100; --i) {
		for (j = 999; j >= 100; --j) {
			temp = i * j;
			if (temp < palindrome) {
				break;
			}
			else if (isPalindrome(temp) && temp > palindrome) {
				palindrome = temp;
				break;
			}
		}
	}

	printf("Answer: %lu\n", palindrome);
}

#endif /* PROB004_H_ */
