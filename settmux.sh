#!/bin/bash

# settmux.sh: configures tmux for various environments.
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Fri Jun 27 2025 15:58:31 CEST

# This is free and unencumbered software released into the public domain.

NAME=$1
DIR=$2

case "$NAME" in
	code)
		tmux new-session -d -s "$NAME" "nvim"

		tmux split-window -v -t "$NAME" -p 30
		tmux split-window -h -t "$NAME:0.1"

		tmux send-keys -t "$NAME:0.1" "cd $DIR; clear" C-m
		tmux send-keys -t "$NAME:0.2" "cd $DIR; clear" C-m

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
