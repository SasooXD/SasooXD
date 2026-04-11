vim.cmd("colorscheme vim")

-- ClangFormat formatter
vim.api.nvim_create_autocmd("BufWritePre", {
	pattern = { "*.c", "*.cpp", "*.h", "*.hpp" },
	callback = function()
		vim.cmd("silent! undojoin | %!clang-format")
	end,
})

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
vim.api.nvim_set_hl(0, 'NonText', { fg = '#323232' })

-- Navigate vim panes better
vim.keymap.set('n', '<c-k>', ':wincmd k<CR>')
vim.keymap.set('n', '<c-j>', ':wincmd j<CR>')
vim.keymap.set('n', '<c-h>', ':wincmd h<CR>')
vim.keymap.set('n', '<c-l>', ':wincmd l<CR>')

vim.keymap.set('n', '<leader>h', ':nohlsearch<CR>')

-- Fucking thing to make the stupid wayland clipboard work
-- I wholeheartedly despise clipboard provider
vim.api.nvim_set_option("clipboard", "unnamedplus")
