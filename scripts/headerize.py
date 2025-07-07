#!/usr/bin/env python3

# headerize.py: Creates a common header for source code files
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Mon Jul 07 2025 15:52:25 CEST

# This is free and unencumbered software released into the public domain.

import sys
import os
import re
from datetime import datetime

COPYRIGHT_ASCII = "(c)"
COPYRIGHT_UNICODE = "©"
AUTHOR = "Matteo Bertolino"

def read_file_lines(path):
	with open(path, "r", encoding="utf-8") as f:
		return f.read().splitlines()

def write_file_lines(path, lines):
	with open(path, "w", encoding="utf-8", newline="\n") as f:
		f.write("\n".join(lines) + "\n")

def has_shebang(lines):
	return lines and lines[0].startswith("#!")

def parse_args():
	args = sys.argv[1:]

	if len(args) < 3:
		print("Usage: headerize.py <file> <description> <license> [--ascii|-a]", file=sys.stderr)
		sys.exit(1)

	filename = args[0]
	description = args[1]
	license_name = args[2]
	use_ascii = "--ascii" in args or "-a" in args

	return filename, description, license_name, use_ascii

def format_header(filename, description, license_name, use_ascii):
	copyright_symbol = COPYRIGHT_ASCII if use_ascii else COPYRIGHT_UNICODE
	year = datetime.now().year

	return [
		"/*",
		f"\t{filename}: {description}",
		"",
		f"\tCopyright {copyright_symbol} {year} {AUTHOR}",
		f"\tLicensed under the {license_name} license, see LICENSE for more details.",
		"*/"
	]

def find_existing_header(lines, filename):
	for i in range(len(lines) - 5):
		if (lines[i].strip() == "/*"
			and filename in lines[i + 1]
			and "Copyright" in lines[i + 3]
			and "Licensed under" in lines[i + 4]
			and lines[i + 5].strip() == "*/"):
			return i
	return None

def update_header(lines, start, filename, description, license_name, use_ascii):
	lines[start + 1] = f"\t{filename}: {description}"
	copyright_symbol = COPYRIGHT_ASCII if use_ascii else COPYRIGHT_UNICODE
	year = datetime.now().year
	lines[start + 3] = f"\tCopyright {copyright_symbol} {year} {AUTHOR}"
	lines[start + 4] = f"\tLicensed under the {license_name} license, see LICENSE for more details."
	return lines

def insert_header(lines, header):
	if has_shebang(lines):
		shebang = lines[0]
		rest = lines[1:]
		if rest and rest[0].strip() == "":
			rest = rest[1:]
		return [shebang, ""] + header + [""] + rest
	else:
		if lines and lines[0].strip() == "":
			lines = lines[1:]
		return header + [""] + lines

def main():
	filename, description, license_name, use_ascii = parse_args()

	if not os.path.isfile(filename):
		print(f"Error: file '{filename}' not found.", file=sys.stderr)
		sys.exit(1)

	lines = read_file_lines(filename)
	basename = os.path.basename(filename)
	start = find_existing_header(lines, basename)

	if start is not None:
		lines = update_header(lines, start, basename, description, license_name, use_ascii)
	else:
		header = format_header(basename, description, license_name, use_ascii)
		lines = insert_header(lines, header)

	write_file_lines(filename, lines)

if __name__ == "__main__":
	main()
