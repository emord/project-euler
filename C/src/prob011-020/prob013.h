/*
 * prob013.h
 * Work out the first ten digits of the sum of the following one-hundred
 * 50-digit numbers.
 *
 *  Created on: Feb 1, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB013_H_
#define PROB013_H_

#include <stdio.h>
#include <stdlib.h>

void problem013() {
	FILE* file = fopen("src/prob011-020/prob013.dat", "r");
	double sum = 0;
	int i;
	char line[100];
	for (i = 0; i < 100; ++i) {
		fgets(line,100,file);
		sum += atof(line);
	}

	printf("Answer: %3.7f\n", sum);
}

#endif /* PROB013_H_ */
