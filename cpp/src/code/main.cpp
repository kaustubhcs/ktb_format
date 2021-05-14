// Created by Kaustubh Shivdikar
//
//  (C) All Rights Reserved

#include "../lib/functions.hpp"
#include "../lib/debugger.hpp"
#include "../lib/ktb_io.hpp"

using namespace std;

// Global Variables

// ************ MAIN FUNCTION ************

int main(int argc, char *argv[])
{

	Input input;
	get_inputs(argc, argv, input, 1);

	string mat_A_file = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/ktb/rmat/edge_8/rmat_A_2.ktb";

	ktb *mat_A;
	mat_A = ktb_read_mtx(mat_A_file.c_str());
	ktb_printer(mat_A);

	cout << "\n\e[1;31mProgram End\e[0m\n\n\n";
	return 0;
}
