
import os, glob
import argparse

parser = argparse.ArgumentParser(description='Scan for TODOs and FIXMEs')
parser.add_argument('path', metavar='path', type=str, nargs='+', help='path to scan')

args = parser.parse_args()
path = args.path[0]
print('path:', path)
if path:
    dir_path = os.path.dirname(path)
else:
    dir_path = os.path.dirname(os.path.realpath(__file__))

for filename in glob.glob('*.py'):
    print('filename: ', filename)
    with open(os.path.join(os.getcwd(), filename)) as f:
        for i, line in enumerate(f):
            if any(keyword in line.lower() for keyword in ('todo', 'fixme')):
                print('line: ',i, ' ', line)