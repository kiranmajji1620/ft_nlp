### Most used linux commands
- `ls` : list files and directories
- `ls -a` : show hidden files as well (.)
- `pwd` : print current working directory
- `mkdir dirname` : make directory
- `cd` : navigate between directories.
- `cp first.txt second.txt` - copy files from first to second.
- `mv first.txt rename.txt` - rename first to rename.
- `rm` - remove files
- `uname` - os information of system.
- `locate` - locate files in the database.
- `touch` - creates an empty file.
- `ln -s Demo linke` - 
- `cat` - see the contents of a file.
- `clear` - Clear the terminal.
- `man ls` - get the manual for using ls
- `ps` - see current active processes in terminal
- `<any command with output> | grep "hai"` - find specific string in a series of outputs.
- `echo "hello world"` - print something in terminal
- `wget <link>` - download files from the internet, runs in background, doen't interfere.
- `sort`
- `cal january 2023` - show the calender
- `whereis command` - to see the location where command is present
- `df` - get the details of file system.
- `wc`
    - `wc -w` : no of words
    - `wc -l` : no of lines
    - `wc -m` : no of characters    

#### Directories
- `mkdir` : make a directory
    - `mkdir -p /home/demo/sub` : No error if they do not exist, create them.
- `mkdir -m home` : create directory with permissions.
- `rmdir ` : remove directory
- `mvdir` : move or rename directory
- `rm -rf <directrory>` : to delete a non empty directory

#### Find
- find files and directories based on conditions.
- `find /path/to/search -name ".txt"` find all txt files in a directory
- `find /path -mtime -7` find files modified in the last 7 days
- `find /path -size +100M` find files larger that 100Mb


#### Grep
- global search for regular expression. used for searching text in files.
- `grep "endl" main.cpp` - to find the occurences of endl 
- `grep "endl" -i main.cpp` case insensitive search
-  `grep "endl" -r directory` recursive search in all files

#### Read lines
- head : show first 10 lines of a file
- tail : show last 10 lines of a file
- less : view a file page by page
- more : similar to less but less powerful

#### which
- find location of an executable/command
- `which python`
#### System info commands
- `cat /etc/os-release` : find linux distro
- `uname -r` : find linux kernel version
- `lscpu | grep -E "Socket|Core"`
- `free -h` : check ram size
- `top` : monitor currently running processes.
- `ps aux --sort=-%mem | head -10` Sory by RAM
- `ps aux --sort=-%cpu | head -10` sort by CPU
- `lspci | grep -i nvdia` Check if lap has GPU
- `lsblk` or `df -h` Find no of disks and their usage
- `lsusb` find all connected USB devices

#### Sudo vs Super user
- Sudo grants temporary administrative privileges for specific commands
- using sudo, it will run that command with extra priviliges, allow a user with proper permissions to execute as another user.
- sudoers can be seen in etc/sudoers
- super user(root) has unrestricted access to the entire system and should be used carefully.

#### APT
- advanced package tool
- Used for package management in debian based linux distros(ubuntu)
- `sudo apt update` update package lists
- `sudo apt upgrade` upgrade installed packages
- `sudo apt install package-name` install a package
- `sudo apt remove package-name` remove a package