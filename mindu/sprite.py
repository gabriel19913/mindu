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
A classe Sprite está definida aqui.
"""

import mindu



class Sprite(object):
    """
    Classe de base dos sprites.
    """

    __slots__ = ()



    @property
    def width(self):
        """
        Inteiro representando a largura do sprite.

        Somente leitura.
        """

        return self._rect.width



    @property
    def height(self):
        """
        Inteiro representando a altura do sprite.

        Somente leitura.
        """

        return self._rect.height



    @property
    def size(self):
        """
        Tupla de inteiros (w, h) representando a largura e a altura do sprite.

        Somente leitura.
        """

        return self._rect.size



    @property
    def top(self):
        """
        Inteiro representando a coordenada Y da borda superior do sprite.

        Leitura e escrita.
        """

        return self._rect.top



    @top.setter
    def top(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "top" precisa ser inteiro')

        self._rect.top = value



    @property
    def left(self):
        """
        Inteiro representando a coordenada X da borda esquerda do sprite.

        Leitura e escrita.
        """

        return self._rect.left



    @left.setter
    def left(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "left" precisa ser inteiro')

        self._rect.left = value



    @property
    def bottom(self):
        """
        Inteiro representando a coordenada Y da borda inferior do sprite.

        Leitura e escrita.
        """

        return self._rect.bottom



    @bottom.setter
    def bottom(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "bottom" precisa ser inteiro')

        self._rect.bottom = value



    @property
    def right(self):
        """
        Inteiro representando a coordenada X da borda direita do sprite.

        Leitura e escrita.
        """

        return self._rect.right



    @right.setter
    def right(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "right" precisa ser inteiro')

        self._rect.right = value



    @property
    def centerx(self):
        """
        Inteiro representando a coordenada X do centro do sprite.

        Leitura e escrita.
        """

        return self._rect.centerx



    @centerx.setter
    def centerx(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "centerx" precisa ser inteiro')

        self._rect.centerx = value



    @property
    def centery(self):
        """
        Inteiro representando a coordenada Y do centro do sprite.

        Leitura e escrita.
        """

        return self._rect.centery



    @centery.setter
    def centery(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "centery" precisa ser inteiro')

        self._rect.centery = value



    @property
    def topleft(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do canto
        superior esquerdo do sprite.

        Leitura e escrita.
        """

        return self._rect.topleft



    @topleft.setter
    def topleft(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "topleft" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "topleft" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "topleft" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "topleft" precisa ser inteiro')

        self._rect.topleft = value



    @property
    def bottomleft(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do canto
        inferior esquerdo do sprite.

        Leitura e escrita.
        """

        return self._rect.bottomleft



    @bottomleft.setter
    def bottomleft(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "bottomleft" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "bottomleft" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "bottomleft" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "bottomleft" precisa ser inteiro')

        self._rect.bottomleft  = value



    @property
    def topright(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do canto
        superior direito do sprite.

        Leitura e escrita.
        """

        return self._rect.topright



    @topright.setter
    def topright(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "topright" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "topright" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "topright" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "topright" precisa ser inteiro')

        self._rect.topright  = value



    @property
    def bottomright(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do canto
        inferior direito do sprite.

        Leitura e escrita.
        """

        return self._rect.bottomright



    @bottomright.setter
    def bottomright(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "bottomright" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "bottomright" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "bottomright" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "bottomright" precisa ser inteiro')

        self._rect.bottomright = value



    @property
    def midtop(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do meio da
        borda superior do sprite.

        Leitura e escrita.
        """

        return self._rect.midtop



    @midtop.setter
    def midtop(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "midtop" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "midtop" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "midtop" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "midtop" precisa ser inteiro')

        self._rect.midtop = value



    @property
    def midleft(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do meio da
        borda esquerda do sprite.

        Leitura e escrita.
        """

        return self._rect.midleft



    @midleft.setter
    def midleft(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "midleft" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "midleft" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "midleft" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "midleft" precisa ser inteiro')

        self._rect.midleft = value



    @property
    def midbottom(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do meio da
        borda inferior do sprite.

        Leitura e escrita.
        """

        return self._rect.midbottom



    @midbottom.setter
    def midbottom(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "midbottom" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "midbottom" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "midbottom" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "midbottom" precisa ser inteiro')

        self._rect.midbottom = value



    @property
    def midright(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do meio da
        borda direita do sprite.

        Leitura e escrita.
        """

        return self._rect.midright



    @midright.setter
    def midright(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "midright" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "midright" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "midright" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "midright" precisa ser inteiro')

        self._rect.midright = value



    @property
    def center(self):
        """
        Tupla de inteiros (x, y) representando as coordenadas X e Y do centro do
        sprite.

        Leitura e escrita.
        """

        return self._rect.center



    @center.setter
    def center(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "center" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "center" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "center" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "center" precisa ser inteiro')

        self._rect.center = value



    def grab(self, sprite):
        """
        grab(sprite) -> tuple

        Move o sprite dado (se necessário), para que fique totalmente dentro
        deste sprite. Se o sprite dado for maior que este sprite, então será
        centralizado neste sprite.

        Note que uma tupla de inteiros (x, y) é retornada, indicando quantos
        pixels o sprite dado foi deslocado nos eixos X e Y.

        São considerados sprites os objetos Image, Label e Animation.
        """

        if not isinstance(sprite, Sprite):
            raise TypeError('grab(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        rect = sprite._rect.clamp(self._rect)

        offset = (rect.centerx - sprite._rect.centerx,
                  rect.centery - sprite._rect.centery)

        sprite._rect = rect

        return offset



    def contains(self, sprite):
        """
        contains(sprite) -> bool

        Verifica se o sprite dado está completamente dentro deste sprite.

        São considerados sprites os objetos Image, Label e Animation.
        """

        if not isinstance(sprite, Sprite):
            raise TypeError('contains(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        return bool(self._rect.contains(sprite._rect))



    def collide(self, sprite):
        """
        collide(sprite) -> bool

        Verifica se alguma porção do sprite dado está dentro deste sprite.

        São considerados sprites os objetos Image, Label e Animation.
        """

        if not isinstance(sprite, Sprite):
            raise TypeError('collide(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        return bool(self._rect.colliderect(sprite._rect))



    def collide_point(self, point):
        """
        collide_point(point) -> bool

        Verifica se o ponto dado está dentro do sprite.

        O argumento "point" é um par de inteiros (x, y) representando as
        cooredenadas X e Y de um ponto.
        """

        if not isinstance(point, (list, tuple)):
            raise TypeError('collide_point(): o argumento "point" precisa ser lista ou tupla')

        if len(point) != 2:
            raise ValueError('collide_point(): o argumento "point" precisa ter comprimento 2')

        (x, y) = point

        if not isinstance(x, int):
            raise TypeError('collide_point(): o primeiro item do argumento "point" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('collide_point(): o segundo item do argumento "point" precisa ser inteiro')

        return bool(self._rect.collidepoint(point))



    def move(self, x, y):
        """
        move(x, y) -> None

        Move o sprite.

        O argumento "x" é um inteiro representando quantos pixels o sprite deve
        ser movido no eixo X.

        O argumento "y" é um inteiro representando quantos pixels o sprite deve
        ser movido no eixo Y.
        """

        if not isinstance(x, int):
            raise TypeError('move(): o argumento "x" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('move(): o argumento "y" precisa ser inteiro')

        return self._rect.move_ip(x, y)



    def get_osd(self):
        """
        get_osd() -> bool

        Verifica se o sprite é On-Screen Display.
        """

        return self._osd



    def set_osd(self, osd):
        """
        set_osd(osd) -> None

        Define se o sprite é On-Screen Display.

        O argumento "osd" é True ou false.
        """

        if not isinstance(osd, bool):
            raise TypeError('set_osd(): o argumento "osd" precisa ser True ou False')

        self._osd = osd



    def toggle_osd(self):
        """
        toggle_osd() -> None

        Define alternadamente se o sprite é On-Screen Display.
        """

        self._osd = not self._osd



    def draw(self):
        """
        draw() -> None

        Desenha o sprite na tela.
        """

        if not mindu.loop._running:
            raise mindu.Error('draw(): método chamado com o loop interno do Mindu parado')

        if self._osd:
            mindu.screen._osd.append((self._surf, self._rect))

        else:
            mindu.screen._surf.blit(self._surf, self._rect)



