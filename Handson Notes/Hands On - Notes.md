Deployment:
Remote access to a server machine - NoMachine, AnyDesk
Secure file transfer from my machine to remote server machine - WinSCP, FileZilla

SUDO

1. sudo apt: APT - Advanced Package Tool. Used for Debian based Linux distributions such as Ubuntu, Linux mint, Kali linux, MX linux.
   - sudo apt update: update all available packages
   - sudo apt install xyz: install xyz software package
2. sudo yum: YUM - Yellowdog Updater, Modifier. Used for Red Hat based Linux distributions such as CentOS, Fedora, RHEL, Oracle linux, Rocky linux, Alma linux.
   - sudo yum update: update all available packages
   - sudo yum install xyz: install xyz software package

File editing:

Nano Commands:

* `nano file.txt`: open a file
* `Ctrl + O`: save file
* `Ctrl + X`: exit nano
* `Ctrl + K`: cut current line
* `Ctrl + U`: paste (uncut) line
* `Ctrl + W`: search text
* `Ctrl + \`: search and replace
* `Ctrl + G`: help
* `Ctrl + A`: move to start of line
* `Ctrl + E`: move to end of line
* `Ctrl + V`: page down
* `Ctrl + Y`: page up
* `Alt + U`: undo
* `Alt + E`: redo
* `Alt + #`: toggle line numbers
* `Alt + A`: mark (select) text

Vim Commands:

* `vim file.txt`: open a file
* `i`: insert mode
* `Esc`: return to normal mode
* `:w`: save file
* `:q`: quit
* `:wq`: save and quit
* `:q!`: quit without saving
* `h j k l`: move cursor
* `0`: start of line
* `$`: end of line
* `gg`: top of file
* `G`: bottom of file
* `x`: delete character
* `dd`: delete line
* `yy`: copy (yank) line
* `p`: paste
* `u`: undo
* `Ctrl + r`: redo
* `/text`: search forward
* `n`: next search result
* `:%s/old/new/g`: replace all
* `v`: visual (select) mode
* `:set number`: show line numbers

---

ngrok:

- Its a tool, a cross platform tunneling application that lets us expose local development server to internet through secure tunnels.
- It creates a secure public URL for a local server. So developers can run a web app on localhost:3000 and instantly get a public URL like https://abcd1234.ngrok.io to share with others.
- Devs use it to share, test and debug applications running on local machines without deploying them to a public server.

---
