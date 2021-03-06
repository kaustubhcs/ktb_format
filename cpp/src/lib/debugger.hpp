// Created by Kaustubh Shivdikar
//
// (C) All Rights Reserved

#ifndef DEBUGGER_HPP
#define DEBUGGER_HPP

void red_start();
void green_start();
void yellow_start();
void cyan_start();
void underline_start();
void color_reset();

#define red "\e[1;31m"
#define green "\e[1;32m"
#define yellow "\e[1;33m"
#define cyan "\e[1;36m"
#define underline "\e[1;4m"
#define reset_color "\e[0m"

#define KTB_FORMAT_VERBOSE

#ifdef KTB_FORMAT_VERBOSE
#define KTB_FORMAT_PRINT(TEXT) \
    {                          \
        cout << TEXT << endl;  \
    }
#else
#define KTB_FORMAT_PRINT(TEXT) \
    {                          \
    }
#endif //KTB_FORMAT_VERBOSE

#endif // DEBUGGER_HPP
