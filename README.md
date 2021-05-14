# KTB Format

## Keep That Bit - Binary Format
[![Author](https://img.shields.io/badge/Author-Kaustubh_Shivdikar-purple)](https://scholar.google.com/citations?user=NCTXsGMAAAAJ&hl=en&oi=ao) ![Status](https://img.shields.io/badge/Status-Open_source-green)
![Caution](https://img.shields.io/badge/CAUTION-Work_in_progess-red)
KTB format is a universal format that allows for compartmentalizing binary data. When binary data needs to be stored in a file, the user has to remember the offsets for each "chunk" of data in that binary file. The KTB format allows for easy compartmentalizing of these chunks of data in memory. KTB format does so by adding a small metadata at the begining of the binary file.

KTB format provides:
1. A C++ library allowing you to read, convert and write data from multiple formats to ktb format and vice-versa.
2. This repository also provides a python package called ``ktb_format`` that allows you to read, convert, write data from multiple format to KTB format.

## Features

## Usage
* ``pip install ktb_format`` OR ``conda install -c kaustubhcs ktb_format``. Package details can be found here: [PyPi](https://pypi.org/project/ktb-format/), [Anaconda](https://anaconda.org/kaustubhcs/ktb_format)


| Serial No | Content            | Content                                                              | Element size |
| --------- | ------------------ | -------------------------------------------------------------------- | ------------ |
| 1         | README size        | Size of the README attached to this binary in bytes.                 | 4 bytes      |
| 2         | README             | A human readable table of list of variables in this binary.          | Variable     |
| 3         | Variable Count     | Count of the total variables stored in this format.                  | 4 bytes      |
| 4         | Variable 1: Type   | Type of data [4 Byte or 8 Byte]                                      | 4 bytes      |
| 5         | Variable 1: Offset | The offset of the variable (in Bytes) from the start of this binary. | 4 bytes      |
| 6         | Variable 1: Count  | Total number of elements in this variable                            | 4 bytes      |
| 7         | Variable 2: Type   | Type of data [4 Byte or 8 Byte]                                      | 4 bytes      |
| 8         | Variable 2: Offset | The offset of the variable (in Bytes) from the start of this binary. | 4 bytes      |
| 9         | Variable 2:  Count | Total number of elements in this variable                            |              |
| ...       | ...                |                                                                      |              |
| 10        | Variable 1: Data   | Data of the variable                                                 | Variable     |
| 11        | Variable 2: Data   | Data of the variable                                                 | Variable     |
| 12        | Error Check Flag   | Single byte ASCII character `K` (Capital K)                          |              |

*Warning*: Trying to access 8 byte data (like Double precision float) from a memory address that is not aligned to 8 bytes might create segmentation faults. In this case, enable the `PAD_8_BYTES` flag.

*Note*: You can set the `ERROR_CHECK` flag to check if the data was corrupted while reading. This checks it the last byte of the read binary is the letter `K`.

### Work in Progress
- [ ] Add Python Reader
- [X] Add Python Writer
- [ ] Add C++ Reader
- [ ] Add C++ Writer

### Future Work

- [ ] Instead of letter `K` as error flag, use MD5 hash of the binary to check if data was correctly read.
- [ ] Experiment with 8 bytes access to check for correctness.
