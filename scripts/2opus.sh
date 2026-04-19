#!/bin/sh

# 2opus.sh: Creates a standardized audio file
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Sun Apr 19 2026 18:08:49 CEST

# This is free and unencumbered software released into the public domain.

OUTPUT="${1%.*}.opus"

[ "$1" -ef "$OUTPUT" ] && OUTPUT="${1%.*}_std.opus"

ffmpeg -i "$1" \
	-c:a libopus \
 	-b:a 128k \
	"$OUTPUT"
