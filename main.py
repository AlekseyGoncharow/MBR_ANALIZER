import os
import struct
import argparse

fmt_str="8B L L"

out_str='''Состояние: {0}
Начльная позиция CHS (головка): {1}
Начльная позиция CHS (сектор): {2}
Начльная позиция CHS (цилиндр): {3}
Тип(формат) раздела: {4}
Конечная позиция CHS (головка): {5}
Конечная позиция CHS (сектор): {6}
Конечная позиция CHS (цилиндр): {7}
Смещение первого сектора: {8}
Количество байт: {9}
'''
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-infile', type=str, default="D:\Общая папка\mbr2fat16.bin", help='Input dump file')
    args = parser.parse_args()

    print(args)

    if not os.path.exists(args.infile):
        quit()

    file_handler = open(args.infile, "rb")
    data_byte = file_handler.read(512)

    for i in range(4):
        print("Partition {0}".format(i+1))
        data = struct.unpack_from(fmt_str, data_byte, 0x1be+i*16)
        print(out_str.format(hex(data[0]),hex(data[1]),hex(data[2]),hex(data[3]),hex(data[4]),hex(data[5]),hex(data[6]),hex(data[7]),data[8],data[9]))
