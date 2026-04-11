# .bashrc: Personal Bash configuration file
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Sat Apr 11 2026 19:59:30 CEST

# This is free and unencumbered software released into the public domain.

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='\u@\h:\w \$ '

set -o vi

tabs 4

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias please="sudo"

export VISUAL=nvim
export EDITOR="$VISUAL"
