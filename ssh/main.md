## SSH
- To connect to a remote machine using ssh,
`ssh username@machine` and then give password.


## To connect to a remote machine using a proxy:
- login to machine1 first and then to machine2
- or change the config file as follows. 
```
# This configuration managed by 0Helper. Do not edit manualy
# ProxyCommand /usr/bin/nc -X connect -x 127.0.0.1:3128 %h %p

Host <machine1>
  HostName <host name 1>
  User <user name 1>

Host <machine2>
  HostName <host name 2>
  User <user name 2>
  ProxyJump <machine1>
```