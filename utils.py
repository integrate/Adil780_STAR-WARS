import pygame, tkinter

pygame.init()

from tkinter import messagebox

def show_warning():
    messagebox.showwarning(message="You don't have enough coins!")


def ask_yes_no(message):
    a = messagebox.askyesno(message=message)
    return a





