'''Faca um programa em Python que abra e reproduza o audio de um arquivo MP3.'''

import pygame

pygame.mixer.init()
pygame.mixer.music.load('Flores.mp3')
pygame.mixer.music.play()
pygame.event.wait()
