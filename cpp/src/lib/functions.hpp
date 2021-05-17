#ifndef FUNCTIONS_HPP
#define FUNCTIONS_HPP

#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <array>
#include <cmath>
#include <fstream>

struct Input
{
	long *number;
};

#define CHECK_CUDA(func)                                               \
	{                                                                  \
		cudaError_t status = (func);                                   \
		if (status != cudaSuccess)                                     \
		{                                                              \
			printf("CUDA API failed at line %d with error: %s (%d)\n", \
				   __LINE__, cudaGetErrorString(status), status);      \
		}                                                              \
	}

Input get_inputs(int, char **, Input, int printer = 0);
void print_inputs(int, Input);

#endif // FUNCTIONS_HPP
