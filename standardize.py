# standardize.py - Small Python script to standardize source code files to my likings.
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Tue Mar 04 2025 00:05:35 CET

#	s	t	a	n	d	a	r	d	i	z	e	.py

import sys
import os
import subprocess

"""Returns the current date in the format 'Tue Jan 30 2024 12:34:56 UTC'"""
def get_current_date():
	result = subprocess.run(["bash", "-c", "LC_TIME=C date +' %a %b %d %Y %T %Z'"],
							capture_output=True, text=True)
	return result.stdout.strip()

"""Makes me remember that LF is the only POSIX approved EOL. (-> destroys everything else)"""
def normalize_line_endings(text):
	return text.replace('\r\n', '\n').replace('\r', '\n')

"""Ensures that the text ends with a single newline."""
def ensure_trailing_newline(text):
	return text if text.endswith('\n') else text + '\n'

"""Adds a formatted header to the file, preserving shebang if present."""
def add_header(filename, description, comment_style, no_date):
	file_basename = os.path.basename(filename)
	date_str = "" if no_date else get_current_date()
	header = ""

	if comment_style == "/*":
		header = f"/*\n * {file_basename} - {description}\n * Matteo Bertolino <m.bertolino.m@gmail.com>\n"
		if not no_date:
			header += f" * {date_str}\n"
		header += " */\n\n"
	else:
		comment_char = "#" if not comment_style else comment_style
		header = f"{comment_char} {file_basename} - {description}\n{comment_char} Matteo Bertolino <m.bertolino.m@gmail.com>\n"
		if not no_date:
			header += f"{comment_char} {date_str}\n"
		header += "\n"

	with open(filename, "r", encoding="utf-8") as f:
		content = f.read()

	content = normalize_line_endings(content)
	lines = content.split('\n')

	if lines and lines[0].startswith("#!"):
		shebang = lines[0] + "\n"
		remaining_content = "\n".join(lines[1:])
		new_content = shebang + "\n" + header + remaining_content
	else:
		new_content = header + content

	new_content = ensure_trailing_newline(new_content)

	with open(filename, "w", encoding="utf-8", newline="\n") as f:
		f.write(new_content)

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: python standardize.py <file> <description> [comment style] [--no-date]")
		sys.exit(1)

	filename = sys.argv[1]
	description = sys.argv[2]
	comment_style = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] != "--no-date" else "#"
	no_date = "--no-date" in sys.argv

	add_header(filename, description, comment_style, no_date)
