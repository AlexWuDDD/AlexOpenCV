import sys
import getopt
import argparse

print("----- Example 1 -----")
# total =len(sys.argv)
# cmdargs = str(sys.argv)
#
# print("The total numbers of args passed to the script: %d" % total)
# print("Args list: %s" % cmdargs)
#
# # print("Script name: %s" % str(sys.argv[0]))
# # print("First argument: %s" % str(sys.argv[1]))
# # print("Second argument: %s" % str(sys.argv[2]))
# for i in range(total):
#     print("Argument # %d : %s" % (i, str(sys.argv[i])))
print("----- Example 2 -----")
# ifile = ''
# ofile = ''
#
# try:
#
#     # Read command line args
#     # python CommandLineArgumentsExamples.py -i input.txt  -o output.txt -x xxxxx aswsw
#     # [('-i', 'input.txt'), ('-o', 'output.txt'), ('-x', 'xxxxx')]
#     # ['aswsw']
#     myopts, args = getopt.getopt(sys.argv[1:], "i:o:x:")
#     print(myopts)
#     print(args)
# except getopt.GetoptError as e:
#     print(str(e))
#     print("Usage: %s -i input -o output" %sys.argv[0])
#     sys.exit(2)
# ###############################
# # o == option
# # a == argument passed to the o
# ###############################
# for o, a in myopts:
#     if o == '-i':
#         ifile = a
#     elif o == '-o':
#         ofile = a
#     else:
#         print("Usage: %s -i input -o output" % sys.argv[0])
#
# print("Input file: %s and output file: %s" % (ifile, ofile))
print("----- Example 3 -----")
parser = argparse.ArgumentParser(description="This is a demo script by alex")
parser.add_argument('-i', '--input', help="Input file name", required=True)
parser.add_argument('-o', '--output', help="Output file name", required=True)
args = parser.parse_args()

print("Input file: %s" % args.input)
print("Output file: %s" % args.output)
