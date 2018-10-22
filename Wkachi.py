#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab
import sys
    
if __name__ == "__main__":
    fi_name = sys.argv[1] 
    fo_name = "w_" + fi_name
    
    m = MeCab.Tagger ("-Owakati")
    
    fi = open(fi_name,'r')
    fo = open(fo_name,'a')
    
    for line in fi:
        words = m.parse(line)
        words = words.rstrip('\n')
        fo.write(words)
        fo.write("\n")
    
    fi.close()
    fo.close()