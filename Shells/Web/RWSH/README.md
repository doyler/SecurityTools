# RWSH - Ray's Web SHell
A PHP web shell and its Python based client

# Features
* Encoded communication
* Pseudo-interactive shell

![Execution](http://www.doyler.net/wp-content/uploads/rwsh/rwsh-1-execution.png)
* Cleaner output formatting than PHP passthru
* Hostname and username (whoami) detection
* (Mostly) Clean exiting
* Ability to still interact with via a browser
* Obfuscated server (this is possible with most/all web shells, I just provide one with it)

![Browser](http://www.doyler.net/wp-content/uploads/rwsh/rwsh-2-browser.png)

# TODO
* Add ability to easily obsfucate shell.php
* Include randomly generated filenames for server.php (similar to Metasploit payloads)
* Look into better methods of encryption or encoding for the traffic
* Handle all exit cases better
* Perform OS detection and better prompt displays
* Look into the ability to change directories (change the prompt, prepend the current directory to any requests?)
