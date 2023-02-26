
import os, glob, argparse, re

parser = argparse.ArgumentParser(description='Scan for TODOs and FIXMEs and optionally other keywords.')
parser.add_argument('--path', metavar='path', type=str, help='path to scan if not specified, the current directory is used')
parser.add_argument('--keyword', metavar='keyword', type=str, nargs='+', help='keyword to scan for')

args = parser.parse_args()
path = args.path
keywords = args.keyword or []

if path:
    dir_path = os.path.abspath(path)
else:
    dir_path = os.getcwd()
print('k', keywords)
pattern = '|'.join(['todo', 'fixme'] + keywords)
regex = re.compile(pattern, re.IGNORECASE)
print('Scanning for: ', pattern)
for filename in glob.glob(os.path.join(dir_path,'*.py')):
    print('Filename: ', filename)
    with open(filename) as f:
        for i, line in enumerate(f):
            if regex.search(line):
                print('line: ',i+1, ' ', line)