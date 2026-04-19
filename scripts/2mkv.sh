#!/bin/sh

# 2mkv.sh: Creates a standardized video file
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Sun Apr 19 2026 18:08:32 CEST

# This is free and unencumbered software released into the public domain.

OUTPUT="${1%.*}.mkv"

[ "$1" -ef "$OUTPUT" ] && OUTPUT="${1%.*}_std.mkv"

ffmpeg -i "$1" \
	-c:v libsvtav1 \
	-crf 30 \
	-preset 6 \
	-pix_fmt yuv420p10le \
	-svtav1-params keyint=10s:tune=0:enable-overlays=1:scd=1:scm=0 \
	-c:a libopus -b:a 128k \
	-c:s copy \
	"$OUTPUT"
