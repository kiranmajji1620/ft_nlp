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


## To automate the process of typing password again and again
- we can login to the remote machine in two ways : using password or using public and private keys
- generate a public key and send that public key to the remote machine 
- generate key using `ssh-key-gen`. give the passphrase.
- Now, say `ssh-copy-id username@hostname`. give the previously given passphrase.
- this will copy the public id to the remote machine: .ssh/authorized_keys.

```
Host <machine1>
  HostName <host name 1>
  User <user name 1>

Host <machine2>
  HostName <host name 2>
  User <user name 2>
  ProxyJump <machine1>
  ForwardAgent yes # No need to give this if we already push the proxy key to the remote machine.
```

## Automating connecting to proxy machine
- Using the below commands, we can directly login to the remote machine without password.
- We are copying the local machine public key to the remote machine via proxy.
- Even though we tunnel through the proxy machine, the ssh client will be local machine only. so the local machine public key is to be pasted in remote machine.
- we are reading the local machine public key and then appending it in to the remote machine.
```
ssh -J proxy_user@proxy_host remoteuser@remotehost "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
cat ~/.ssh/localkey.pub | ssh -J proxy_user@proxy_host remoteuser@remotehost "cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```