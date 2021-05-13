from .ktb_class import ktb
from scipy.io import mmread
from pathlib import Path
from struct import pack


def mtx2ktb(file_path, precision=8):
    if (precision != 4 and precision != 8):
        raise Exception("Precision has to be either 4 or 8")
    file_object = Path(file_path)
    if not(file_object.is_file()):
        raise Exception("File does not exist: " + file_path)
    ktb_object = ktb()
    mmr_file = mmread(file_path)
    csr_file = mmr_file.tocsr()
    row_ptr = csr_file.indptr
    col_idx = csr_file.indices
    data = csr_file.data
    matrix_size = len(row_ptr) - 1
    ktb_object.readme_content = \
        "\nCSR File\n" + \
        "Matrix Dimensions: " + str(matrix_size) + " x " + str(matrix_size) + "\n" + \
        "Number of non-zeros: " + str(len(data)) + "\n"
    ktb_object.readme_size = len(ktb_object.readme_content)
    # Create 3 variables
    # 0. row_ptr (4B)
    # 1. col_idx (4B)
    # 2. data (4B or 8B).
    ktb_object.variable_count = 3
    ktb_object.variable_type_array = [4, 4, precision]
    ktb_object.variable_count_array = [len(row_ptr), len(col_idx), len(data)]
    ktb_object.variable_data_array = [row_ptr, col_idx, data]
    ktb_object.error_check_flag = 'K'
    return ktb_object


def pack_int_array(variable_array):
    h_variable_array = []
    for i in range(len(variable_array)):
        h_variable_array.append(pack('<i', variable_array[i]))
    return h_variable_array


def pack_long_long_array(variable_array):
    h_variable_array = []
    for i in range(len(variable_array)):
        h_variable_array.append(pack('<q', variable_array[i]))
    return h_variable_array


def pack_float_array(variable_array):
    h_variable_array = []
    for i in range(len(variable_array)):
        h_variable_array.append(pack('<f', variable_array[i]))
    return h_variable_array


def pack_double_array(variable_array):
    h_variable_array = []
    for i in range(len(variable_array)):
        h_variable_array.append(pack('<d', variable_array[i]))
    return h_variable_array


def ktb_matrix_write(ktb_matrix, outfile_name):
    # h_ corresponds to hex packed format of the number (INT or FLOAT).
    h_readme_size = []
    h_readme_size.append(pack('<i', ktb_matrix.readme_size))
    h_variable_count = []
    h_variable_count.append(pack('<i', ktb_matrix.variable_count))
    h_variable_type_array = pack_int_array(ktb_matrix.variable_type_array)
    h_variable_count_array = pack_int_array(ktb_matrix.variable_count_array)
    h_readme_content = (ktb_matrix.readme_content).encode('ascii')

    # TODO: Set offset values.
    INT_SIZE = 4  # In bytes
    LONG_LONG_SIZE = 8  # In bytes
    FLOAT_SIZE = 4  # In bytes
    DOUBLE_SIZE = 8  # In bytes
    CHAR_SIZE = 1  # In bytes

    ktb_matrix.variable_offset_array = [0, 0, 0]
    h_variable_offset_array = pack_int_array(ktb_matrix.variable_offset_array)
    headline_size = (INT_SIZE * len(h_readme_size)) + \
        (CHAR_SIZE * len(h_readme_content)) + \
        (INT_SIZE * len(h_variable_count)) + \
        (INT_SIZE * len(h_variable_type_array)) + \
        (INT_SIZE * len(h_variable_offset_array)) + \
        (INT_SIZE * len(h_variable_count_array))

    h_row_ptr_array = pack_int_array(ktb_matrix.variable_data_array[0])
    h_col_idx_array = pack_int_array(ktb_matrix.variable_data_array[1])
    h_data = []
    if ktb_matrix.variable_type_array[2] == 4:
        h_data = pack_float_array(ktb_matrix.variable_data_array[2])
    elif ktb_matrix.variable_type_array[2] == 8:
        h_data = pack_double_array(ktb_matrix.variable_data_array[2])
    else:
        raise Exception("Precision has to be either 4 or 8")

    row_ptr_offset = headline_size
    col_idx_offset = row_ptr_offset + (INT_SIZE * len(h_row_ptr_array))
    data_offset = col_idx_offset + (INT_SIZE * len(h_col_idx_array))
    ktb_matrix.variable_offset_array = [
        row_ptr_offset, col_idx_offset, data_offset]
    h_variable_offset_array = pack_int_array(ktb_matrix.variable_offset_array)
    # Rewrite an empty file if file already exists.
    output_file = open(outfile_name, "wb")
    output_file.close()
    output_file = open(outfile_name, "ab+")
    output_file.writelines(h_readme_size)
    output_file.write(h_readme_content)
    output_file.writelines(h_variable_count)
    output_file.writelines(h_variable_type_array)
    output_file.writelines(h_variable_offset_array)
    output_file.writelines(h_variable_count_array)
    output_file.writelines(h_row_ptr_array)
    output_file.writelines(h_col_idx_array)
    output_file.writelines(h_data)
    output_file.close()
