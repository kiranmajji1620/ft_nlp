### Environment variables
- Key value pairs that define system wide settings and configurations.
- Allow you to change system settings and program behaviour without modifying the actual code.


- When we open a new terminal window or tab, a new shell session is created. 
- It's scope includes
    - The shell process
    - All child process(programs or scripts launched from that terminal)
    - Environment variables
    - Working directory.
- Once the terminal is closed, the scope ends. meaning all processes env variables and temporary configurations are lost unless explicitly saved in configuration files.


#### Scope of an environment variable
- Dictates where the variable can be accessed or defined
- Global
    - `export MY_VAR="HELLO"`
    - `echo $MY_VAR`
    - Accessible from anywhere within that terminal's environment
    - Can be employed by scripts, programs, processes running within the scope of that terminal.
- Local
    - `MY_VAR='HELLO'`
    - confined to specific terminal 
    - isolated from external programs or processes, making their reach exclusive to the terminal that birthed them.
    - Cannot be employed by child processes.

### Persistence
- To persist global variable for user wide programs, even after session closes, save them to .bashrc file.
- To persist them for system wide, store them in /etc/environment

#### Commands
- `echo $variable_name` display variable value
- `printenv` list of all global env variables
- `set` list of all global and local
- `unset A` or `A = ''` to unset or delete 

### .env file
- simple text file used to store environment variables
- Commonly used indevelopment to keep configurations separate from code.
- Must put it in .gitignore for version control.

### Uses
- Configure management : store the credentials in environment variables 
- System wide settings : control system behaviour using variables like path
- Security : data can be stored instead of being hardcoded in scripts

#### Different ways to create environment variables
- `export MYVAR='Hai'` global variable
- `MYVAR='Hello'` shell variable
- `MYVAR='Hello' command_name` Inline, doesn't persist
Permanent methods
- `echo 'export MYVAR='Hello'' >> .bashrc` for userwide
- `echo 'export MYVAR='Hello'' >> etc/environment` for system wide
- Create a .env file and load it.
- Write a script and run it.

#### Shell variables vs environment variables
- shell variables are the local environment variables which cannot be accessed by the child processes.
