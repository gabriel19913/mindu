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
A classe Channel está definida aqui.
"""

import pygame
import mindu



class Channel(object):
    """
    Objeto para representar canais de som.
    """

    __slots__ = ('_pygame_channel',)



    def __init__(self, id): self._pygame_channel = pygame.mixer.Channel(id)



    def play(self, sound, loops = 0, maxtime = 0, fadein = 0):
        """
        play(sound, loops = 0, maxtime = 0, fadein = 0) -> None

        Inicia a reprodução de som no canal.

        O argumento "sound" é um objeto Sound, representando o som a ser
        reproduzido.

        O argumento "loops" é um inteiro representando quantas vezes o som deve
        se repetir automaticamente depois de tocar a primeira vez. Por exemplo,
        1 fará com que o som seja reproduzido 2 vezes ao todo. Para que o som se
        repita indefinidamente, use -1.

        O argumento "maxtime" é um inteiro indicando após quantos milissegundos
        o som deve ser interrompido automaticamente. Se for 0, o som será
        reproduzido até o fim.

        O argumento "fadein" é um inteiro representando quantos milissegundos
        deve levar para o volume total ser atingido na reprodução do som,
        iniciando em mudo. Se for 0, por exemplo, a reprodução já inicia no
        volume total; se for 1000, a reprodução começa no mudo e o volume é
        aumentado automaticamente e de forma gradual, de modo que em 1000
        milissegundos o volume total é atingido.
        """

        if not mindu.loop._running:
            raise mindu.Error('play(): método chamado com o loop interno do Mindu parado')

        if not isinstance(sound, mindu.Sound):
            raise TypeError('play(): o argumento "sound" precisa ser um objeto Sound')

        if not isinstance(loops, int):
            raise TypeError('play(): o argumento "loops" precisa ser inteiro')

        if loops < -1:
            raise ValueError('play(): o argumento "loops" precisa ser maior ou igual a -1')

        if not isinstance(maxtime, int):
            raise TypeError('play(): o argumento "maxtime" precisa ser inteiro')

        if maxtime < 0:
            raise ValueError('play(): o argumento "maxtime" precisa ser maior ou igual a 0')

        if not isinstance(fadein, int):
            raise TypeError('play(): o argumento "fadein" precisa ser inteiro')

        if fadein < 0:
            raise ValueError('play(): o argumento "fadein" precisa ser maior ou igual a 0')

        self._pygame_channel.play(sound._pygame_sound, loops, maxtime, fadein)



    def stop(self):
        """
        stop() -> None

        Interrompe a reprodução de som no canal.
        """

        self._pygame_channel.stop()



    def pause(self):
        """
        pause() -> None

        Pausa a reprodução de som no canal.
        """

        self._pygame_channel.pause()



    def unpause(self):
        """
        unpause() -> None

        Retoma a reprodução de som no canal, no ponto onde foi pausada.
        """

        self._pygame_channel.unpause()



    def fadeout(self, time):
        """
        fadeout(time) -> None

        Reduz o volume da reprodução de som automaticamente e de forma gradual.
        A reprodução é interrompida quando se torna muda.

        O argumento "time" é um inteiro representando quantos milissegundos deve
        levar para a reprodução emudecer.
        """

        if not isinstance(time, int):
            raise TypeError('fadeout(): o argumento "time" precisa ser inteiro')

        if time <= 0:
            raise ValueError('fadeout(): o argumento "time" precisa ser maior que 0')

        self._pygame_channel.fadeout(time)



    def busy(self):
        """
        busy() -> bool

        Verifica se o canal está reproduzindo som.
        """

        return bool(self._pygame_channel.get_busy())



    def get_sound(self):
        """
        get_sound() -> Sound ou None

        Obtém o som que estiver sendo reproduzido no canal ou None.
        """

        pygame_sound = self._pygame_channel.get_sound()

        if pygame_sound is not None:
            return pygame_sound._mindu_sound



    def queue(self, sound):
        """
        queue(sound) -> None

        Coloca um som na fila de reprodução do canal. O som será reproduzido
        automaticamente assim que a reprodução atual chegar ao fim.

        O argumento "sound" é um objeto Sound representando o som a ser
        enfileirado.
        """

        if not mindu.loop._running:
            raise mindu.Error('queue(): método chamado com o loop interno do Mindu parado')

        if not isinstance(sound, mindu.Sound):
            raise TypeError('queue(): o argumento "sound" precisa ser um objeto Sound')

        self._pygame_channel.queue(sound._pygame_sound)



    def get_queue(self):
        """
        get_queue() -> Sound ou None

        Obtém o som que estiver na fila de reprodução do canal ou None.
        """

        pygame_sound = self._pygame_channel.get_queue()

        if pygame_sound is not None:
            return pygame_sound._mindu_sound



    def get_volume(self):
        """
        get_volume() -> float

        Verifica o volume do canal.
        """

        return self._pygame_channel.get_volume()



    def set_volume(self, volume):
        """
        set_volume(volume) -> None

        Define o volume do canal.

        O argumento "volume" é um float representando o volume do canal. Se for
        menor que 0.0, será arredondado para 0.0, e se for maior que 1.0, será
        arredondado para 1.0.
        """

        if not isinstance(volume, float):
            raise TypeError('set_volume(): o argumento "volume" precisa ser float')

        if volume > 1.0: volume = 1.0

        elif volume < 0.0: volume = 0.0

        self._pygame_channel.set_volume(volume)



