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
A classe Input está definida aqui.
"""

import pygame
import mindu



class Input(object):
    """
    Classe de base dos dispositivos de entrada.
    """

    __slots__ = ()



    def _update(self):
        self._ding = []
        self._dong = []

        for (id, bool) in enumerate(self._busy):

            if bool:

                if not self._old_busy[id]: self._ding.append(id)

                else: self._time[id] += (1000 // mindu.loop._ips)

            elif self._old_busy[id]:
                self._dong.append(id)
                self._time[id] = 0

        if self._on_ding is not None:
            for id in self._ding:
                symbol = self._symbols.get(id, 'unknow symbol')
                self._on_ding(symbol, *self._on_ding_pargs, **self._on_ding_kwargs)

        if self._on_dong is not None:
            for id in self._dong:
                symbol = self._symbols.get(id, 'unknow symbol')
                self._on_dong(symbol, *self._on_dong_pargs, **self._on_dong_kwargs)



    def get_symbols(self):
        """
        get_symbols() -> tuple

        Obtém os símbolos do dispositivo de entrada.
        """

        return tuple([key for key in self._symbols.keys() if isinstance(key, str)])



    def ding(self, symbol):
        """
        ding(symbol) -> bool

        Verifica se o símbolo dado tornou-se ocupado.

        O argumento "symbol" é uma string representando um símbolo do
        dispositivo de entrada. Para conhecer os símbolos válidos, use o método
        get_symbols().
        """

        if not isinstance(symbol, str):
            raise TypeError('ding(): o argumento "symbol" precisa ser string')

        if symbol not in self._symbols:
            raise ValueError('ding(): símbolo inválido: "{}"'.format(symbol))

        return self._symbols[symbol] in self._ding



    def dong(self, symbol):
        """
        dong(symbol) -> bool

        Verifica se o símbolo dado tornou-se desocupado.

        O argumento "symbol" é uma string representando um símbolo do
        dispositivo de entrada. Para conhecer os símbolos válidos, use o método
        get_symbols().
        """

        if not isinstance(symbol, str):
            raise TypeError('dong(): o argumento "symbol" precisa ser string')

        if symbol not in self._symbols:
            raise ValueError('dong(): símbolo inválido: "{}"'.format(symbol))

        return self._symbols[symbol] in self._dong



    def busy(self, symbol):
        """
        busy(symbol) -> bool

        Verifica se o símbolo dado está ocupado.

        O argumento "symbol" é uma string representando um símbolo do
        dispositivo de entrada. Para conhecer os símbolos válidos, use o método
        get_symbols().
        """

        if not isinstance(symbol, str):
            raise TypeError('busy(): o argumento "symbol" precisa ser string')

        if symbol not in self._symbols:
            raise ValueError('busy(): símbolo inválido: "{}"'.format(symbol))

        return bool(self._busy[self._symbols[symbol]])



    def time(self, symbol):
        """
        time(symbol) -> int

        Verifica há quantos milissegundos o símbolo dado está ocupado.

        O argumento "symbol" é uma string representando um símbolo do
        dispositivo de entrada. Para conhecer os símbolos válidos, use o método
        get_symbols().
        """

        if not isinstance(symbol, str):
            raise TypeError('time(): o argumento "symbol" precisa ser string')

        if symbol not in self._symbols:
            raise ValueError('time(): símbolo inválido: "{}"'.format(symbol))

        return self._time[self._symbols[symbol]]



    def get(self):
        """
        get() -> str ou None

        Obtém o símbolo do dispositivo de entrada que tornou-se ocupado. Retorna
        None se nenhum símbolo tornou-se ocupado.
        """

        if self._ding: return self._symbols.get(self._ding[0], 'unknow symbol')



    def on_ding(self, callable, *pargs, **kwargs):
        """
        on_ding(callable, *pargs, **kwargs) -> callable

        Registra o objeto chamável dado, para que seja chamado sempre que um
        símbolo do dispositivo de entrada se torna ocupado. O objeto chamável
        precisa suportar chamadas com pelo menos 1 argumento, para receber o
        símbolo que se torna ocupado.

        O argumento "callable" é o objeto chamável a ser registrado. Pode ser
        None, para que nenhum objeto chamável fique registrado.

        Os argumentos posicionais e de palavra-chave opcionais "*pargs" e
        "**kwargs" serão repassados ao objeto chamável a cada chamada.

        Note que o mesmo objeto chamável dado é retornado de volta para
        facilitar o uso deste método como um decorador.
        """

        self._on_ding = callable
        self._on_ding_pargs = pargs
        self._on_ding_kwargs = kwargs

        return callable



    def on_dong(self, callable, *pargs, **kwargs):
        """
        on_dong(callable, *pargs, **kwargs) -> callable

        Registra o objeto chamável dado, para que seja chamado sempre que um
        símbolo do dispositivo de entrada se torna desocupado. O objeto chamável
        precisa suportar chamadas com pelo menos 1 argumento, para receber o
        símbolo que se torna desocupado.

        O argumento "callable" é o objeto chamável a ser registrado. Pode ser
        None, para que nenhum objeto chamável fique registrado.

        Os argumentos posicionais e de palavra-chave opcionais "*pargs" e
        "**kwargs" serão repassados ao objeto chamável a cada chamada.

        Note que o mesmo objeto chamável dado é retornado de volta para
        facilitar o uso deste método como um decorador.
        """

        self._on_dong = callable
        self._on_dong_pargs = pargs
        self._on_dong_kwargs = kwargs

        return callable



