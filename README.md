# Dotfiles

Here I will post my dotfiles and changes I make to them. I'm not a pro about tilling window managers but I'm trying to learn new stuff every day about them and also learn as much as I can about Linux. 

## Favorite fonts

- [HackNerdFont](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/Hack.zip)
- [JetBrainsMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/JetBrainsMono.zip)

## Window manager and tools

- [Spectrwm](https://github.com/conformal/spectrwm)
- [Kitty](https://github.com/kovidgoyal/kitty) (For plug & play)
- [st](https://st.suckless.org/)

## For Debian users

### Essential packages

- dkms
- build-essentials
- linux-headers-$(uname -r)

### Bash script for installing everything you need to rock n roll

```shell

#!/bin/bash

update_system() {
	echo "[*] Updating system..."
	if ! sudo apt update -y > /dev/null 2>&1; then
		echo "Error updating the system"
		return 1
	fi

	if ! sudo apt upgrade -y > /dev/null 2>&1; then
		echo "Error upgrading the system"
		return 1
	fi
	
	echo "[*] System up to date"
}

install_essentials() {
	echo "[*] Installing Debian essentials..."

	if ! sudo apt install -y dkms build-essential linux-headers-$(uname -r) git zip unzip > /dev/null 2>&1; then
		echo "Error installing essentials."
		return 1
	fi

	echo "[*] Essentials installed."
}

update_system
install_essentials

```

Just a little bit fancy but, works and feels good.
