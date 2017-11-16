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
A classe Loop está definida aqui.
"""

import pygame
import mindu



class Loop(object):
    """
    Objeto representando o loop interno do Mindu.
    """

    __slots__ = ('_running', '_ips', '_on_iterate', '_on_iterate_pargs',
                 '_on_iterate_kwargs')



    def __init__(self):
        self._running = False
        self._ips = 60
        self._on_iterate = None
        self._on_iterate_pargs = ()
        self._on_iterate_kwargs = {}



    def start(self):
        """
        start() -> None

        Inicia o loop.
        """

        if self._running:
            raise mindu.Error('start(): método chamado com o loop já rodando')

        self._running = True
        tick = pygame.time.Clock().tick

        mindu.screen._create()

        try:
            while True:
                mindu.keyboard._update()
                mindu.mouse._update()

                pygame.event.get(pygame.JOYAXISMOTION)
                pygame.event.get(pygame.JOYHATMOTION)
                pygame.event.get(pygame.JOYBUTTONUP)
                pygame.event.get(pygame.JOYBUTTONDOWN)

                for joystick in mindu.joysticks: joystick._update()

                if self._on_iterate is not None:
                    self._on_iterate(*self._on_iterate_pargs, **self._on_iterate_kwargs)

                mindu.screen._update()

                tick(self._ips)

        except Stop: pass

        finally:
            mindu.screen._destroy()
            pygame.mixer.stop()
            self._running = False



    def stop(self):
        """
        stop() -> None

        Interrompe o loop.
        """

        if not self._running:
            raise mindu.Error('stop(): método chamado com o loop já parado')

        raise Stop()



    def running(self):
        """
        running() -> bool

        Verifica se o loop está rodando.
        """

        return self._running



    def on_iterate(self, callable, *pargs, **kwargs):
        """
        on_iterate(callable, *pargs, **kwargs) -> callable

        Registra o objeto chamável dado, para que seja chamado uma vez a cada
        iteração do loop.

        O argumento "callable" é o objeto chamável a ser registrado. Pode ser
        None, para que nenhum objeto chamável fique registrado.

        Os argumentos posicionais e de palavra-chave opcionais "*pargs" e
        "**kwargs" serão repassados ao objeto chamável a cada chamada.

        Note que o mesmo objeto chamável dado é retornado de volta para
        facilitar o uso deste método como um decorador.
        """

        self._on_iterate = callable
        self._on_iterate_pargs = pargs
        self._on_iterate_kwargs = kwargs

        return callable



    def get_ips(self):
        """
        get_ips() -> int

        Obtém a taxa de iterações por segundo do loop.
        """

        return self._ips



    def set_ips(self, ips):
        """
        set_ips(ips) -> None

        Define a taxa de iterações por segundo do loop.

        O argumento ips é um inteiro maior que 0.
        """

        if not isinstance(ips, int):
            raise TypeError('set_ips(): o argumento "ips" precisa ser inteiro')

        if ips <= 0:
            raise ValueError('set_ips(): o argumento "ips" precisa ser maior que 0')

        self._ips = ips




class Stop(BaseException): pass



