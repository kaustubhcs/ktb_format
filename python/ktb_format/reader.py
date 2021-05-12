from .ktb_class import ktb
from scipy.io import mmread
from pathlib import Path


def mtx2ktb(file_path, precision=8):
    if (precision != 4 and precision != 8):
        raise Exception("Precision has to be either 4 or 8")
    file_object = Path("/path/to/file")
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
        "CSR File\n" + \
        "Matrix Dimensions: " + str(matrix_size) + " x " + str(matrix_size) + "\n" + \
        "Number of non-zeros: " + str(len(data)) + "\n"
    ktb_object.readme_size = len(ktb_object.readme_content)
