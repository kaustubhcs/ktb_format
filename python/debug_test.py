# Imports
# from ktb_class import ktb
from ktb_format.ktb_mtx import mtx2ktb, ktb_matrix_write
from ktb_format.ktb_class import *

# CONFIGURABLES
DATA_DIR = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/rmat"
EDGE_VALUE = 8
RMAT_POWER = 23
RMAT_DIR = DATA_DIR + "/edge_" + str(EDGE_VALUE)
INPUT_MATRIX_A = RMAT_DIR + "/rmat_A_" + str(RMAT_POWER) + ".mtx"
INPUT_MATRIX_B = RMAT_DIR + "/rmat_B_" + str(RMAT_POWER) + ".mtx"

OUTPUT_DIR = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/ktb/rmat/edge_" + \
    str(EDGE_VALUE)
OUTPUT_MATRIX_A = OUTPUT_DIR + "/rmat_A_" + str(RMAT_POWER) + ".ktb"
OUTPUT_MATRIX_B = OUTPUT_DIR + "/rmat_B_" + str(RMAT_POWER) + ".ktb"

# CODE

print("Converting Mat A...")
ktb_mat_A = mtx2ktb(INPUT_MATRIX_A, TYPE_FLOAT)
ktb_matrix_write(ktb_mat_A, OUTPUT_MATRIX_A)
print("Converting Mat B...")
ktb_mat_B = mtx2ktb(INPUT_MATRIX_B, TYPE_FLOAT)
ktb_matrix_write(ktb_mat_B, OUTPUT_MATRIX_B)
print("Done")
