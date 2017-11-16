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
A classe Mouse está definida aqui.
"""

import os
import pygame
import mindu



class Mouse(mindu.Input):
    """
    Objeto para lidar com o mouse.
    """

    __slots__ = ('_symbols', '_busy', '_old_busy', '_time', '_ding', '_dong',
                 '_on_ding', '_on_ding_pargs', '_on_ding_kwargs', '_on_dong',
                 '_on_dong_pargs', '_on_dong_kwargs', '_position', '_visible',
                 '_cursor', '_idle', '_idle_time', '_idle_timer')



    def __init__(self):
        self._on_ding = None
        self._on_ding_pargs = ()
        self._on_ding_kwargs = {}

        self._on_dong = None
        self._on_dong_pargs = ()
        self._on_dong_kwargs = {}

        self._busy = list(pygame.mouse.get_pressed() + (0, 0, 0, 0, 0, 0))
        self._old_busy = self._busy

        self._time = [0] * len(self._busy)

        self._ding = []
        self._dong = []

        self._symbols = {'button-left':0, 'button-middle':1, 'button-right':2,
                          'scroll-up':3, 'scroll-down':4, 'motion-left':5,
                          'motion-right':6, 'motion-up':7, 'motion-down':8,
                          0:'button-left', 1:'button-middle', 2:'button-right',
                          3:'scroll-up', 4:'scroll-down', 5:'motion-left',
                          6:'motion-right', 7:'motion-up', 8:'motion-down'}

        self._position = pygame.mouse.get_pos()
        self._visible = True
        self._idle = False
        self._idle_time = 500
        self._idle_timer = 0

        self.set_cursor(None)



    def _update(self):
        self._old_busy = self._busy
        self._busy = list(pygame.mouse.get_pressed() + (0, 0, 0, 0, 0, 0))

        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):

            if event.button == 4: self._busy[3] = 1

            elif event.button == 5: self._busy[4] = 1

        position = self._position
        self._position = pygame.mouse.get_pos()

        if position != self._position:

            self._idle = False
            self._idle_timer = 0

            (x1, y1) = position
            (x2, y2) = self._position

            if x2 < x1: self._busy[5] = 1

            elif x2 > x1: self._busy[6] = 1

            if y2 < y1: self._busy[7] = 1

            elif y2 > y1: self._busy[8] = 1

        elif self._idle_timer < self._idle_time:
            self._idle_timer += (1000 // mindu.loop._ips)

            if self._idle_timer >= self._idle_time:
                self._idle = True

        mindu.Input._update(self)



    def get_cursor(self):
        """
        get_cursor() -> Image

        Obtém o cursor do mouse.
        """

        return self._cursor



    def set_cursor(self, cursor):
        """
        set_cursor(cursor) -> None

        Define o cursor do mouse.

        O argumento "cursor" é um objeto Image. Também pode ser None, para que o
        cursor padrão seja utilizado.
        """

        if (cursor is not None) and (not isinstance(cursor, mindu.Image)):
            raise TypeError('set_cursor(): o argumento "cursor" precisa ser um objeto Image ou None')

        if cursor is None:
            cursor = os.path.dirname(os.path.abspath(__file__))
            cursor = os.path.join(cursor, 'cursor.png')
            cursor = mindu.Image(cursor, True)

        self._cursor = cursor



    def get_visible(self):
        """
        get_visible() -> bool

        Verifica se o cursor do mouse está visível.
        """

        return self._visible



    def set_visible(self, visible):
        """
        set_visible(visible) -> None

        Define se o cursor do mouse está visível.

        O argumento "visible" é True ou False.
        """

        if type(visible) is not bool:
            raise TypeError('set_visible(): o argumento "visible" precisa ser True ou False')

        self._visible = visible



    def toggle_visible(self):
        """
        toggle_visible() -> None

        Define alternadamente se o cursor do mouse está visível.
        """

        self._visible = not self._visible



    def get_position(self):
        """
        get_position() -> tuple

        Retorna uma tupla de inteiros (x, y) representando as coordenadas X e Y
        do ponto onde está o cursor do mouse (topo superior esquerdo da imagem
        que representa o cursor do mouse).
        """

        return self._position



    def set_position(self, position):
        """
        set_position(position) -> None

        Define a posição do cursor do mouse (canto superior esquerdo da imagem
        que representa o cursor do mouse).

        O argumento "position" é um par de inteiros representando as coordenadas
        X e Y do ponto onde deve ser posicionado o cursor do mouse.
        """

        if not isinstance(position, (list, tuple)):
            raise TypeError('set_position(): o argumento "position" precisa ser lista ou tupla')

        if len(position) != 2:
            raise ValueError('set_position(): o argumento "position" precisa ter comprimento 2')

        (x, y) = position

        if not isinstance(x, int):
            raise TypeError('set_position(): o primeiro item do argumento "position" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('set_position(): o segundo item do argumento "position" precisa ser inteiro')

        pygame.mouse.set_pos(position)



    def idle(self):
        """
        idle() -> bool

        Verifica se o mouse está ocioso, isto é, se o mouse não se movimenta há
        um determinado tempo. Por padrão o mouse é considerado ocioso se fica
        500 milissegundos sem se mover, mas você pode definir esse tempo com o
        método set_idle_time(), e pode verificá-lo com o método get_idle_time().
        """

        return self._idle



    def get_idle_time(self):
        """
        get_idle_time() -> int

        Verifica a partir de quantos miliossegundos sem se mover o mouse será
        considerado ocioso.
        """

        return self._idle_time



    def set_idle_time(self, time):
        """
        set_idle_time(time) -> None

        Define a partir de quantos miliossegundos sem se mover o mouse será
        considerado ocioso.
        """

        if not isinstance(time, int):
            raise TypeError('set_idle_time(): o argumento "time" precisa ser inteiro')

        if time <= 0:
            raise ValueError('set_idle_time(): o argumento "time" precisa ser maior que 0')

        self._idle_time = time
        self._idle_timer = 0



