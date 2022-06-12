#  _______ __________________ _        _______ 
# (  ___  )\__   __/\__   __/( \      (  ____ \
# | (   ) |   ) (      ) (   | (      | (    \/
# | |   | |   | |      | |   | |      | (__    
# | |   | |   | |      | |   | |      |  __)   
# | | /\| |   | |      | |   | |      | (      
# | (_\ \ |   | |   ___) (___| (____/\| (____/\
# (____\/_)   )_(   \_______/(_______/(_______/
#
# By Raymond:
# https://github.com/slash071/Linux/tree/main/Dotfiles
#
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#################
##   IMPORTS   ##
#################

import os
import subprocess
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

###################
##   VARIABLES   ##
###################

mod = "mod4"
myTerm = "alacritty"
myBrowser = "chromium"

#####################
##   KEYBINDINGS   ##
#####################

keys = [
    
    #---   Switch between windows   ---#
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "c", lazy.layout.next()),

    #---   Move windows   ---#
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    #---   Resize windows   ---#
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    #---   Window Functions   ---#
    Key([mod], "s", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    #---   Reset all window sizes   ---#
    Key([mod], "n", lazy.layout.normalize()),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),

    #---   Terminal   ---#
    Key([mod], "Return", lazy.spawn(myTerm)),
    
    #---   Browser   ---#
    Key([mod], "b", lazy.spawn(myBrowser)),

    #---   Launcher   ---#
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    #---   Reload Qtile   ---#
    Key([mod, "control"], "r", lazy.reload_config()),

    #---   Quit Qtile     ---#
    Key([mod, "control"], "q", lazy.shutdown()),

    #---   Shutdown/Reboot system   ---#
    Key([mod, "control"], "s", lazy.spawn("shutdown -P now")),
    Key([mod, "control"], "BackSpace", lazy.spawn("reboot")),

    #---   Adjust brightness   ---#
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

    #---   Adjust volume   ---#
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    
    #---   Take screenshot   ---#
    Key([], "Print", lazy.spawn("scrot /home/raymond/Pictures/Captures/%Y-%m-%d-$wx$h.png")),
    Key(["control"], "Print", lazy.spawn("scrot -s -b /home/raymond/Pictures/Captures/%Y-%m-%d-$wx$h.png")),

    #---   Change Keyboard layout   ---#
    Key(["mod1"], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard()),
    
    #---   Lock screen   ---#
    Key([mod], "F1", lazy.spawn("betterlockscreen -l"))    
]

####################
##   WORKSPACES   ##
####################

groups = [Group("I", layout='monadtall'),
          Group("II", layout='tile'),
          Group("III", layout='ratiotile'),
          Group("IV", layout='bsp'),
          Group("V", layout='monadwide'),
          Group("VI", layout='floating')]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

################
##   COLORS   ##
################

# I use Tokyonight
# https://github.com/ghifarit53/tokyonight-vim/tree/master/port
colors={
        "black": "#1a1b26",
        "gray": "#4e5173",
        "red": "#F7768E", 
        "green": "#9ECE6A",
        "yellow": "#e5af6a",
        "blue": "#7AA2F7",
        "magenta": "#9a7ecc",
        "cyan": "#9ecbd5",
        "white": "#acb0d0"
}

#################################
##   WINDOW STYLE IN LAYOUTS   ##
#################################

layout_theme = {"border_width": 4,
                "margin": 10,
                "border_focus": colors["cyan"],
                "border_normal": colors["gray"]
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme)
    ## Try more layouts by unleashing below layouts :)
    #layout.Max(),
    # layout.Stack(),
    # layout.Matrix(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy()
]

#############
##   BAR   ##
#############

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=14,
    padding=6
)
extension_defaults = widget_defaults.copy()

def left_arrow(color1, color2):
	return widget.TextBox(
		text = '\uE0B2',
		background = color1,
		foreground = color2,
        fontsize=28,
        padding=-3
	)

def right_arrow(color1, color2):
	return widget.TextBox(
		text = '\uE0B0',
		background = color1,
		foreground = color2,
        fontsize=28,
        padding=-3
	)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding=8,
                    linewidth=0
                ),
                widget.GroupBox(
                    margin_y=6,
                    fontsize=15,
                    highlight_method='line',
                    this_current_screen_border=colors["blue"],
                    highlight_color=[colors["cyan"], "#2E2E2E"],
                    borderwidth=3
                ),
                widget.TextBox(
                    text='',
                    fontsize=16,
                    foreground=colors["yellow"]
                ),
                widget.CurrentLayout(),
                widget.Cmus(
                    fmt='{}',
                    play_color=colors["yellow"]
                ),
                widget.Spacer(),
                widget.TextBox(
                    text='',
                    fontsize=16,
                    foreground=colors["magenta"]
                ),
                widget.Clock(
                    format= '%d %b, %a %I:%M %p',
                    update_interval=60.0
                ),
                widget.Spacer(),
                left_arrow(colors["black"], colors["red"]),
                widget.TextBox(
                    text='',
                    fontsize=16,
                    background=colors["red"],
                    foreground=colors["black"]
                ),
                widget.KeyboardLayout(
                    configured_keyboards=['us','ir'],
                    fmt='{}',
                    background=colors["red"],
                    foreground=colors["black"]
                ),
                left_arrow(colors["red"], colors["blue"]),
                widget.TextBox(
                    text="",
                    fontsize=16,
                    background=colors["blue"],
                    foreground=colors["black"]
                ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch",
                    display_format="{updates}",
                    no_update_string='NO UPDATES',
                    background=colors["blue"],
                    colour_have_updates=colors["black"]
                ),
                left_arrow(colors["blue"], colors["red"]),
                widget.TextBox(
                    text='',
                    fontsize=16,
                    background=colors["red"],
                    foreground=colors["black"]
                ),
                widget.ThermalZone(
                    format='{temp}°C',
                    zone="/sys/class/thermal/thermal_zone0/temp",
                    background=colors["red"],
                    fgcolor_normal=colors["black"]
                ),
                left_arrow(colors["red"], colors["blue"]),
                widget.TextBox(
                    text='溜',
                    fontsize=16,
                    background=colors["blue"],
                    foreground=colors["black"]
                ),
                widget.Memory(
                    format="{MemUsed:.0f}{mm}",
                    interval=1.0,
                    background=colors["blue"],
                    foreground=colors["black"]
                ),
                left_arrow(colors["blue"], colors["red"]),
                widget.TextBox(
                    text='',
                    fontsize=16,
                    background=colors["red"],
                    foreground=colors["black"]
                ),
         		widget.Backlight(
           		    fmt='{}',
 		            brightness_file='/sys/class/backlight/intel_backlight/actual_brightness',
 		            max_brightness_file='/sys/class/backlight/intel_backlight/max_brightness',
        		    background=colors["red"],
                    foreground=colors["black"]
                ),
                left_arrow(colors["red"], colors["blue"]),
                widget.TextBox(
                    text='',
                    fontsize=16,
                    background=colors["blue"],
                    foreground=colors["black"]
                ),
                widget.Volume(
                    fmt='{}',
                    background=colors["blue"],
                    foreground=colors["black"]
                ),        
                left_arrow(colors["blue"], colors["red"]),
                widget.TextBox(
                    text='直',
                    fontsize=16,
                    background=colors["red"],
                    foreground=colors["black"]
                ),
                widget.Wlan(
                    interface='wlo1',
                    format='{essid}',
                    background=colors["red"],
                    foreground=colors["black"]
                ),
                left_arrow(colors["red"],colors["blue"]),
        		widget.Battery(
                    charge_char='',
                    discharge_char='',
                    format='{char} {percent:2.0%}',
                    background=colors["blue"],
                    foreground=colors["black"]
                ),
                widget.Sep(
                    padding=8,
                    linewidth=0,
                    background=colors["blue"]
                )
            ],
            25,
            background=colors["black"],
        ),
    ),
]

###########################
##   FLOATING WINDOWS    ##
###########################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
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
    ],
    border_width=4,
    border_focus=colors["cyan"],
    border_normal=colors["gray"]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

###################
##   AUTOSTART   ##
###################

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
