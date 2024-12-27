local vim = vim
local Plug = vim.fn['plug#']

vim.call('plug#begin')

    Plug('jiangmiao/auto-pairs')
    Plug('deparr/tairiki.nvim')
    Plug('miikanissi/modus-themes.nvim')
    Plug('NLKNguyen/papercolor-theme')

    Plug('nvim-lua/plenary.nvim')
    Plug('nvim-telescope/telescope.nvim', { ['tag'] = '0.1.8' })

vim.call('plug#end')
