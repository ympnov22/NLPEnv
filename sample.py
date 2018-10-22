#!/usr/bin/python
#-*- coding:utf-8 -*-

import MeCab
m = MeCab.Tagger ("-Ochasen")
print(m.parse ("すもももももももものうち"))