# .bashrc: personal Bash configuration file.
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Fri Jun 27 2025 16:06:15 CEST

# This is free and unencumbered software released into the public domain.

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

tabs 4

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

set -o vi
alias please="sudo"

export VISUAL=nvim
export EDITOR="$VISUAL"
