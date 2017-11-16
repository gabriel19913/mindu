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
A classe Label está definida aqui.
"""

import os
import pygame
import mindu



class Label(mindu.Sprite):
    """
    Label( text,
           font = None,
           size = 30,
           color = (1.0, 1.0, 1.0, 1.0),
           alignment = "left",
           italic = False,
           bold = False,
           underline = False,
           osd = False,
           **position ) -> Label

    Sprite para representar imagens textuais.

    O argumento "text" é uma string representando o texto a ser renderizado.

    O argumento "font" é uma string representando o nome do arquivo de fonte a
    ser carregado. O único formato de arquivo de fonte suportado é o TTF. Este
    argumento também pode ser None, para que a fonte padrão seja utilizada.

    O argumento "size" é um inteiro maior que 0 representando o tamanho da
    fonte.

    O argumento "color" é uma sequência de 4 floats representando a cor RGBA da
    fonte. Se os floats forem menores que 0.0, serão arredondados para 0.0, e se
    forem maiores que 1.0, serão arredondados para 1.0.

    O argumento "alignment" é "left", "center" ou "right", indicando como o
    texto deve ser alinhado.

    O argumento "italic" é True ou False, indicando se o rótulo usa itálico.

    O argumento "bold" é True ou False, indicando se o rótulo usa negrito.

    O argumento "underline" é True ou False, indicando se o rótulo usa
    sublinhado.

    O argumento "osd" é True ou False, indicando se o rótulo é On-Screen
    Display.

    Os argumentos de palavra-chave opcionais "**position" servem para posicionar
    o rótulo em relação à tela. Os argumentos de palavra-chave válidos são:

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

    __slots__ = ('_text', '_font', '_pygame_font', '_size', '_color',
                 '_ints_color', '_alignment', '_italic', '_bold', '_underline',
                 '_osd', '_surf', '_rect')



    def __init__( self,
                  text,
                  font = None,
                  size = 30,
                  color = (1.0, 1.0, 1.0, 1.0),
                  alignment = 'left',
                  italic = False,
                  bold = False,
                  underline = False,
                  osd = False,
                  **position ):

        if not isinstance(text, str):
            raise TypeError('Label(): o argumento "text" precisa ser string')

        if not isinstance(size, int):
            raise TypeError('Label(): o argumento "size" precisa ser inteiro')

        if size <= 0:
            raise ValueError('Label(): o argumento "size" precisa ser maior que 0')

        if (font is not None) and (not isinstance(font, str)):
            raise TypeError('Label(): o argumento "font" precisa ser string ou None')

        try:
            pygame_font = pygame.font.Font(font, size)

        except:
            raise mindu.Error('Label(): impossível carregar o arquivo "{}"'.format(font))

        if not isinstance(color, (list, tuple)):
            raise TypeError('Label(): o argumento "color" precisa ser lista ou tupla')

        if len(color) != 4:
            raise ValueError('Label(): o argumento "color" precisa ter comprimento 4')

        (r, g, b, a) = color

        if not isinstance(r, float):
            raise TypeError('Label(): o primeiro item do argumento "color" precisa ser float')

        if not isinstance(g, float):
            raise TypeError('Label(): o segundo item do argumento "color" precisa ser float')

        if not isinstance(b, float):
            raise TypeError('Label(): o terceiro item do argumento "color" precisa ser float')

        if not isinstance(a, float):
            raise TypeError('Label(): o quarto item do argumento "color" precisa ser float')

        if r > 1.0: r = 1.0
        elif r < 0.0: r = 0.0

        if g > 1.0: g = 1.0
        elif g < 0.0: g = 0.0

        if b > 1.0: b = 1.0
        elif b < 0.0: b = 0.0

        if a > 1.0: a = 1.0
        elif a < 0.0: a = 0.0

        color = (r, g, b, a)

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        a = int(a * 255)

        ints_color = (r, g, b, a)

        if not isinstance(alignment, str):
            raise TypeError('Label(): o argumento "alignment" precisa ser string')

        if alignment not in ('left', 'center', 'right'):
            raise ValueError('Label(): o argumento "alignment" precisa ser "left", "center" ou "right"')

        if not isinstance(italic, bool):
            raise TypeError('Label(): o argumento "italic" precisa ser True ou False')

        if not isinstance(bold, bool):
            raise TypeError('Label(): o argumento "bold" precisa ser True ou False')

        if not isinstance(underline, bool):
            raise TypeError('Label(): o argumento "underline" precisa ser True ou False')

        if not isinstance(osd, bool):
            raise TypeError('Label(): o argumento "osd" precisa ser True ou False')

        self._text = text
        self._font = font
        self._pygame_font = pygame_font
        self._size = size
        self._color = color
        self._ints_color = ints_color
        self._alignment = alignment
        self._italic = italic
        self._bold = bold
        self._underline = underline
        self._osd = osd

        self._pygame_font.set_italic(self._italic)
        self._pygame_font.set_bold(self._bold)
        self._pygame_font.set_underline(self._underline)

        self._surf = None
        self._rect = None

        self._render()

        for (key, value) in position.items():

            if key not in ('top', 'left', 'bottom', 'right', 'topleft',
                           'bottomleft', 'topright', 'bottomright', 'midtop',
                           'midleft', 'midbottom', 'midright', 'center',
                           'centerx', 'centery'):

                raise KeyError('Label(): argumento de palavra-chave inválido: "{}"'.format(key))

            setattr(self, key, value)



    def _render(self):
        color = self._ints_color[:3]
        lines = self._text.split('\n')
        lines = [self._pygame_font.render(line, True, color) for line in lines]

        width = max((line.get_width() for line in lines))
        linesize = self._pygame_font.get_linesize()
        height = linesize * len(lines)

        surf = pygame.Surface((width, height), pygame.SRCALPHA)

        rect_position = {'top': 0}

        if self._alignment == 'center':
            rect_position['centerx'] = width // 2

        elif self._alignment == 'right':
            rect_position['right'] = width

        for line in lines:
            rect = line.get_rect(**rect_position)
            surf.blit(line, rect)
            rect_position['top'] += linesize

        surf = surf.subsurface(surf.get_bounding_rect())

        alpha = 255 - self._ints_color[3]
        alpha_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
        alpha_surf.fill((0, 0, 0, alpha))

        surf.blit(alpha_surf, (0, 0), None, pygame.BLEND_RGBA_SUB)

        self._surf = surf

        if self._rect is None: self._rect = self._surf.get_rect()
        else: self._rect = self._surf.get_rect(center = self._rect.center)



    def get_text(self):
        """
        get_text() -> str

        Obtém o texto do rótulo.
        """

        return self._text



    def set_text(self, text):
        """
        set_text(text) -> None

        Define o texto do rótulo.

        O argumento "text" é uma string representando o texto a ser renderizado.
        """

        if not isinstance(text, str):
            raise TypeError('set_text(): o argumento "text" precisa ser string')

        self._text = text
        self._render()



    def get_font(self):
        """
        get_font() -> str

        Obtém o nome da fonte do rótulo.
        """

        if self._font is None: return pygame.font.get_default_font()

        return os.path.split(self._font)[1]



    def set_font(self, font):
        """
        set_font(font) -> None

        Define a fonte do rótulo.

        O argumento "font" é uma string representando o nome do arquivo de fonte
        a ser carregado. O único formato de arquivo de fonte suportado é o TTF.
        Este argumento também pode ser None, para que a fonte padrão seja
        utilizada.
        """

        if (font is not None) and (not isinstance(font, str)):
            raise TypeError('set_font(): o argumento "font" precisa ser string ou None')

        try:
            pygame_font = pygame.font.Font(font, self._size)

        except:
            raise mindu.Error('set_font(): impossível carregar o arquivo "{}"'.format(font))

        self._font = font
        self._pygame_font = pygame_font

        self._pygame_font.set_italic(self._italic)
        self._pygame_font.set_bold(self._bold)
        self._pygame_font.set_underline(self._underline)

        self._render()



    def get_size(self):
        """
        get_size() -> int

        Obtém o tamanho da fonte do rótulo.
        """

        return self._size



    def set_size(self, size):
        """
        set_size(size) -> None

        Define o tamanho da fonte do rótulo.

        O argumento "size" é um inteiro maior que 0 representando o tamanho da
        fonte.
        """

        if not isinstance(size, int):
            raise TypeError('set_size(): o argumento "size" precisa ser inteiro')

        if size <= 0:
            raise ValueError('set_size(): o argumento "size" precisa ser maior que 0')

        self._size = size
        self._pygame_font = pygame.font.Font(self._font, size)

        self._pygame_font.set_italic(self._italic)
        self._pygame_font.set_bold(self._bold)
        self._pygame_font.set_underline(self._underline)

        self._render()



    def get_color(self):
        """
        get_color() -> tuple

        Obtém a cor da fonte do rótulo.
        """

        return self._color



    def set_color(self, color):
        """
        set_color(color) -> None

        Define a cor da fonte do rótulo.

        O argumento "color" é uma sequência de 4 floats representando a cor RGBA
        da fonte. Se os floats forem menores que 0.0, serão arredondados para
        0.0, e se forem maiores que 1.0, serão arredondados para 1.0.
        """

        if not isinstance(color, (list, tuple)):
            raise TypeError('set_color(): o argumento "color" precisa ser lista ou tupla')

        if len(color) != 4:
            raise ValueError('set_color(): o argumento "color" precisa ter comprimento 4')

        (r, g, b, a) = color

        if not isinstance(r, float):
            raise TypeError('set_color(): o primeiro item do argumento "color" precisa ser float')

        if not isinstance(g, float):
            raise TypeError('set_color(): o segundo item do argumento "color" precisa ser float')

        if not isinstance(b, float):
            raise TypeError('set_color(): o terceiro item do argumento "color" precisa ser float')

        if not isinstance(a, float):
            raise TypeError('set_color(): o quarto item do argumento "color" precisa ser float')

        if r > 1.0: r = 1.0
        elif r < 0.0: r = 0.0

        if g > 1.0: g = 1.0
        elif g < 0.0: g = 0.0

        if b > 1.0: b = 1.0
        elif b < 0.0: b = 0.0

        if a > 1.0: a = 1.0
        elif a < 0.0: a = 0.0

        self._color = (r, g, b, a)

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        a = int(a * 255)

        self._ints_color = (r, g, b, a)

        self._render()



    def get_alignment(self):
        """
        get_alignment() -> str

        Obtém o alinhamento do texto do rótulo.
        """

        return self._alignment



    def set_alignment(self, alignment):
        """
        set_alignment(alignment) -> None

        Define o alinhamento do texto do rótulo.

        O argumento "alignment" é "left", "center" ou "right", indicando como o
        texto deve ser alinhado.
        """

        if not isinstance(alignment, str):
            raise TypeError('set_alignment(): o argumento "alignment" precisa ser string')

        if alignment not in ('left', 'center', 'right'):
            raise ValueError('set_alignment(): o argumento "alignment" precisa ser "left", "center" ou "right"')

        self._alignment = alignment

        self._render()



    def get_italic(self):
        """
        get_italic() -> bool

        Verifica se o rótulo usa itálico.
        """

        return self._italic



    def set_italic(self, italic):
        """
        set_italic(italic) -> None

        Define se o rótulo usa itálico.

        O argumento "italic" é True ou False, indicando se o rótulo usa itálico.
        """

        if not isinstance(italic, bool):
            raise TypeError('set_italic(): o argumento "italic" precisa ser True ou False')

        self._italic = italic
        self._pygame_font.set_italic(italic)

        self._render()



    def toggle_italic(self):
        """
        toggle_italic() -> None

        Define alternadamente se o rótulo usa itálico.
        """

        self.set_italic(not self._italic)



    def get_bold(self):
        """
        get_bold() -> bool

        Verifica se o rótulo usa negrito.
        """

        return self._bold



    def set_bold(self, bold):
        """
        set_bold(bold) -> None

        Define se o rótulo usa negrito.

        O argumento "bold" é True ou False, indicando se o rótulo usa negrito.
        """

        if not isinstance(bold, bool):
            raise TypeError('set_bold(): o argumento "bold" precisa ser True ou False')

        self._bold = bold
        self._pygame_font.set_bold(bold)

        self._render()



    def toggle_bold(self):
        """
        toggle_bold() -> None

        Define alternadamente se o rótulo usa negrito.
        """

        self.set_bold(not self._bold)



    def get_underline(self):
        """
        get_underline() -> bool

        Verifica se o rótulo usa sublinhado.
        """

        return self._underline



    def set_underline(self, underline):
        """
        set_underline(underline) -> None

        Define se o rótulo usa sublinhado.

        O argumento "underline" é True ou False, indicando se o rótulo usa
        sublinhado.
        """

        if not isinstance(underline, bool):
            raise TypeError('set_underline(): o argumento "underline" precisa ser True ou False')

        self._underline = underline
        self._pygame_font.set_underline(underline)

        self._render()



    def toggle_underline(self):
        """
        toggle_underline() -> None

        Define alternadamente se o rótulo usa sublinhado.
        """

        self.set_underline(not self._underline)



    def copy(self):
        """
        copy() -> Label

        Cria uma cópia do rótulo.
        """

        copy = object.__new__(Label)

        copy._text = self._text
        copy._font = self._font
        copy._pygame_font = pygame.font.Font(self._font, self._size)
        copy._size = self._size
        copy._color = self._color
        copy._ints_color = self._ints_color
        copy._alignment = self._alignment
        copy._italic = self._italic
        copy._bold = self._bold
        copy._underline = self._underline
        copy._osd = self._osd

        copy._pygame_font.set_italic(self._italic)
        copy._pygame_font.set_bold(self._bold)
        copy._pygame_font.set_underline(self._underline)

        copy._surf = self._surf
        copy._rect = self._rect.copy()

        return copy



    def to_image(self):
        """
        to_image() -> Image

        Cria uma imagem a partir do rótulo.
        """

        image = object.__new__(mindu.Image)

        image._surf = self._surf
        image._rect = self._rect.copy()
        image._osd = self._osd

        return image



