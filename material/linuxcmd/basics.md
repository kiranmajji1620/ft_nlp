### Symlink
- symlink short for symbolic link is a special type of file that acts as a shortcut or pointer to another file or directory
- it doesn't contain the actual data but references the target file or directory.
- when you access the symlink, the system automatically redirects to the original file
- useful for making executables available system-wide without duplicating files.

### Pipx not able to resolve the `poetry --version`
- even though poetry is installed using pipx, it is not symlinked correctly.
- like pipx stores it's envs in `/home/sai-tt0670/.local/share/pipx/venvs/poetry`
- the expected location is `/home/sai-tt0670/.local/pipx/venvs/poetry`
- and path is in `/home/sai-tt0670/.local/bin`
-  ensure pipx configured the path correctly using `pipx ensurepath`

- Scrolling in linux terminal : ctrl + shift + up/down