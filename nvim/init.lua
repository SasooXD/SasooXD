-- init.lua: personal Neovim initial configuration file.
-- Matteo Bertolino <m.bertolino.m@gmail.com>
-- Fri Jun 27 2025 17:16:02 CEST

-- This is free and unencumbered software released into the public domain.

vim.opt.number = true

vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = false
vim.opt.autoindent = true
vim.opt.smartindent = true

vim.opt.list = true
vim.opt.listchars = {
	tab = '→ ',
	space = '·',
	trail = '•',
	eol = '↴',
	nbsp = '⎵'
}

vim.opt.cursorline = true
vim.opt.wrap = true
vim.opt.colorcolumn = '100'
vim.opt.signcolumn = 'yes'

vim.opt.updatetime = 300
vim.opt.timeout = true
vim.opt.timeoutlen = 500
