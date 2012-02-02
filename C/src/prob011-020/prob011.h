/*
 * prob011.h
 * In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
 *
 * The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
 *
 * What is the greatest product of four adjacent numbers in any direction
 * (up, down, left, right, or diagonally) in the 20×20 grid?
 *
 *  Created on: Feb 1, 2012
 *      Author: Jonathan Emord
 */

#ifndef PROB011_H_
#define PROB011_H_

#include <stdio.h>

void problem011() {
	int nums[20][20];
	FILE* file = fopen("src/prob011-020/prob011.dat", "r");
	int i, j;
	char c;

	for (i = 0; i < 20; ++i) {
		for(j = 0; j < 20; ++j) {
			fread(&c, 1, 1, file);
			nums[i][j] = (c-'0')*10;
			fread(&c, 1, 1, file);
			nums[i][j] += (c-'0');
			fread(&c, 1, 1, file);
		}
	}

	unsigned long result = 0;
	unsigned long t1;

	for (i = 0; i < 20; ++i) {
		for (j = 0; j < 17; ++j) {
			t1 = nums[i][j] * nums[i][j+1] * nums[i][j+2] * nums[i][j+3];
			if (t1 > result) result = t1;
		}
	}
	for (i = 0; i < 17; ++i) {
		for (j = 0; j < 17; ++j) {
			t1 = nums[i][j] * nums[i+1][j+1] * nums[i+2][j+2] * nums[i+3][j+3];
			if (t1 > result) result = t1;
		}
	}
	for (i = 0; i < 17; ++i) {
		for (j = 0; j < 20; ++j) {
			t1 = nums[i][j] * nums[i+1][j] * nums[i+2][j] * nums[i+3][j];
			if (t1 > result) result = t1;
		}
	}
	for (i = 0; i < 17; ++i) {
		for (j = 3; j < 20; ++j) {
			t1 = nums[i][j] * nums[i+1][j-1] * nums[i+2][j-2] * nums[i+3][j-3];
			if (t1 > result) result = t1;
		}
	}

	printf("Answer: %lu\n", result);
}

#endif /* PROB011_H_ */
