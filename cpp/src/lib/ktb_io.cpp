#include "functions.hpp"
#include "debugger.hpp"
#include "ktb_io.hpp"
#include <fstream>
#include <sys/stat.h>
#include <cstring>

using namespace std;

ktb *ktb_read_mtx(const char *file_name)
{
    ktb *matrix;
    matrix = (ktb *)malloc(1 * sizeof(ktb));
    struct stat file_meta;
    // The size of the file in bytes
    int file_size;
    if (stat(file_name, &file_meta) == 0)
        file_size = file_meta.st_size;
    else
    {
        throw("FATAL ERROR: File could not be read\n");
        return (nullptr);
    }
    char *ktb_mem;
    ktb_mem = (char *)malloc(file_size * sizeof(char));
    std::ifstream file_object(file_name, ios::in | ios::binary);
    file_object.read(ktb_mem, file_size);
    if (!file_object)
    {
        throw("FATAL ERROR: File could not be read\n");
        return (nullptr);
    }
    matrix->readme_size = ((int *)ktb_mem)[0];
    char *readme_char_array = (char *)malloc(matrix->readme_size * sizeof(char));
    memcpy(readme_char_array, &(ktb_mem[4]), matrix->readme_size);
    matrix->readme_content = readme_char_array;
    // matrix->readme_content = &(ktb_mem[4]); // Will not work if you have a null terminate character in the REAMDE CONTENT string.
    int *ktb_mem_variable_count_ptr = (int *)&(ktb_mem[4 + matrix->readme_size]);
    matrix->variable_count = ktb_mem_variable_count_ptr[0];

    matrix->variable_type_array = ktb_mem_variable_count_ptr + 1;
    matrix->variable_offset_array = matrix->variable_type_array + matrix->variable_count;
    matrix->variable_element_count_array = matrix->variable_offset_array + matrix->variable_count;
    matrix->variable_data_array = (char *)(matrix->variable_element_count_array + matrix->variable_count);
    long long data_chunk_size = get_data_chunk_size(matrix);
    matrix->error_check_flag = matrix->variable_data_array + data_chunk_size;
    ktb_check(matrix);
    return matrix;
}

void ktb_printer(ktb *ktb_object)
{
    cout << cyan << "Readme Size: " << reset << ktb_object->readme_size << endl;
    cout << cyan << "Readme Content: " << reset << ktb_object->readme_content;
    cout << cyan << "Variable Count: " << reset << ktb_object->variable_count << endl;
    cout << cyan << "Variable Type Array: " << reset;
    ktb_int_array_printer(ktb_object->variable_type_array, ktb_object->variable_count);
    cout << endl;
    cout << cyan << "Variable Offset Array: " << reset;
    ktb_int_array_printer(ktb_object->variable_offset_array, ktb_object->variable_count);
    cout << endl;
    cout << cyan << "Variable Count Array: " << reset;
    ktb_int_array_printer(ktb_object->variable_element_count_array, ktb_object->variable_count);
    cout << endl;
    cout << cyan << "Data Array" << reset << endl;
    const int type_size_array[7] = {0, 4, 4, 8, 4, 8, 1};
    for (int i = 0; i < ktb_object->variable_count; i++)
    {
        int print_element_count = get_min(MAX_PRINT_ELEMENTS, ktb_object->variable_element_count_array[i]);
        cout << "Array " << i << ", first " << print_element_count << " elements: ";
        int element_size = type_size_array[ktb_object->variable_type_array[i]];
        for (int j = 0; j < print_element_count; j++)
        {
            auto_type_printer(ktb_object->variable_type_array[i], (void *)(&(ktb_object->variable_data_array[ktb_object->variable_offset_array[i] + (j * element_size)])));
            cout << " ";
        }
        cout << endl;
    }
}

void auto_type_printer(int type_flag, void *data)
{
    switch (type_flag)
    {
    case TYPE_UNDEFINED:
        throw("Found undefined type for variable");
        return;
    case TYPE_INT:
        cout << ((int *)data)[0];
        return;
    case TYPE_LONG:
        cout << ((long *)data)[0];
        return;
    case TYPE_LONG_LONG:
        cout << ((long long *)data)[0];
        return;
    case TYPE_FLOAT:
        cout << ((float *)data)[0];
        return;
    case TYPE_DOUBLE:
        cout << ((double *)data)[0];
        return;
    case TYPE_CHAR:
        cout << ((char *)data)[0];
        return;
    default:
        throw("Found illegal type for variable");
        return;
    }
}

void ktb_int_array_printer(int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << array[i] << " ";
    }
}

long long get_data_chunk_size(ktb *ktb_object)
{
    const int type_size_array[7] = {0, 4, 4, 8, 4, 8, 1};
    long long chunk_size = 0;
    for (int i = 0; i < ktb_object->variable_count; i++)
    {
        chunk_size += (ktb_object->variable_element_count_array[i] * type_size_array[ktb_object->variable_type_array[i]]);
    }
    return (chunk_size);
}

void ktb_check(ktb *ktb_object)
{
    char canary = (ktb_object->error_check_flag)[0];
    if (canary != 'K')
    {
        cout << red << "WARNING: " << reset << "Error check flag (Canary) not found. Memory chunk might be corrupted! ";
        cout << "Found " << yellow << canary << reset << "instead of " << yellow << "K" << reset << endl;
    }
}

inline int get_min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}