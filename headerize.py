#!/usr/bin/env python3

# headerize.py: creates a common header for scripts and dotfiles.
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Fri Jun 27 2025 15:56:42 CEST

# This is free and unencumbered software released into the public domain.

import sys
import os
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

def header_starts_at(lines, comment, filename, index):
	try:
		return(
			lines[index].startswith(f"{comment} {filename}:") and
			lines[index + 1].strip() == f"{comment} {AUTHOR}" and
			lines[index + 2].strip().startswith(f"{comment} ") and
			lines[index + 4].strip() == f"{comment} {LICENSE}"
		)
	except IndexError:
		return False

def find_header_start(lines, comment, filename):
	for i, line in enumerate(lines):
		if line.strip() == f"{comment} {AUTHOR}":
			start = i - 1
			if start >= 0 and header_starts_at(lines, comment, filename, start):
				return start
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
	if len(sys.argv) not in [2, 3, 5]:
		print(f"Usage: {sys.argv[0]} <file> [description] [-c <comment_char>].", file=sys.stderr)
		sys.exit(1)

	filename = sys.argv[1]
	description = None
	comment = "#"

	if len(sys.argv) == 3 and sys.argv[2] != "-c":
		description = sys.argv[2]
	elif len(sys.argv) == 5 and sys.argv[3] == "-c":
		description = sys.argv[2]
		comment = sys.argv[4]
	elif len(sys.argv) == 3 and sys.argv[2] == "-c":
		print("Error: missing comment type.", file=sys.stderr)
		sys.exit(1)

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
		lines = update_existing_header(lines, start, comment, basename, description)
	else:
		if description is None:
			print(f"Error: can't update {filename} because no header was found.", file=sys.stderr)
			sys.exit(1)
		header = create_new_header(comment, basename, description)
		lines = insert_header(lines, header)

	write_file_lines(filename, lines)

if __name__ == "__main__":
	main()
