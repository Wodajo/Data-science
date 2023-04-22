
`interactive` - `sdin` and `sdout` connected to `terminal emulator`
`non-interactive` - doesn't accept user input. e.g. command launched from script
`login` - used for logging into
`non-login`

system-wide zsh startup files are the following:
-   `/etc/zshenv` - set ENVs, **always** invoked when zsh session is started
-   `/etc/zprofile` - read when `login shell` session is started (if `interactive` - before `zshrc`)
-   `/etc/zlogin` - read when `login shell` session is started (if `interactive` - after `zshrc`)
-   `/etc/zshrc` - read when `interactive shell` is started
-   `/etc/zlogout` - read when `login shell` is closed

user-level conf. files: 
-   `.zshenv` - e.g. `$ZDOTDIR`, `$PATH`, `$EDITOR`
-   `.zprofile` 
-   `.zlogin` 
-   `.zshrc`  - everything interactive e.g. prompt, command completion, correction, suggestion, highlighting, output coloring, alioases, key bindings, history managment
-   `.zlogout` 
path to it's dir is set as a value of `ZDOTDIR`
if `ZDOTDIR` is an empty string files assumed to be in `HOME` dir

Order examples:
for `interactive, no-login` shell:
`/etc/zshenv` -> `~/.zshenv` -> `/etc/zshrc` -> `~/.zshrc`

for `interactive, login` shell:
`/etc/zshenv` -> `~/.zshenv` -> `/etc/zprofile` -> `~/.zprofile` -> `/etc/zshrc` -> `~/.zshrc` -> `/etc/zlogin` -> `~/.zlogin` -> `/etc/zlogout` -> `~/.zlogout`

for `non-interactive, non-login` shell:
`/etc/zshenv` -> `~/.zshenv`


to export a dir to PATH:
append `path=("$HOME/.local/bin" $path)` to `~/.zshenv`
at each `.zshenv` invocation `$HOME/.local/bin` would be added to the array. To solve this problem use `typeset -U path` before array declaration. This keeps the leftmost element of array if there are duplicates.

e.g.
 `echo $path`
```
/home/egdoc/.local/bin /home/egdoc/bin /usr/local/bin
```
if we append `/usr/local/bin` at the begginig of the array the old one is removed:
`typeset -U path`
`path=(/usr/local/bin $path)
`echo $path`
```
/usr/local/bin /home/egdoc/.local/bin /home/egdoc/bin
```

`chsh -s $(which zsh)` 
`.zshenv` must be in `$HOME`. Export ENVs:
```
export XDG_CONFIG_HOME="$HOME/.config"`
export XDG_DATA_HOME=""$XDG_CONFIG_HOME/.local/share
export XDG_CACHE_HOME="$XDG_CONFIG_HOME/cache"
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"
```
Create according directories. Populate `$ZDOTDIR/.zshrc` with history variables, sources to tab completion, sytax highlighting, autosuggestions and prompt.


[dotfiles](index.md)
[one of the main sources](https://thevaluable.dev/zsh-install-configure-mouseless/)
[prompt creation instructions](https://voracious.dev/blog/a-guide-to-customizing-the-zsh-shell-prompt)
[prompt creation v.2](https://scriptingosx.com/2019/07/moving-to-zsh-06-customizing-the-zsh-prompt/)
[zsh promp documentation](https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html)