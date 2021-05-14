# Imports
# from ktb_class import ktb
from ktb_format.ktb_mtx import mtx2ktb, ktb_matrix_write
from ktb_format.ktb_class import *

# CONFIGURABLES
INPUT_MATRIX = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/rmat/edge_8/rmat_A_2.mtx"
OUTPUT_FILENAME = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/ktb/rmat/edge_8/rmat_A_2.ktb"

# CODE

ktb_mat_A = mtx2ktb(INPUT_MATRIX, TYPE_DOUBLE)
ktb_matrix_write(ktb_mat_A, OUTPUT_FILENAME)
print("Done")
