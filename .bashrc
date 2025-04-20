# .bashrc - Personal Bash configuration file.
# Matteo Bertolino <m.bertolino.m@gmail.com>
# Sun Apr 06 2025 18:04:05 CEST

#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

set -o vi

alias please="sudo"

export PATH="$PATH:/usr/local/bin/android_sdk/platform-tools:/usr/local/bin/android_sdk/build-tools/34.0.0"
export ANDROID_SDK_ROOT="/usr/local/bin/android_sdk"
export ANDROID_HOME="/usr/local/bin/android_sdk"
