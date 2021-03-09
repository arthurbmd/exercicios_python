# faça um programa em python que abra e reproduza o audio de um arquivo MP3

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('02. Unsainted.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Você está ouvindo!')
