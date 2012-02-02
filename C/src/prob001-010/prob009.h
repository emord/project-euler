/*
 * prob009.h
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for
 * which, a^2 + b^2 = c^2
 *
 * For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 *
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 *
 *
 *  Created on: Feb 1, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB009_H_
#define PROB009_H_

#include <stdio.h>

void problem009() {
	int a, b, c;

	for (a = 1; ; ++a) {
		for (b = a; ; ++b) {
			c = 1000-a-b;
			if (a > c || b > c) break;
			if (c * c == a * a + b * b) break;
		}
		if (c * c == a * a + b * b) break;
	}

	printf("Answer: %d\n", a*b*c);
}

#endif /* PROB009_H_ */
