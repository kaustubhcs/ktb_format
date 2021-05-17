# Imports
# from ktb_class import ktb
from ktb_format.ktb_mtx import mtx2ktb, ktb_matrix_write
from ktb_format.ktb_class import *

DATA_DIR = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/rmat"
OUTPUT_DATA_DIR = "/home/ktb/git/sparse_matrix_data_generator/sparse_matrix_data/ktb/rmat"


def input_matrix_filename_generator(edge_value, rmat_power, matrix_index):
    matrix_filename = ""
    if matrix_index == "A":
        matrix_filename = DATA_DIR + "/edge_" + \
            str(edge_value) + "/rmat_A_" + str(rmat_power) + ".mtx"
    elif matrix_index == "B":
        matrix_filename = DATA_DIR + "/edge_" + \
            str(edge_value) + "/rmat_B_" + str(rmat_power) + ".mtx"
    return matrix_filename


def output_matrix_filename_generator(edge_value, rmat_power, matrix_index):
    matrix_filename = ""
    if matrix_index == "A":
        matrix_filename = OUTPUT_DATA_DIR + "/edge_" + \
            str(edge_value) + "/rmat_A_" + str(rmat_power) + ".ktb"
    elif matrix_index == "B":
        matrix_filename = DATA_DIR + "/edge_" + \
            str(edge_value) + "/rmat_B_" + str(rmat_power) + ".ktb"
    return matrix_filename


EDGE_VALUE = 8
RMAT_POWER = [2, 10, 14]


for r in RMAT_POWER:
    print("Converting Mat A, RMAT: " + str(r))
    ktb_mat_A = mtx2ktb(input_matrix_filename_generator(
        EDGE_VALUE, r, "A"), TYPE_FLOAT)
    ktb_matrix_write(
        ktb_mat_A, output_matrix_filename_generator(EDGE_VALUE, r, "A"))
    print("Converting Mat B, RMAT: " + str(r))
    ktb_mat_B = mtx2ktb(input_matrix_filename_generator(
        EDGE_VALUE, r, "B"), TYPE_FLOAT)
    ktb_matrix_write(
        ktb_mat_B, output_matrix_filename_generator(EDGE_VALUE, r, "B"))

print("Done")
