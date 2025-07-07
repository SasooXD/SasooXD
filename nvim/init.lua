-- init.lua: personal Neovim initial configuration file.
-- Matteo Bertolino <m.bertolino.m@gmail.com>
-- Mon Jul 07 2025 14:19:42 CEST

-- This is free and unencumbered software released into the public domain.

vim.cmd "colorscheme vim"

vim.cmd "map <Up> <Nop>"
vim.cmd "map <Left> <Nop>"
vim.cmd "map <Right> <Nop>"
vim.cmd "map <Down> <Nop>"

vim.opt.relativenumber = true

vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = false
vim.opt.autoindent = true
vim.opt.smartindent = true

vim.opt.list = true

vim.opt.cursorline = true
vim.opt.wrap = true
vim.opt.colorcolumn = '100'
vim.opt.signcolumn = 'yes'

vim.opt.updatetime = 300
vim.opt.timeout = true
vim.opt.timeoutlen = 500
