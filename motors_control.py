#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# Подготавливаем пины GPIO.
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

# Включаем вращение двигателя 1 в одну сторону.
GPIO.output(4, GPIO.HIGH)

# ждем 5 секунд.
time.sleep(5)

# Выключаем двигатель 1.
GPIO.output(4, GPIO.LOW)