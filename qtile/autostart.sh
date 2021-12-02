#!/bin/bash

xrandr --output eDP-1 --mode 1366x768 --pos 1440x66 --rotate normal --output HDMI-1 --off --output DP-1 --primary --mode 1440x900 --pos 0x0 --rotate normal

nm-applet &
nitrogen --restore &
picom &
