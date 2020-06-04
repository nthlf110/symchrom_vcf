import sys
import os
import subprocess
import csv
import optparse

def read_file(path):
    try:
        with open(path,'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            rows = [row for row in reader]
            return rows
    except Exception as e:
        print("Read from: %s, ERROR: %s" %(path, e))


def write_file(path, data):
    try:
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            for row in  data:
                writer.writerow(row)
    except Exception as e:
        print ("Write to: %s, ERROR: %s" %(path, e))



if __name__ == '__main__':
    # read sample list
    parser = optparse.OptionParser()
    parser.add_option('-i', '--ifile', dest='input')
    (options, args) = parser.parse_args()
    sample_list = options.input

    # read .txt
    txt = read_file(sample_list)

    # read .vcf
    orig_vcf = read_file(sample_list[0:-4]+'.vcf')
    if len(orig_vcf) == 0:
    	os._exit()

    # symchromize .vcf
    valid_pos = []
    for i in iter(txt):
    	if i[0][0] != '#':
        	valid_pos.append(i[0]+' '+i[1])
    sym_vcf = []
    sym_vcf.append(orig_vcf[0])
    for i in range(0, len(orig_vcf)):
        if orig_vcf[i][0]+' '+orig_vcf[i][1] in valid_pos:
            sym_vcf.append(orig_vcf[i])

    # output
    write_file(sample_list[0:-4]+'.vcf', sym_vcf)