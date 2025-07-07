#!/usr/bin/env python3

# headerize-lite.py: Creates a common header for scripts and dotfiles
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Mon Jul 07 2025 15:53:39 CEST

# This is free and unencumbered software released into the public domain.

import sys
import os
import re
from datetime import datetime

AUTHOR = "Matteo Bertolino <m.bertolino.m@gmail.com>"
LICENSE = "This is free and unencumbered software released into the public domain."

def get_date_line(comment):
	now = datetime.now().astimezone()
	return f"{comment} " + now.strftime("%a %b %d %Y %H:%M:%S %Z")

def read_file_lines(path):
	with open(path, "r", encoding="utf-8") as f:
		return f.read().splitlines()

def write_file_lines(path, lines):
	with open(path, "w", encoding="utf-8", newline="\n") as f:
		f.write("\n".join(lines) + "\n")

def has_shebang(lines):
	return lines and lines[0].startswith("#!")

def find_header_start(lines, comment, filename):
	# Prepare regex pattern for the header lines
	prefix = re.escape(comment) + r"\s*"
	filename_line = re.compile(rf"^{prefix}{re.escape(filename)}:.*$")
	author_line   = re.compile(rf"^{prefix}{re.escape(AUTHOR)}$")
	date_line     = re.compile(rf"^{prefix}[A-Z][a-z]{{2}} [A-Z][a-z]{{2}} \d{{2}} \d{{4}} \d{{2}}:\d{{2}}:\d{{2}} [A-Z]+$")
	license_line  = re.compile(rf"^{prefix}{re.escape(LICENSE)}$")

	for i in range(len(lines) - 4):
		if (
			filename_line.match(lines[i]) and
			author_line.match(lines[i + 1]) and
			date_line.match(lines[i + 2]) and
			license_line.match(lines[i + 4])
		):
			return i
	return None

def update_existing_header(lines, start, comment, filename, new_description=None):
	if new_description:
		lines[start] = f"{comment} {filename}: {new_description}"
	lines[start + 2] = get_date_line(comment)
	return lines

def create_new_header(comment, filename, description):
	return [
		f"{comment} {filename}: {description}",
		f"{comment} {AUTHOR}",
		get_date_line(comment),
		"",
		f"{comment} {LICENSE}"
	]

def insert_header(lines, header):
	if has_shebang(lines):
		shebang = lines[0]
		content = lines[1:]
		if content and content[0].strip() == "":
			content = content[1:]
		return [shebang, ""] + header + [""] + content
	else:
		content = lines
		if content and content[0].strip() == "":
			content = content[1:]
		return header + [""] + content

def parse_args():
	args = sys.argv
	if len(args) < 2:
		print(f"Usage: {args[0]} <file> [description] [-c <comment_char>]", file=sys.stderr)
		sys.exit(1)

	filename = args[1]
	description = None
	comment = "#"

	# Handle -c
	if "-c" in args:
		c_index = args.index("-c")
		if c_index + 1 >= len(args):
			print("Error: missing comment character after -c.", file=sys.stderr)
			sys.exit(1)
		comment = args[c_index + 1]
		# Description is optional, and must be right before -c if present
		if c_index == 3:
			description = args[2]
		elif c_index != 2:
			print(f"Usage: {args[0]} <file> [description] [-c <comment_char>].", file=sys.stderr)
			sys.exit(1)
	else:
		if len(args) >= 3:
			description = args[2]

	return filename, description, comment

def main():
	filename, description, comment = parse_args()

	if not os.path.isfile(filename):
		print(f"Error: can't find {filename}.", file=sys.stderr)
		sys.exit(1)

	basename = os.path.basename(filename)
	lines = read_file_lines(filename)
	start = find_header_start(lines, comment, basename)

	if start is not None:
		# Header exists: update date (and description if present)
		lines = update_existing_header(lines, start, comment, basename, description)
	else:
		# Header not found: create only if description is provided
		if description is None:
			print(f"Error: can't update {filename} because no header was found.", file=sys.stderr)
			sys.exit(1)
		header = create_new_header(comment, basename, description)
		lines = insert_header(lines, header)

	write_file_lines(filename, lines)

if __name__ == "__main__":
	main()

