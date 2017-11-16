# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 José Falero.
#
# ﻿This file is part of Mindu.
#
# Mindu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mindu is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mindu.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: José Falero <jzfalero.@gmail.com>.
"""
A classe Joystick está definida aqui.
"""

import pygame
import mindu



class Joystick(mindu.Input):
    """
    Objeto para lidar com joysticks.
    """

    __slots__ = ('_symbols', '_joy', '_name', '_numbuttons', '_numhats',
                 '_numaxes', '_busy', '_old_busy', '_time', '_ding', '_dong',
                 '_on_ding', '_on_ding_pargs', '_on_ding_kwargs', '_on_dong',
                 '_on_dong_pargs', '_on_dong_kwargs')



    def __init__(self, id):
        self._on_ding = None
        self._on_ding_pargs = ()
        self._on_ding_kwargs = {}

        self._on_dong = None
        self._on_dong_pargs = ()
        self._on_dong_kwargs = {}

        self._joy = pygame.joystick.Joystick(id)
        self._joy.init()

        # Alguns nomes de joystick possuem caracteres em branco bizarros.
        name = self._joy.get_name().split()
        self._name = ''
        for word in name: self._name += (word + ' ')
        self._name = self._name[:-1]

        self._numbuttons = self._joy.get_numbuttons()
        self._numhats = self._joy.get_numhats()
        self._numaxes = self._joy.get_numaxes()

        self._symbols = {}

        for b in range(self._numbuttons):
            symbol = 'button-{}'.format(b)
            self._symbols[b] = symbol

        for h in range(self._numhats):
            symbol = 'hat-{}-left'.format(h)
            i = len(self._symbols)
            self._symbols[i] = symbol

            symbol = 'hat-{}-right'.format(h)
            i = len(self._symbols)
            self._symbols[i] = symbol

            symbol = 'hat-{}-up'.format(h)
            i = len(self._symbols)
            self._symbols[i] = symbol

            symbol = 'hat-{}-down'.format(h)
            i = len(self._symbols)
            self._symbols[i] = symbol

        for a in range(self._numaxes):
            symbol = 'axis-{}-minus'.format(a)
            i = len(self._symbols)
            self._symbols[i] = symbol

            symbol = 'axis-{}-plus'.format(a)
            i = len(self._symbols)
            self._symbols[i] = symbol

        for (key, value) in list(self._symbols.items()):
            self._symbols[value] = key

        buttons = [self._joy.get_button(b) for b in range(self._numbuttons)]

        hats = []
        for h in range(self._numhats):
            (hx, hy) = self._joy.get_hat(h)
            hats += [hx < 0, hx > 0, hy > 0, hy < 0]

        axes = []
        for a in range(self._numaxes):
            a = self._joy.get_axis(a)
            axes += [a < 0, a > 0]

        self._busy = buttons + hats + axes
        self._old_busy = self._busy
        self._time = [0] * len(self._busy)
        self._ding = []
        self._dong = []



    def _update(self):
        self._old_busy = self._busy

        buttons = [self._joy.get_button(b) for b in range(self._numbuttons)]

        hats = []
        for h in range(self._numhats):
            hx, hy = self._joy.get_hat(h)
            hats += [hx < 0, hx > 0, hy > 0, hy < 0]

        axes = []
        for a in range(self._numaxes):
            a = self._joy.get_axis(a)
            axes += [a < 0, a > 0]

        self._busy = buttons + hats + axes

        mindu.Input._update(self)



    def get_name(self):
        """
        get_name() -> str

        Obtém o nome do joystick.
        """

        return self._name



