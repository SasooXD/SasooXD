#!/usr/bin/env bash

# settmux.sh: Configures tmux for various environments
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Mon Jul 07 2025 15:59:24 CEST

# This is free and unencumbered software released into the public domain.

NAME=$1
DIR=$2

case "$NAME" in
	code)
		tmux new-session -d -s "$NAME" "nvim $DIR"

		if [ "$(uname -n)" = "MiniBess" ]; then
			tmux split-window -h -t "$NAME" -p 13
		elif [ "$(uname -n)" = "OldBess" ]; then
			tmux split-window -h -t "$NAME" -p 37
		fi

		tmux split-window -v -t "$NAME:0.1"

		tmux send-keys -t "$NAME:0.1" "cd $(dirname "$DIR"); clear" C-m
		tmux send-keys -t "$NAME:0.2" "cd $(dirname "$DIR"); clear" C-m

		tmux select-pane -t "$NAME:0.0"

		tmux attach-session -t "$NAME"
	;;

	sys)
		tmux new-session -d -s "$NAME"

		tmux split-window -h -t "$NAME"

		tmux send-keys -t "$NAME" "cd $DIR; clear" C-m
		tmux send-keys -t "$NAME:0.1" "cd $DIR; clear" C-m

		tmux select-pane -t "$NAME:0.0"

		tmux attach-session -t "$NAME"
	;;

	-k)
		tmux kill-server
	;;
esac
