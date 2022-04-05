import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Custom keybindings
    Key([mod], "r", lazy.spawn('rofi -show run'), desc="Spawn a command using Rofi launcher"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "o", lazy.next_screen(), desc='Next monitor'),

    # Audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer set Master 10%+')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer set Master 10%-')),

    Key([], "XF86AudioMute", lazy.spawn('amixer set Master toggle')),
    Key([], "XF86AudioNext", lazy.spawn('playerctl next')),
    Key([], "XF86AudioPrev", lazy.spawn('playerctl previous')),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn('light -A 5')),
    Key([], "XF86MonBrightnessDown", lazy.spawn('light -U 5')),
]

groups = [
    Group("a", label=""),
    Group("b", label=""),
    Group("c", label=""),
    Group("d", label=""),
    Group("e", label=""),
    Group("f", label=""),
    Group("g", label=""),
    Group("h", label=""),
    Group("i", label=""),
]

layout_theme = {
        "border_width": 2,
        "margin": 6,
        "border_focus": "d08770",
        "border_normal": "2e3440"
}

layouts = [
    layout.MonadTall(**layout_theme),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(),

    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    margin=3,
                    margin_x=0,
                    padding=6,
                    spacing=0,

                    inactive='4c566a',
                    active='eceff4',
                    highlight_method='text',
                    rounded=False,
                    this_current_screen_border='d08770',
                    urgent_alert_method='text',
                    urgent_border='bf616a',
                    other_current_screen_border='F55C47',
                    other_screen_border='16817A',

                    disable_drag=True,
                    use_mouse_wheel=False
                ),
                widget.Spacer(),     
                widget.Net(
                    interface="wlp2s0"
                ),
                widget.Sep(
                    padding=30,
                    size_percent=30,
                ),
                widget.Systray( 
                    padding=3,
                    icon_size=19
                ),
                widget.Sep(
                    padding=30,
                    size_percent=30,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    padding=7
                ),
            ],
            26,
            opacity=0.94,
            margin=3,
            background='2e3440'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = simple_key_binder("mod4")
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
