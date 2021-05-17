// Created by Kaustubh Shivdikar
//
// (C) All Rights Reserved

#ifndef KTB_IO_HPP
#define KTB_IO_HPP

#include <string>
#define TYPE_UNDEFINED 0
#define TYPE_INT 1
#define TYPE_LONG 2
#define TYPE_LONG_LONG 3
#define TYPE_FLOAT 4
#define TYPE_DOUBLE 5
#define TYPE_CHAR 6

#define CPU_MALLOC 1
#define GPU_MALLOC 2

// Configurations
#define MAX_PRINT_ELEMENTS 10

// Function and Class Declarations
class ktb;
ktb *ktb_read_mtx(const char *file_name);
void ktb_printer(ktb *ktb_object);
void auto_type_printer(int type_flag, void *data);
void ktb_int_array_printer(int *array, int size);
long long get_data_chunk_size(ktb *ktb_object);
void ktb_check(ktb *matrix_object);
inline int get_min(int a, int b);

using namespace std;

class ktb
{
private:
    /* data */
public:
    inline ktb(/* args */);
    inline ~ktb();
    int readme_size;
    string readme_content;
    int variable_count;
    int *variable_type_array;
    int *variable_offset_array;
    int *variable_element_count_array;
    char *variable_data_array;
    char *error_check_flag;
};

#endif // KTB_IO_HPP
