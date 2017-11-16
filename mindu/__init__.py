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
Ferramenta baseada em Pygame para desenvolvimento rápido e fácil de jogos 2D.

O Mindu provê:

reload_joysticks ------ função para recarregar os joysticks.

Animation - tipo de objeto para representar animações.
Error ----- tipo de erros específicos do Mindu.
Image ----- tipo de objeto para representar imagens.
Label ----- tipo de objeto para representar imagens textuais.
Sound ----- tipo de objeto para representar sons.

channels -- tupla de objetos com funcionalidades para lidar com canais de som.
joysticks - tupla de objetos com funcionalidades para lidar com joysticks.
keyboard -- objeto com funcionalidades para lidar com o teclado.
logo ------ o logo do Mindu como um objeto Image.
loop ------ objeto com funcionalidades para lidar com o loop interno do Mindu.
mouse ----- objeto com funcionalidades para lidar com o mouse.
screen ---- objeto com funcionalidades para lidar com a tela.
version --- tupla de inteiros representando a versão do Mindu.
"""

import os
import atexit
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'

atexit.register(pygame.quit)

pygame.mixer.pre_init(44100, -16, 1, 0)
pygame.init()

pygame.mixer.set_num_channels(100)

pygame.mouse.set_visible(False)

pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
pygame.event.set_allowed(pygame.JOYAXISMOTION)
pygame.event.set_allowed(pygame.JOYHATMOTION)
pygame.event.set_allowed(pygame.JOYBUTTONUP)
pygame.event.set_allowed(pygame.JOYBUTTONDOWN)

from mindu.error import Error
from mindu.input import Input
from mindu.sprite import Sprite
from mindu.image import Image
from mindu.label import Label
from mindu.animation import Animation
from mindu.sound import Sound
from mindu.keyboard import Keyboard
from mindu.mouse import Mouse
from mindu.joystick import Joystick
from mindu.loop import Loop
from mindu.screen import Screen
from mindu.channel import Channel

__all__ = ('reload_joysticks', 'Animation', 'Error', 'Image', 'Label', 'Sound',
           'channels', 'joysticks', 'keyboard', 'logo', 'loop', 'mouse',
           'screen', 'version')

__author__ = 'José Falero <jzfalero.@gmail.com>'
__version__ = '1.0'

version = (1, 0)

keyboard = Keyboard()
mouse = Mouse()
joysticks = tuple([Joystick(id) for id in range(pygame.joystick.get_count())])
channels = tuple([Channel(id) for id in range(pygame.mixer.get_num_channels())])
screen = Screen()
loop = Loop()
logo = os.path.dirname(os.path.abspath(__file__))
logo = os.path.join(logo, 'logo.png')
logo = Image(logo)



def reload_joysticks():
    """
    reload_joysticks() -> None

    Recarrega os joysticks conectados ao computador.
    """

    global joysticks

    pygame.joystick.quit()
    pygame.joystick.init()

    joysticks = tuple([Joystick(id) for id in range(pygame.joystick.get_count())])



