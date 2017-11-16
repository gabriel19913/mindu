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
A classe Image está definida aqui.
"""

import pygame
import mindu



class Image(mindu.Sprite):
    """
    Image(file, alpha = True, osd = False, **position) -> Image

    Sprite para representar imagens.

    O argumento "file" é uma string representando o nome do arquivo de imagem a
    ser carregado. Os formatos de arquivo de imagem suportados são: JPEG, PNG,
    GIF, BMP, PCX, TGA, TIF, LBM, PBM e XPM.

    O argumento "alpha" é True ou False, indicando se a imagem possui canal
    alpha (transparência).

    O argumento "osd" é True ou False, indicando se a imagem é On-Screen
    Display.

    Os argumentos de palavra-chave opcionais "**position" servem para posicionar
    a imagem em relação à tela. Os argumentos de palavra-chave válidos são:

        top = int
        left = int
        bottom = int
        right = int
        centerx = int
        centery = int
        topleft = (int, int) ou [int, int]
        bottomleft = (int, int) ou [int, int]
        topright = (int, int)  ou [int, int]
        bottomright = (int, int) ou [int, int]
        midtop = (int, int) ou [int, int]
        midleft = (int, int) ou [int, int]
        midbottom = (int, int) ou [int, int]
        midright = (int, int) ou [int, int]
        center = (int, int) ou [int, int]
    """

    __slots__ = ('_surf', '_rect', '_osd')



    def __init__(self, file, alpha = True, osd = False, **position):

        if not isinstance(file, str):
            raise TypeError('Image(): o argumento "file" precisa ser string')

        try:
            surface = pygame.image.load(file)

        except:
            raise mindu.Error('Image(): impossível carregar o arquivo "{}"'.format(file))

        if not isinstance(alpha, bool):
            raise TypeError('Image(): o argumento "alpha" precisa ser True ou False')

        if not isinstance(osd, bool):
            raise TypeError('Image(): o argumento "osd" precisa ser True ou False')

        if alpha:
            surf = pygame.Surface(surface.get_size(), pygame.SRCALPHA)

        else:
            surf = pygame.Surface(surface.get_size())

        surf.blit(surface, (0, 0))

        self._surf = surf
        self._rect = surf.get_rect()
        self._osd = osd

        for (key, value) in position.items():

            if key not in ('top', 'left', 'bottom', 'right', 'topleft',
                           'bottomleft', 'topright', 'bottomright', 'midtop',
                           'midleft', 'midbottom', 'midright', 'center',
                           'centerx', 'centery'):

                raise KeyError('Image(): argumento de palavra-chave inválido: "{}"'.format(key))

            setattr(self, key, value)



    def copy(self):
        """
        copy() -> Image

        Cria uma cópia da imagem.
        """

        copy = object.__new__(Image)
        copy._surf = self._surf
        copy._rect = self._rect.copy()
        copy._osd = self._osd

        return copy



    def flip(self, hbool, vbool):
        """
        flip(hbool, vbool) -> Image

        Cria uma cópia espelhada da imagem.

        O argumento "hbool" é True ou False, indicando se a cópia deve ser
        espelhada horizontalmente.

        O argumento "vbool" é True ou False, indicando se a cópia deve ser
        espelhada verticalmente.
        """

        if not isinstance(hbool, bool):
            raise TypeError('flip(): o argumento "hbool" precisa ser True ou False')

        if not isinstance(vbool, bool):
            raise TypeError('flip(): o argumento "vbool" precisa ser True ou False')

        copy = object.__new__(Image)
        copy._surf = pygame.transform.flip(self._surf, hbool, vbool)
        copy._rect = copy._surf.get_rect(center = self._rect.center)
        copy._osd = self._osd

        return copy



    def resize(self, size):
        """
        resize(size) -> Image

        Cria uma cópia arbitrariamente redimensionada da imagem.

        O argumento "size" é um par de inteiros representando as dimensões da
        cópia.
        """

        if not isinstance(size, (list, tuple)):
            raise TypeError('resize(): o argumento "size" precisa ser lista ou tupla')

        if len(size) != 2:
            raise ValueError('resize(): o argumento "size" precisa ter comprimento 2')

        (w, h) = size

        if not isinstance(w, int):
            raise TypeError('resize(): o primeiro item do argumento "size" precisa ser inteiro')

        if not isinstance(h, int):
            raise TypeError('resize(): o segundo item do argumento "size" precisa ser inteiro')

        if w <= 0:
            raise ValueError('resize(): o primeiro item do argumento "size" precisa ser maior que 0')

        if h <= 0:
            raise ValueError('resize(): o segundo item do argumento "size" precisa ser maior que 0')

        copy = object.__new__(Image)
        copy._surf = pygame.transform.smoothscale(self._surf, size)
        copy._rect = copy._surf.get_rect(center = self._rect.center)
        copy._osd = self._osd

        return copy



    def rotate(self, angle):
        """
        rotate(angle) -> Image

        Cria uma cópia rotacionada da imagem.

        O argumento "angle" é um float representando quantos graus rotacionar a
        cópia.
        """

        if not isinstance(angle, float):
            raise TypeError('rotate(): o argumento "angle" precisa ser float')

        copy = object.__new__(Image)
        copy._surf = pygame.transform.rotozoom(self._surf, -angle, 1.0)
        copy._rect = copy._surf.get_rect(center = self._rect.center)
        copy._osd = self._osd

        return copy



    def scale(self, scale):
        """
        scale(scale) -> Image

        Cria uma cópia redimensionada da imagem, mantendo a relação de aspecto
        original.

        O argumento "scale" é um float maior que 0.0 para multiplicar o tamanho
        original da imagem.
        """

        if not isinstance(scale, float):
            raise TypeError('scale(): o argumento "scale" precisa ser float')

        if scale <= 0.0:
            raise ValueError('scale(): o argumento "scale" precisa ser maior que 0.0')

        copy = object.__new__(Image)
        copy._surf = pygame.transform.rotozoom(self._surf, 0.0, scale)
        copy._rect = copy._surf.get_rect(center = self._rect.center)
        copy._osd = self._osd

        return copy



