import pygame, tkinter

pygame.init()

from tkinter import messagebox

def show_warning():
    messagebox.showwarning(message="You don't have enough coins!")


def ask_yes_no():
    a = messagebox.askyesno(message="Are you sure?")
    return a




