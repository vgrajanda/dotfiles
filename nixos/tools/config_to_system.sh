#!/bin/sh

echo "-- Configuration file --"
diff /home/doco/.repos/dotfiles/nixos/configuration.nix /etc/nixos/configuration.nix

echo "-- Hardware configuration file --"
diff /home/doco/.repos/dotfiles/nixos/hardware-configuration.nix /etc/nixos/hardware-configuration.nix

sudo cat /home/doco/.repos/dotfiles/nixos/configuration.nix > /etc/nixos/configuration.nix
sudo cat /home/doco/.repos/dotfiles/nixos/hardware-configuration.nix > /etc/nixos/hardware-configuration.nix

