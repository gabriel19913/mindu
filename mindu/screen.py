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
A classe Screen está definida aqui.
"""

import os
import pygame
import mindu



class Screen(object):
    """
    Objeto para lidar com a tela.
    """

    __slots__ = ('_title', '_icon', '_size', '_rect', '_zoom_rect', '_full',
                 '_surf', '_osd', '_last_surf', '_bright_surf',
                 '_subtraction_surf', '_red', '_green', '_blue', '_bright',
                 '_zoom', '_on_close', '_on_close_pargs', '_on_close_kwargs',
                 '_replay', '_replay_length')



    def __init__(self):
        self.set_title(None)
        self.set_icon(None)

        info = pygame.display.Info()
        self._size = (info.current_w // 2, info.current_h // 2)

        self._rect = pygame.Rect(0, 0, self._size[0], self._size[1])
        self._zoom_rect = self._rect.copy()

        self._full = False

        self._surf = None
        self._last_surf = None
        self._osd = []

        # Os níveis de brilho e cor podem ser ajustados antes mesmo de a tela
        # ser criada, então estas duas surfaces precisam estar disponíveis.
        self._bright_surf = pygame.Surface(self._size)
        self._bright_surf.set_alpha(0, pygame.RLEACCEL)
        self._subtraction_surf = pygame.Surface(self._size)

        self._red = 1.0
        self._green = 1.0
        self._blue = 1.0
        self._bright = 1.0
        self._zoom = 0.0

        self._on_close = None
        self._on_close_pargs = ()
        self._on_close_kwargs = {}

        self._replay = []
        self._replay_length = 0



    def _create(self):

        if self._full:
            self._surf = pygame.display.set_mode(self._size, pygame.FULLSCREEN)

        else:
            self._surf = pygame.display.set_mode(self._size)

        self._last_surf = self._surf.copy()



    def _update(self):

        if pygame.event.get(pygame.QUIT):

            if self._on_close is None: mindu.loop.stop()

            else: self._on_close(*self._on_close_pargs, **self._on_close_kwargs)

        if self._bright < 1.0: self._surf.blit(self._bright_surf, (0, 0))

        self._zoom_rect.clamp_ip(self._rect)
        if self._zoom > 0.0:
            subsurf = self._surf.subsurface(self._zoom_rect)
            pygame.transform.smoothscale(subsurf, self._size, self._surf)

        if (self._red < 1.0) or (self._green < 1.0) or (self._blue < 1.0):
            self._surf.blit(self._subtraction_surf, (0, 0), None, pygame.BLEND_RGB_SUB)

        for (surf, rect) in self._osd: self._surf.blit(surf, rect)
        self._osd = []

        if mindu.mouse._visible: self._surf.blit(mindu.mouse._cursor._surf, mindu.mouse._position)

        pygame.display.flip()

        self._last_surf = self._surf.copy()

        if self._replay_length:
            self._replay.append(self._last_surf)

            if len(self._replay) > self._replay_length:
                self._replay.pop(0)

        self._surf.fill((0, 0, 0))



    def _destroy(self):

        self._surf = None
        self._last_surf = None
        self._osd = []

        # Reinicializando o módulo display para destruir a tela.
        pygame.display.quit()
        pygame.display.init()

        # A reinicialização do módulo display desconfigura estas coisas, então
        # precisamos configurar de novo.
        pygame.display.set_caption(self._title)
        pygame.display.set_icon(self._icon._surf)
        pygame.mouse.set_visible(False)
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.QUIT)
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_allowed(pygame.JOYAXISMOTION)
        pygame.event.set_allowed(pygame.JOYHATMOTION)
        pygame.event.set_allowed(pygame.JOYBUTTONUP)
        pygame.event.set_allowed(pygame.JOYBUTTONDOWN)



    @property
    def width(self):
        """
        Inteiro representando a largura da tela.

        Somente leitura.
        """

        return self._rect.width



    @property
    def height(self):
        """
        Inteiro representando a altura da tela.

        Somente leitura.
        """

        return self._rect.height



    @property
    def size(self):
        """
        Tupla de inteiros (w, h) representando a largura e a altura da tela.

        Somente leitura.
        """

        return self._rect.size



    @property
    def top(self):
        """
        Inteiro representando a coordenada Y da borda superior da tela.

        Somente leitura.
        """

        return self._rect.top



    @property
    def left(self):
        """
        Inteiro representando a coordenada X da borda esquerda da tela.

        Somente leitura.
        """

        return self._rect.left



    @property
    def bottom(self):
        """
        Inteiro representando a coordenada Y da borda inferior da tela.

        Somente leitura.
        """

        return self._rect.bottom



    @property
    def right(self):
        """
        Inteiro representando a coordenada X da borda direita da tela.

        Somente leitura.
        """

        return self._rect.right



    @property
    def centerx(self):
        """
        Inteiro representando a coordenada X do centro da tela.

        Somente leitura.
        """

        return self._rect.centerx



    @property
    def centery(self):
        """
        Inteiro representando a coordenada Y do centro da tela.

        Somente leitura.
        """

        return self._rect.centery



    @property
    def topleft(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto superior
        esquerdo da tela.

        Somente leitura.
        """

        return self._rect.topleft



    @property
    def bottomleft(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto inferior
        esquerdo da tela.

        Somente leitura.
        """

        return self._rect.bottomleft



    @property
    def topright(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto superior
        direito da tela.

        Somente leitura.
        """

        return self._rect.topright



    @property
    def bottomright(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto inferior
        direito da tela.

        Somente leitura.
        """

        return self._rect.bottomright



    @property
    def midtop(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        superior da tela.

        Somente leitura.
        """

        return self._rect.midtop



    @property
    def midleft(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        esquerda da tela.

        Somente leitura.
        """

        return self._rect.midleft



    @property
    def midbottom(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        inferior da tela.

        Somente leitura.
        """

        return self._rect.midbottom



    @property
    def midright(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        direita da tela.

        Somente leitura.
        """

        return self._rect.midright



    @property
    def center(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do centro da tela.

        Somente leitura.
        """

        return self._rect.center



    @property
    def ztop(self):
        """
        Inteiro representando a coordenada Y da borda superior do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.top



    @ztop.setter
    def ztop(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "ztop" precisa ser inteiro')

        self._zoom_rect.top = value



    @property
    def zleft(self):
        """
        Inteiro representando a coordenada X da borda esquerda do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.left



    @zleft.setter
    def zleft(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "zleft" precisa ser inteiro')

        self._zoom_rect.left = value



    @property
    def zbottom(self):
        """
        Inteiro representando a coordenada Y da borda inferior do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.bottom



    @zbottom.setter
    def zbottom(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "zbottom" precisa ser inteiro')

        self._zoom_rect.bottom = value



    @property
    def zright(self):
        """
        Inteiro representando a coordenada X da borda direita do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.right



    @zright.setter
    def zright(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "zright" precisa ser inteiro')

        self._zoom_rect.right = value



    @property
    def zcenterx(self):
        """
        Inteiro representando a coordenada X do centro do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.centerx



    @zcenterx.setter
    def zcenterx(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "zcenterx" precisa ser inteiro')

        self._zoom_rect.centerx = value



    @property
    def zcentery(self):
        """
        Inteiro representando a coordenada Y do centro do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.centery



    @zcentery.setter
    def zcentery(self, value):

        if not isinstance(value, int):
            raise TypeError('o atributo "zcentery" precisa ser inteiro')

        self._zoom_rect.centery = value



    @property
    def ztopleft(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto superior
        esquerdo do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.topleft



    @ztopleft.setter
    def ztopleft(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "ztopleft" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "ztopleft" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "ztopleft" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "ztopleft" precisa ser inteiro')

        self._zoom_rect.topleft = value



    @property
    def zbottomleft(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto inferior
        esquerdo do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.bottomleft



    @zbottomleft.setter
    def zbottomleft(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zbottomleft" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "zbottomleft" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zbottomleft" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zbottomleft" precisa ser inteiro')

        self._zoom_rect.bottomleft  = value



    @property
    def ztopright(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto superior
        direito do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.topright



    @ztopright.setter
    def ztopright(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "ztopright" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "ztopright" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "ztopright" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "ztopright" precisa ser inteiro')

        self._zoom_rect.topright  = value



    @property
    def zbottomright(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do canto inferior
        direito do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.bottomright



    @zbottomright.setter
    def zbottomright(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zbottomright" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "bottomright" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zbottomright" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zbottomright" precisa ser inteiro')

        self._zoom_rect.bottomright = value



    @property
    def zmidtop(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        superior do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.midtop



    @zmidtop.setter
    def zmidtop(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zmidtop" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "zmidtop" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zmidtop" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zmidtop" precisa ser inteiro')

        self._zoom_rect.midtop = value



    @property
    def zmidleft(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        esquerda do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.midleft



    @zmidleft.setter
    def zmidleft(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zmidleft" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "zmidleft" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zmidleft" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zmidleft" precisa ser inteiro')

        self._zoom_rect.midleft = value



    @property
    def zmidbottom(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        inferior do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.midbottom



    @zmidbottom.setter
    def zmidbottom(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zmidbottom" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "zmidbottom" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zmidbottom" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zmidbottom" precisa ser inteiro')

        self._zoom_rect.midbottom = value



    @property
    def zmidright(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do meio da borda
        direita do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.midright



    @zmidright.setter
    def zmidright(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zmidright" precisa ser lista ou tupla')

        if len(value) != 2:
            raise ValueError('o atributo "zmidright" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zmidright" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zmidright" precisa ser inteiro')

        self._zoom_rect.midright = value



    @property
    def zcenter(self):
        """
        Tupla de inteiros representando as coordenadas X e Y do centro do zoom.

        Leitura e escrita.
        """

        return self._zoom_rect.center



    @zcenter.setter
    def zcenter(self, value):

        if not isinstance(value, (list, tuple)):
            raise TypeError('o atributo "zcenter" precisa ser lista tupla')

        if len(value) != 2:
            raise ValueError('o atributo "zcenter" precisa ter comprimento 2')

        (x, y) = value

        if not isinstance(x, int):
            raise TypeError('o primeiro item do atributo "zcenter" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('o segundo item do atributo "zcenter" precisa ser inteiro')

        self._zoom_rect.center = value



    @property
    def red(self):
        """
        Float representando o nível de vermelho da tela.

        Leitura e escrita.
        """

        return self._red



    @red.setter
    def red(self, value):

        if not isinstance(value, float):
            raise TypeError('o atributo "red" precisa ser float')

        if value < 0.0: value = 0.0
        elif value > 1.0: value = 1.0

        self._red = value

        red = 255 - int(self._red * 255)
        green = 255 - int(self._green * 255)
        blue = 255 - int(self._blue * 255)

        self._subtraction_surf.fill((red, green, blue))



    @property
    def green(self):
        """
        Float representando o nível de verde da tela.

        Leitura e escrita.
        """

        return self._green



    @green.setter
    def green(self, value):

        if not isinstance(value, float):
            raise TypeError('o atributo "green" precisa ser float')

        if value < 0.0: value = 0.0
        elif value > 1.0: value = 1.0

        self._green = value

        red = 255 - int(self._red * 255)
        green = 255 - int(self._green * 255)
        blue = 255 - int(self._blue * 255)

        self._subtraction_surf.fill((red, green, blue))



    @property
    def blue(self):
        """
        Float representando o nível de azul da tela.

        Leitura e escrita.
        """

        return self._blue



    @blue.setter
    def blue(self, value):

        if not isinstance(value, float):
            raise TypeError('o atributo "blue" precisa ser float')

        if value < 0.0: value = 0.0
        elif value > 1.0: value = 1.0

        self._blue = value

        red = 255 - int(self._red * 255)
        green = 255 - int(self._green * 255)
        blue = 255 - int(self._blue * 255)

        self._subtraction_surf.fill((red, green, blue))



    @property
    def bright(self):
        """
        Float representando o nível de brilho da tela.

        Leitura e escrita.
        """

        return self._bright



    @bright.setter
    def bright(self, value):

        if not isinstance(value, float):
            raise TypeError('o atributo "bright" precisa ser float')

        if value < 0.0: value = 0.0
        elif value > 1.0: value = 1.0

        self._bright = value

        bright = 255 - int(self._bright * 255)

        self._bright_surf.set_alpha(bright, pygame.RLEACCEL)



    @property
    def zoom(self):
        """
        Float representando o nível de zoom da tela.

        Obtém a quantidade de zoom da tela.
        """

        return self._zoom



    @zoom.setter
    def zoom(self, value):

        if not isinstance(value, float):
            raise TypeError('o atributo "zoom" precisa ser float')

        if value > 1.0: value = 1.0

        elif value < 0.0: value = 0.0

        self._zoom = value

        zoom = 1.0 - self._zoom

        width = int(zoom * self._rect.width) or 1
        height = int(zoom * self._rect.height) or 1

        center = self._zoom_rect.center
        self._zoom_rect = pygame.Rect(0, 0, width, height)
        self._zoom_rect.center = center



    def grab(self, sprite):
        """
        grab(sprite) -> tuple

        Move o sprite dado (se necessário), para que fique totalmente dentro da
        tela. Se o sprite dado for maior que a tela, então será centralizado na
        tela.

        Note que uma tupla de inteiros (x, y) é retornada, indicando quantos
        pixels o sprite dado foi deslocado nos eixos X e Y.

        São considerados sprites os objetos Image, Label e Animation.
        """

        if not isinstance(sprite, mindu.Sprite):
            raise TypeError('grab(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        rect = sprite._rect.clamp(self._rect)

        offset = (rect.centerx - sprite._rect.centerx,
                  rect.centery - sprite._rect.centery)

        sprite._rect = rect

        return offset



    def contains(self, sprite):
        """
        contains(sprite) -> bool

        Verifica se o sprite dado está completamente dentro da tela.

        São considerados sprites os objetos Image, Label e Animation.
        """

        if not isinstance(sprite, mindu.Sprite):
            raise TypeError('contains(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        return bool(self._rect.contains(sprite._rect))



    def collide(self, sprite):
        """
        collide(sprite) -> bool

        Verifica se alguma porção do sprite dado está dentro da tela.

        São considerados sprites os objetos Image, Label e Animation.
        """

        if not isinstance(sprite, mindu.Sprite):
            raise TypeError('collide(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        return bool(self._rect.colliderect(sprite._rect))



    def collide_point(self, point):
        """
        collide_point(point) -> bool

        Verifica se o ponto dado está dentro da tela.

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



    def zgrab(self, sprite):
        """
        zgrab(sprite) -> tuple

        Funciona como grab(), mas leva em consideração o zoom.
        """

        if not isinstance(sprite, mindu.Sprite):
            raise TypeError('zgrab(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        rect = sprite._rect.clamp(self._zoom_rect)

        offset = (rect.centerx - sprite._rect.centerx,
                  rect.centery - sprite._rect.centery)

        sprite._rect = rect

        return offset



    def zcontains(self, sprite):
        """
        zcontains(sprite) -> bool

        Funciona como contains(), mas leva em consideração o zoom.
        """

        if not isinstance(sprite, mindu.Sprite):
            raise TypeError('zcontains(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        return bool(self._zoom_rect.contains(sprite._rect))



    def zcollide(self, sprite):
        """
        zcollide(sprite) -> bool

        Funciona como collide(), mas leva em consideração o zoom.
        """

        if not isinstance(sprite, mindu.Sprite):
            raise TypeError('zcollide(): o argumento "sprite" precisa ser um objeto Image, Label ou Animation')

        return bool(self._zoom_rect.colliderect(sprite._rect))



    def zcollide_point(self, point):
        """
        zcollide_point(point) -> bool

        Funciona como collide_point(), mas leva em consideração o zoom.
        """

        if not isinstance(point, (list, tuple)):
            raise TypeError('zcollide_point(): o argumento "point" precisa ser lista ou tupla')

        if len(point) != 2:
            raise ValueError('zcollide_point(): o argumento "point" precisa ter comprimento 2')

        (x, y) = point

        if not isinstance(x, int):
            raise TypeError('zcollide_point(): o primeiro item do argumento "point" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('zcollide_point(): o segundo item do argumento "point" precisa ser inteiro')

        return bool(self._zoom_rect.collidepoint(point))



    def move_zoom(self, x, y):
        """
        move_zoom(x, y) -> None

        Move o zoom.

        O argumento "x" é um inteiro, representando quantos pixels o zoom deve
        ser movido no eixo X.

        O argumento "y" é um inteiro, representando quantos pixels o zoom deve
        ser movido no eixo Y.
        """

        if not isinstance(x, int):
            raise TypeError('move_zoom(): o argumento "x" precisa ser inteiro')

        if not isinstance(y, int):
            raise TypeError('move_zoom(): o argumento "y" precisa ser inteiro')

        self._zoom_rect.move_ip(x, y)



    def get_title(self):
        """
        get_title() -> str

        Obtém o título usado quando a tela está em modo janela.
        """

        return self._title



    def set_title(self, title):
        """
        set_title(title) -> None

        Define o título usado quando a tela está em modo janela.

        O argumento "title" é uma string não-vazia. Também pode ser None para
        restaurar o título padrão.
        """

        if (title is not None) and (not isinstance(title, str)):
            raise TypeError('set_title(): o argumento "title" precisa ser string ou None')

        if (title is not None) and (not title):
            raise ValueError('set_title(): o argumento "title" não pode ser string vazia')

        if title is None: title = 'Mindu Window'

        self._title = title

        pygame.display.set_caption(title)



    def get_icon(self):
        """
        get_icon() -> Image

        Obtém o ícone utilizado quando a tela está em modo janela.
        """

        return self._icon



    def set_icon(self, image):
        """
        set_icon(image) -> None

        Define o ícone utilizado quando a tela está em modo janela.

        O argumento "image" é um objeto Image. Também pode ser None para
        restaurar o ícone padrão.
        """

        if (image is not None) and (not isinstance(image, mindu.Image)):
            raise TypeError('set_icon(): o argumento "image" precisa ser um objeto Image ou None')

        if image is None:
            image = os.path.dirname(os.path.abspath(__file__))
            image = os.path.join(image, 'icon.png')
            image = mindu.Image(image, True)

        self._icon = image
        pygame.display.set_icon(image._surf)



    def get_full(self):
        """
        get_full() -> bool

        Verifica se a tela está cheia.
        """

        return self._full



    def set_full(self, full):
        """
        set_full(full) -> None

        Define se a tela está cheia.

        O argumento "full" é True ou False.
        """

        if not isinstance(full, bool):
            raise TypeError('set_full(): o argumento "full" precisa ser True ou False')

        self._full = full

        if not mindu.loop._running: return

        if self._full:
            self._surf = pygame.display.set_mode(self._size, pygame.FULLSCREEN)

        else:
            self._surf = pygame.display.set_mode(self._size)



    def toggle_full(self):
        """
        toggle_full() -> None

        Define alternadamente se a tela está cheia.
        """

        self.set_full(not self._full)



    def set_size(self, size):
        """
        set_size(size) -> None

        Define as dimensões da tela.

        O argumento "size" é um par de inteiros (w, h) representando a largura e
        a altura da tela.
        """

        if mindu.loop._running:
            raise mindu.Error('set_size(): método chamado com o loop interno do Mindu rodando')

        if not isinstance(size, (list, tuple)):
            raise TypeError('set_size(): o argumento "size" precisa ser lista ou tupla')

        if len(size) != 2:
            raise ValueError('set_size(): o argumento "size" precisa ter comprimento 2')

        (w, h) = size

        if not isinstance(w, int):
            raise TypeError('set_size(): o primeiro item do argumento "size" precisa ser inteiro')

        if not isinstance(h, int):
            raise TypeError('set_size(): o segundo item do argumento "size" precisa ser inteiro')

        if w <= 0:
            raise ValueError('set_size(): o primeiro item do argumento "size" precis ser maior que 0')

        if h <= 0:
            raise ValueError('set_size(): o segundo item do argumento "size" precis ser maior que 0')

        self._size = tuple(size)

        self._rect = pygame.Rect(0, 0, self._size[0], self._size[1])

        self._zoom_rect = self._rect.copy()
        zoom = 1.0 - self._zoom
        width = int(zoom * self._rect.width) or 1
        height = int(zoom * self._rect.height) or 1
        center = self._zoom_rect.center
        self._zoom_rect = pygame.Rect(0, 0, width, height)
        self._zoom_rect.center = center

        self._bright_surf = pygame.Surface(self._size)
        bright = 255 - int(self._bright * 255)
        self._bright_surf.set_alpha(bright, pygame.RLEACCEL)

        self._subtraction_surf = pygame.Surface(self._size)
        red = 255 - int(self._red * 255)
        green = 255 - int(self._green * 255)
        blue = 255 - int(self._blue * 255)
        self._subtraction_surf.fill((red, green, blue))



    def on_close(self, callable, *pargs, **kwargs):
        """
        on_close(callable, *pargs, **kwargs) -> callable

        Registra o objeto chamável dado, para que seja chamado sempre que o
        usuário tenta fechar a tela, quando a tela está em modo janela.

        O argumento "callable" é o objeto chamável a ser registrado. Pode ser
        None, para que nenhum objeto chamável fique registrado.

        Os argumentos posicionais e de palavra-chave opcionais "*pargs" e
        "**kwargs" serão repassados ao objeto chamável a cada chamada.

        Note que o mesmo objeto chamável dado é retornado de volta para
        facilitar o uso deste método como um decorador.
        """

        self._on_close = callable
        self._on_close_pargs = pargs
        self._on_close_kwargs = kwargs

        return callable



    def get_last_frame(self):
        """
        get_last_frame() -> Image

        Obtém o último quadro renderizado como uma imagem.
        """

        if not mindu.loop._running:
            raise mindu.Error('get_last_frame(): método chamado com o loop interno do Mindu parado')

        image = object.__new__(mindu.Image)
        image._surf = self._last_surf
        image._rect = image._surf.get_rect()
        image._osd = False

        return image



    def shot(self, file):
        """
        shot(file) -> None

        Salva o último frame renderizado no disco.

        O argumento "file" é o nome do arquivo onde os dados serão despejados.
        A extensão de arquivo precisa estar presente. As extensões válidas são:
        ".bmp", ".tga", ".png" e ".jpeg".
        """

        if not mindu.loop._running:
            raise mindu.Error('shot(): método chamado com o loop interno do Mindu parado')

        if not isinstance(file, str):
            raise TypeError('shot(): o argumento "file" precisa ser string')

        ext = os.path.splitext(file)[1]

        if ext.upper() not in ('.BMP', '.TGA', '.PNG', '.JPEG'):
            raise ValueError('shot(): extensão de arquivo inválida: "{}"'.format(ext))

        try: pygame.image.save(self._last_surf, file)

        except: raise mindu.Error('shot(): impossível despejar dados em "{}"'.format(file))



    def get_replay_length(self):
        """
        get_replay_length() -> int

        Obtém o comprimento do replay (número de quadros do replay).

        A tela guarda os últimos N quadros renderizados em um histórico interno,
        e você pode obter esses quadros na forma de uma animação (um replay) com
        o método get_replay().
        """

        return self._replay_length



    def set_replay_length(self, length):
        """
        set_replay_length(length) -> None

        Define o comprimento do replay (número de quadros do replay).

        A tela guarda os últimos N quadros renderizados em um histórico interno,
        e você pode obter esses quadros na forma de uma animação (um replay) com
        o método get_replay().

        O argumento "length" é um inteiro maior ou igual a 0. Se for 0, então
        nenhum quadro será mantido no histórico, e assim o método get_replay()
        provocará um erro.
        """

        if not isinstance(length, int):
            raise TypeError('set_replay_length(): o argumento "length" precisa ser inteiro')

        if length < 0:
            raise ValueError('set_replay_length(): o argumento "length" precisa ser maior ou igual a 0')

        if not length: self._replay = []

        else: self._replay = self._replay[-length:]

        self._replay_length = length



    def get_replay(self):
        """
        get_replay() -> Animation

        Obtém os últimos N quadros renderizados como uma animação de replay.

        Use os métodos get_replay_length() e set_replay_length() para consultar
        e definir o comprimento do replay.
        """

        if not mindu.loop._running:
            raise mindu.Error('get_replay(): método chamado com o loop interno do Mindu parado')

        if not self._replay:
            raise mindu.Error('get_replay(): nenhum frame no histórico')

        animation = object.__new__(mindu.Animation)

        animation._surfs = self._replay[:]
        animation._rects = [surf.get_rect() for surf in animation._surfs]

        animation._redraw = 1
        animation._anchor = 'midbottom'
        animation._repeat = True
        animation._running = True
        animation._osd = False

        animation._redraw_count = 0
        animation._index = 0
        animation._limit = len(animation._surfs)

        animation._surf = animation._surfs[animation._index]
        animation._rect = animation._rects[animation._index]

        return animation



