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
A classe Keyboard está definida aqui.
"""

import pygame
import mindu



class Keyboard(mindu.Input):
    """
    Objeto para lidar com o teclado.
    """

    __slots__ = ('_symbols', '_busy', '_old_busy', '_time', '_ding', '_dong',
                 '_on_ding', '_on_ding_pargs', '_on_ding_kwargs', '_on_dong',
                 '_on_dong_pargs', '_on_dong_kwargs')



    def __init__(self):
        self._on_ding = None
        self._on_ding_pargs = ()
        self._on_ding_kwargs = {}

        self._on_dong = None
        self._on_dong_pargs = ()
        self._on_dong_kwargs = {}

        self._busy = pygame.key.get_pressed()
        self._old_busy = self._busy

        self._time = [0] * len(self._busy)

        self._ding = []
        self._dong = []

        self._symbols = {}

        for attr in [attr for attr in dir(pygame) if attr.startswith('K_')]:

            value = getattr(pygame, attr)

            if value == pygame.K_UNKNOWN: continue

            attr = attr.replace('K_', '', 1).lower().replace('_', '-')

            self._symbols[attr] = value
            self._symbols[value] = attr



    def _update(self):
        self._old_busy = self._busy
        self._busy = pygame.key.get_pressed()

        mindu.Input._update(self)



