vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

vim.opt.nu = true
vim.opt.relativenumber = true

vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true

vim.opt.smartindent = true

vim.opt.hlsearch = false
vim.opt.incsearch = true

vim.opt.scrolloff = 8
vim.opt.updatetime = 50
vim.opt.colorcolumn = "80"
vim.opt.cursorline = true

vim.opt.swapfile = false
vim.opt.wrap = false
vim.opt.undofile = true
vim.opt.undodir = os.getenv('HOME') .. '/.local/share/nvim/undodir'
