#!/usr/bin/bash

#---   restore nitrogen   ---#
nitrogen --restore

#---   launch compositor   ---#
picom -f &
