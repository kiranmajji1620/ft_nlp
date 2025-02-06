#### Tmux
- Terminal multiplexer
- `sudo apt install tmux` install tmux

- Multiple sessions: Run multiple programs in single window
- Session persistence: Detach from a session and leave it running in the background and then reattach later, even after disconnecting from SSH
- Panes splitting : Split the terminal into multiple windows and panes, making multi tasking easier.
- Remote work : Useful for long running processes, especially in remote servers where disconnections might occur.

Sessoin : collection of windows and panes that are associated with each other. We can have multiple sessions running simultaneously
Window : A full screen terminal within a session
Pane : Division of a window into multiple sections
Prefix key : default control key to send commands to tmux.

#### Split panes
- `ctrl + B + %` vertical split
- `ctrl + B + "` horizontal split
- `ctrl + B` arrow keys to navigate between panes

#### Create and switch windows
- `ctrl + B + C` create a new window
- `ctrl + B + 2` switch between windows
- `ctrl + B + N` next window
- `ctrl + B + P` previous window

#### Managing sessions and windows
- `tmux` start a new tmux session
- `tmux new-session -s mysession` start a session with a name
- `ctrl + B + D` detach from the session
- `tmux attach-session -t mysession` or `-a -t 0` reattach to an existing session
- `tmux ls` list all session
- `ctrl + B + ,` rename the current window
- `tmux rename-session -t oldname newname`
- `ctrl + B + &` close a window
- `ctrl + D` or `exit` close a pane
- `tmux kill-session -t mysession` kill a session
