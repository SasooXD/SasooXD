-- init.lua: Personal Neovim initial configuration file
-- Matteo Bertolino <m.bertolino.m@gmail.com>
-- Mon Jul 07 2025 16:28:27 CEST

-- This is free and unencumbered software released into the public domain.

-- Fucking thing to make the stupid wayland clipboard work
-- I wholeheartedly despise clipboard provider
vim.g.clipboard = {
	name = "wl-clipboard",
	copy = {
		["+"] = "wl-copy --foreground --type text/plain",
		["*"] = "wl-copy --foreground --type text/plain",
	},
	paste = {
		["+"] = "wl-paste --no-newline",
		["*"] = "wl-paste --no-newline",
	},
	cache_enabled = true,
}

vim.cmd "colorscheme vim"

vim.cmd "map <Up> <Nop>"
vim.cmd "map <Left> <Nop>"
vim.cmd "map <Right> <Nop>"
vim.cmd "map <Down> <Nop>"

-- At least some line number is on
vim.opt.number = true
vim.opt.relativenumber =true

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

-- Invisible characters
vim.opt.listchars = {
	tab = '→ ',
	space = '·',
	trail = '•',
	eol = '↴'
}

-- Colors for invisible characters
vim.api.nvim_set_hl(0, 'NonText', { fg = '#323232' })         -- Caratteri di fine riga
