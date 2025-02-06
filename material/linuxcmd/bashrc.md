- bash read command
- Hidden in root, can be viewed by `ls -a`

### Bashrc
- script that is executed when a user logs in.
- contains a series of configurations for the terminal session.
- Can be used to define functions that reduce redundant efforts. 

### Functions
- `cd` - go to root
- `ls -a` - show all files including hidden files
- `vi .bashrc` - Open bashrc in vi editor
- `i` - to enter insert mode
- Add the code
    today()
    {
        This is a 'fajs' return
    }
- `esc` -> `:wq` -> `enter` => Save the changes and exit vim
- reopen the terminal or reload .bashrc `source .bashrc`


### Alias
- `alias aliasname='commands'`

### Backup your bashrc file
- `cp /etc/skel/.bashrc backup` - copies your default bashrc file to backup folder.

### Create and use new bashrc file
- `touch .mybashrc` 
- Add the commands
- Everytime you load the terminal, run source .mybashrc
