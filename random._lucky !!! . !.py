# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:46:41 2021

@author: θανάσης Λάππας
title: random_lucky ;_ :: P [
    ]
"""
import sympy
import random

limit= float(input("guess a number"))
result =random.randint(-limit*(round(limit)),(round(limit)))
print("resulting number", result)