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
A classe Animation está definida aqui.
"""

import os
import pygame
import mindu



class Animation(mindu.Sprite):
    """
    Animation( directory,
               alpha = True,
               redraw = 1,
               anchor = "midbottom",
               repeat = True,
               running = True,
               osd = True,
               **position ) -> Animation

    Sprite para representar animações.

    O argumento "directory" é uma string representando o nome do diretório que
    contém os arquivos de imagem a serem carregados como quadros da animação. Os
    formatos de arquivo de imagem suportados são: JPEG, PNG, GIF, BMP, PCX, TGA,
    TIF, LBM, PBM e XPM.

    O argumento "alpha" é True ou False, indicando se a animação possui canal
    alpha (transparência).

    O argumento "redraw" é um inteiro maior que 0, indicando quantas vezes cada
    quadro deve ser desenhado antes de ser substituído pelo próximo.

    O argumento "anchor" é uma string, representando a âncora da animação. As
    âncoras válidas são: "top", "left", "bottom", "right", "centerx", "centery",
    "topleft", "bottomleft", "topright", "bottomright", "midtop", "midleft",
    "midbottom", "midright", "center".

    O argumento "repeat" é True ou False, indicando se a animação deve se
    repetir automaticamente quando chega ao fim.

    O argumento "running" é True ou False, indicando se a animação está rodando.

    O argumento "osd" é True ou False, indicando se a animação é On-Screen
    Display.

    Os argumentos de palavra-chave opcionais "**position" servem para posicionar
    a animação em relação à tela. Os argumentos de palavra-chave válidos são:

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

    __slots__ = ('_surfs', '_surf', '_rects', '_rect', '_redraw_count',
                 '_redraw', '_anchor', '_repeat', '_index', '_limit',
                 '_running', '_osd')



    def __init__( self,
                  directory,
                  alpha = True,
                  redraw = 1,
                  anchor = "midbottom",
                  repeat = True,
                  running = True,
                  osd = False,
                  **position  ):

        if not isinstance(alpha, bool):
            raise TypeError('Animation(): o argumento "alpha" precisa ser True ou False')

        if not isinstance(directory, str):
            raise TypeError('Animation(): o argumento "directory" precisa ser string')

        if not os.path.exists(directory):
            raise mindu.Error('Animation(): o diretório "{}" não existe'.format(directory))

        if not os.path.isdir(directory):
            raise mindu.Error('Animation(): "{}" não é um diretório'.format(directory))

        files = [os.path.join(directory, file) for file in os.listdir(directory)]

        if not files:
            raise mindu.Error('Animation(): o diretório "{}" está vazio'.format(directory))

        files.sort()

        self._surfs = []

        for file in files:

            try: surface = pygame.image.load(file)

            except:
                raise mindu.Error('Animation(): impossível carregar o arquivo "{}"'.format(file))

            if alpha:
                surf = pygame.Surface(surface.get_size(), pygame.SRCALPHA)

            else:
                surf = pygame.Surface(surface.get_size())

            surf.blit(surface, (0, 0))
            self._surfs.append(surf)

        if not isinstance(redraw, int):
            raise TypeError('Animation(): o argumento "redraw" precisa ser inteiro')

        if redraw <= 0:
            raise ValueError('Animation(): o argumento "redraw" precisa ser maior que 0')

        if not isinstance(anchor, str):
            raise TypeError('Animation(): o argumento "anchor" precisa ser string')

        if anchor not in ('top', 'left', 'bottom', 'right', 'centerx',
                          'centery', 'topleft', 'bottomleft', 'topright',
                          'bottomright', 'midtop', 'midleft', 'midbottom',
                          'midright', 'center'):

            raise ValueError('Animation(): valor inválido para o argumento "anchor": "{}"'.format(anchor))

        if not isinstance(repeat, bool):
            raise TypeError('Animation(): o argumento "repeat" precisa ser True ou False')

        if not isinstance(running, bool):
            raise TypeError('Animation(): o argumento "running" precisa ser True ou False')

        if not isinstance(osd, bool):
            raise TypeError('Animation(): o argumento "osd" precisa ser True ou False')

        self._rects = [surf.get_rect() for surf in self._surfs]
        self._redraw = redraw
        self._anchor = anchor
        self._repeat = repeat
        self._running = running
        self._osd = osd

        self._redraw_count = 0
        self._index = 0
        self._limit = len(self._surfs)

        self._surf = self._surfs[self._index]
        self._rect = self._rects[self._index]

        for (key, value) in position.items():

            if key not in ('top', 'left', 'bottom', 'right', 'topleft',
                           'bottomleft', 'topright', 'bottomright', 'midtop',
                           'midleft', 'midbottom', 'midright', 'center',
                           'centerx', 'centery'):

                raise KeyError('Animation(): argumento de palavra-chave inválido: "{}"'.format(key))

            setattr(self, key, value)



    def _update(self):
        if not self._running: return

        self._redraw_count += 1

        if self._redraw_count == self._redraw:
            self._redraw_count = 0
            self._index += 1

            if self._index == self._limit:

                if not self._repeat:
                    self._index -= 1
                    self._running = False

                    return

                else:
                    self._index = 0

            self._surf = self._surfs[self._index]

            anchor_value = getattr(self._rect, self._anchor)
            self._rect = self._rects[self._index]
            setattr(self._rect, self._anchor, anchor_value)



    def play(self):
        """
        play() -> None

        Roda a animação a partir do começo.
        """

        self._running = True
        self._index = 0
        self._redraw_count = 0

        self._surf = self._surfs[self._index]

        anchor = getattr(self._rect, self._anchor)
        self._rect = self._rects[self._index]
        setattr(self._rect, self._anchor, anchor)



    def pause(self):
        """
        pause() -> None

        Pausa a animação.
        """

        self._running = False



    def unpause(self):
        """
        unpause() -> None

        Roda a animação a partir do ponto onde foi pausada.
        """

        self._running = True



    def get_redraw(self):
        """
        get_redraw() -> int

        Retorna um inteiro representando quantas vezes cada quadro é desehado
        antes de ser substituído pelo próximo.
        """

        return self._redraw



    def set_redraw(self, redraw):
        """
        set_redraw(redraw) -> None

        Define quantas vezes cada quadro é desehado antes de ser substituído
        pelo próximo.

        O argumento "redraw" é um inteiro maior que 0.
        """

        if not isinstance(redraw, int):
            raise TypeError('set_redraw(): o argumento "redraw" precisa ser inteiro')

        if redraw <= 0:
            raise ValueError('set_redraw(): o argumento "redraw" precisa ser maior que 0')

        self._redraw = redraw
        self._redraw_count = 0



    def get_repeat(self):
        """
        get_repeat() -> bool

        Verifica se a animação se repete quando chega ao fim.
        """

        return self._repeat



    def set_repeat(self, repeat):
        """
        set_repeat(repeat) -> None

        Define se a animação se repete quando chega ao fim.

        O argumento "repeat" é True ou False.
        """

        if not isinstance(repeat, bool):
            raise TypeError('set_repeat(): o argumento "repeat" precisa ser True ou False')

        self._repeat = repeat



    def toggle_repeat(self):
        """
        toggle_repeat() -> None

        Define alternadamente se a animação se repete quando chega ao fim.
        """

        self._repeat = not self._repeat



    def get_anchor(self):
        """
        get_anchor() -> str

        Retorna uma string representando a âncora da animação.
        """

        return self._anchor



    def set_anchor(self, anchor):
        """
        set_anchor(anchor) -> None

        Define a âncora da animação.

        O argumento "anchor" é uma das seguintes strings: "top", "left",
        "bottom", "right", "topleft", "bottomleft", "topright", "bottomright",
        "midtop", "midleft", "midbottom", "midright", "center", "centerx" ou
        "centery".
        """

        if not isinstance(anchor, str):
            raise TypeError('set_anchor(): o argumento "anchor" precisa ser string')

        if anchor not in ('top', 'left', 'bottom', 'right', 'topleft',
                          'bottomleft', 'topright', 'bottomright', 'midtop',
                          'midleft', 'midbottom', 'midright', 'center',
                          'centerx', 'centery'):

            raise ValueError('set_anchor(): âncora inválida: "{}"'.format(anchor))

        self._anchor = anchor



    def running(self):
        """
        running() -> bool

        Verifica se a animação está rodando.
        """

        return self._running



    def copy(self):
        """
        copy() -> Animation

        Cria uma cópia da animação.
        """

        copy = object.__new__(Animation)

        copy._redraw_count = self._redraw_count
        copy._redraw = self._redraw
        copy._anchor = self._anchor
        copy._repeat = self._repeat
        copy._index = self._index
        copy._limit = self._limit
        copy._running = self._running
        copy._surfs = self._surfs
        copy._rects = [rect.copy() for rect in self._rects]
        copy._surf = copy._surfs[copy._index]
        copy._rect = copy._rects[copy._index]
        copy._osd = self._osd

        return copy



    def flip(self, hbool, vbool):
        """
        flip(hbool, vbool) -> Animation

        Cria uma cópia espelhada da animação.

        O argumento "hbool" é True ou False, indicando se a animação deve ser
        espelhada horizontalmente.

        O argumento "vbool" é True ou False, indicando se a animação deve ser
        espelhada verticalmente.
        """

        if not isinstance(hbool, bool):
            raise TypeError('flip(): o argumento "hbool" precisa ser True ou False')

        if not isinstance(vbool, bool):
            raise TypeError('flip(): o argumento "vbool" precisa ser True ou False')

        copy = object.__new__(Animation)

        copy._redraw_count = self._redraw_count
        copy._redraw = self._redraw
        copy._anchor = self._anchor
        copy._repeat = self._repeat
        copy._index = self._index
        copy._limit = self._limit
        copy._running = self._running
        copy._surfs = [pygame.transform.flip(surf, hbool, vbool) for surf in self._surfs]
        copy._rects = [surf.get_rect() for surf in copy._surfs]
        copy._surf = copy._surfs[copy._index]
        copy._rect = copy._rects[copy._index]
        copy._rect.center = self._rect.center
        copy._osd = self._osd

        return copy



    def rotate(self, angle):
        """
        rotate(angle) -> Animation

        Cria uma cópia rotacionada da animação.

        O argumento "angle" é um float representando quantos graus rotacionar a
        cópia.
        """

        if not isinstance(angle, float):
            raise TypeError('rotate(): o argumento "angle" precisa ser float')

        copy = object.__new__(Animation)

        copy._redraw_count = self._redraw_count
        copy._redraw = self._redraw
        copy._anchor = self._anchor
        copy._repeat = self._repeat
        copy._index = self._index
        copy._limit = self._limit
        copy._running = self._running
        copy._surfs = [pygame.transform.rotozoom(surf, -angle, 1.0) for surf in self._surfs]
        copy._rects = [surf.get_rect() for surf in copy._surfs]
        copy._surf = copy._surfs[copy._index]
        copy._rect = copy._rects[copy._index]
        copy._rect.center = self._rect.center
        copy._osd = self._osd

        return copy



    def scale(self, scale):
        """
        scale(scale) -> Animation

        Retorna uma cópia redimensioada da animação, mantendo a relação de
        aspecto original.

        O argumento "scale" é um float maior que 0 para multiplicar o tamanho
        original da animação.
        """

        if not isinstance(scale, float):
            raise TypeError('scale(): o argumento "scale" precisa ser float')

        if scale <= 0.0:
            raise ValueError('scale(): o argumento "scale" precisa ser maior que 0.0')

        copy = object.__new__(Animation)

        copy._redraw_count = self._redraw_count
        copy._redraw = self._redraw
        copy._anchor = self._anchor
        copy._repeat = self._repeat
        copy._index = self._index
        copy._limit = self._limit
        copy._running = self._running
        copy._surfs = [pygame.transform.rotozoom(surf, 0.0, scale) for surf in self._surfs]
        copy._rects = [surf.get_rect() for surf in copy._surfs]
        copy._surf = copy._surfs[copy._index]
        copy._rect = copy._rects[copy._index]
        copy._rect.center = self._rect.center
        copy._osd = self._osd

        return copy



    def draw(self):
        """
        draw() -> None

        Desenha a animação na tela.
        """

        mindu.Sprite.draw(self)

        self._update()



