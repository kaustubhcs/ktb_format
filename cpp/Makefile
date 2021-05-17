#!/bin/bash

# Created Kaustubh Shivdikar -- All Rights Reserved


TARGET = ktb.bin
LIB_TARGET = libktb.a
#CC = g++
# CFLAGS=-Wall -O2 -std=c++0x
CC = nvcc
CFLAGS=-O2 -std=c++11 -g
LDFLAGS=
AR = ar
AR_FLAGS = rcs

ROOT_DIR=$(PWD)
CODE_DIR=$(ROOT_DIR)/src/code
HEADER_DIR=$(ROOT_DIR)/src/lib
LIB_DIR=$(ROOT_DIR)/src/lib
OBJ_DIR=$(ROOT_DIR)/src/obj

LIB_OBJ=$(OBJ_DIR)/functions.o $(OBJ_DIR)/debugger.o $(OBJ_DIR)/ktb_io.o
OBJ=$(CODE_DIR)/main.o $(LIB_OBJ)
OBJ_WITH_TARGET=$(OBJ_DIR)/main.o $(LIB_OBJ)



all: clean $(OBJ)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(ROOT_DIR)/$(TARGET) $(OBJ_WITH_TARGET)
#	cp $(BIN_DIR)/$(TARGET) $(ROOT_DIR)

$(OBJ_DIR)/%.o: $(LIB_DIR)/%.cpp
	$(CC) -I$(LIB_DIR) $(CFLAGS) -c $<
	mv $(@F) $(OBJ_DIR)

$(CODE_DIR)/%.o: $(CODE_DIR)/%.cpp
	$(CC) -I$(LIB_DIR) $(CFLAGS) -c $<
	mv $(@F) $(OBJ_DIR)

libktb.a: clean $(OBJ)
	$(AR) $(AR_FLAGS) $(ROOT_DIR)/libs/$(LIB_TARGET) $(LIB_OBJ)

libs: libktb.a

clean:
	printf "\n\e[1;32mCleaning all files\e[0m\n"
	rm -f $(OBJ_DIR)/*.o $(ROOT_DIR)/*.bin
	rm -f $(ROOT_DIR)/libs/$(LIB_TARGET)

run: all
	$(ROOT_DIR)/$(TARGET)

test:
	echo "Test Start"
