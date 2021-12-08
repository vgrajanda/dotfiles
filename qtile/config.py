from typing import List  # noqa: F401

import os, subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run"),
        desc="Rofi application launcher"),

    ##################
    # Custom keybinds#
    ##################

    Key([mod], "b", lazy.spawn("firefox"),
        desc="Web Browser"),
    Key([mod], "e", lazy.spawn("thunar"),
        desc="File Manager"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Fullscreen mode"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(),
        desc="Floating window mode"),
    Key([mod], "t", lazy.spawn("telegram-desktop"),
        desc="Telegram"),
    Key([mod], "m", lazy.spawn("spotify"),
        desc="Spotify"),
    Key([mod], "c", lazy.spawn("alacritty -e nvim /home/donja/.config/qtile/config.py"),
        desc="Spotify"),

    # Window keybinds

    Key([mod, "control"], "h", lazy.to_screen(0)),
    Key([mod, "control"], "l", lazy.to_screen(1)),

    # Basic control keys
    
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),

    # Audio control

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 10%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 10%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
]

# Credits: DT
# Setting group names

def init_group_names():
    return [("WWW", {'layout': 'monadtall'}),
            ("DEV", {'layout': 'monadtall'}),
            ("SYS", {'layout': 'monadtall'}),
            ("TERM", {'layout': 'monadtall'}),
            ("DOCS", {'layout': 'monadtall'}),
            ("VBOX", {'layout': 'monadtall'}),
            ("CHAT", {'layout': 'monadtall'}),
            ("DIS", {'layout': 'monadtall'}),
            ("MUS", {'layout': 'monadtall'})]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# Default config, just in case

"""
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
])
"""

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "FC85AE",
                "border_normal": "252525"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack Nerd Font',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    margin=3,
                    margin_x=0,
                    padding=7,
                    spacing=0,

                    inactive='3A4750',
                    highlight_method='block',
                    rounded=False,
                    this_current_screen_border='574B90',
                    block_highlight_text_color='ffffff',
                    urgent_alert_method='block',
                    urgent_border='C37B89',
                    other_current_screen_border='9E579D',
                    other_screen_border='9E579D',

                    disable_drag=True,
                    use_mouse_wheel=False
                ),
                widget.Spacer(),
                widget.Net(
                    interface="wlp2s0"
                ),
                widget.Sep(
                    padding=30,
                    size_percent=100,
                ),
                widget.Systray( 
                    padding=7,
                    icon_size=19
                ),
                widget.Sep(
                    padding=30,
                    size_percent=100,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    padding=7
                ),
            ],
            26,
            opacity=0.8,
            margin=5,
            background='191A19'
        ),
    ),

    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    margin=3,
                    margin_x=0,
                    padding=7,
                    spacing=0,

                    inactive='3A4750',
                    highlight_method='block',
                    rounded=False,
                    this_current_screen_border='574B90',
                    block_highlight_text_color='ffffff',
                    urgent_alert_method='block',
                    urgent_border='C37B89',
                    other_current_screen_border='9E579D',
                    other_screen_border='9E579D',

                    disable_drag=True,
                    use_mouse_wheel=False
                ),
                widget.Spacer(),

                #widget.Net(
                #    interface="wlp2s0"
                #),

                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    padding=7
                ),
            ],
            28,
            opacity=0.8,
            margin=5,
            background='191A19'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
