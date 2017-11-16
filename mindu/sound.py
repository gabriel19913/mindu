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
A classe Sound está definida aqui.
"""

import os
import pygame
import mindu



class PygameSound(pygame.mixer.Sound): __slots__ = ('_mindu_sound',)



class Sound(object):
    """
    Sound(file) -> Sound

    Objeto para representar sons.

    O argumento "file" é uma string representando o nome do arquivo de som a ser
    carregado. Os formatos de arquivo de som suportados são: WAV e OGG.
    """

    __slots__ = ('_pygame_sound',)



    def __init__(self, file):

        if not isinstance(file, str):
            raise TypeError('Sound(): o argumento "file" precisa ser string')

        if not os.path.exists(file):
            raise mindu.Error('Sound(): impossível carregar o arquivo "{}"'.format(file))

        if not os.path.isfile(file):
            raise mindu.Error('Sound(): impossível carregar o arquivo "{}"'.format(file))

        if os.path.splitext(file)[1].upper() not in ('.OGG', '.WAV'):
            raise mindu.Error('Sound(): o formato do arquivo de som precisa ser OGG ou WAV')

        try:
            self._pygame_sound = PygameSound(file)

        except:
            raise mindu.Error('Sound(): impossível carregar o arquivo "{}"'.format(file))

        self._pygame_sound._mindu_sound = self



    def get_num_channels(self):
        """
        get_num_channels() -> int

        Retorna um inteiro, indicando o número de canais reproduzindo este som.
        """

        return self._pygame_sound.get_num_channels()



    def get_length(self):
        """
        get_length() -> int

        Retorna um inteiro, indicando a duração deste som em milissegundos.
        """

        return int(self._pygame_sound.get_length() * 1000)




