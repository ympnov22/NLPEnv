#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import MeCab
import sys

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

VEC_SIZE = 4

fi_name = sys.argv[1]

if __name__ == "__main__":

    f = open(fi_name,'r')
    
    trainings = [TaggedDocument(words = data.split(),tags = [i]) for i,data in enumerate(f)]
    
    m = Doc2Vec(documents= trainings, dm = 1, vector_size=VEC_SIZE, window=8, min_count=10, workers=4)
    
    m.save("./model/doc2vec.model")
    #m = Doc2Vec.load('./model/doc2vec.model')
    
    """
    for data in m.most_similar(positive=["海外"]):
        print(data[0],end=" ")
        print(data[1])
    """    
    
    print(m.infer_vector(["スピード","は","最大","の","サービス"]))
    print(m.infer_vector(["いま","一歩","踏み","込め"]))
    print(m.infer_vector(["長","たる","もの","は","決断","が","大事"]))
    #print(m.infer_vector(["先","の","先","を","読め"]))
    
    print(m.infer_vector(["私","たち","一人","一人","が","積水","ハウス","です"]))
    print(m.infer_vector(["相手","の","幸せ","を","願う","暖かい","心","で","全て","に","取り","組もう"]))
    print(m.infer_vector(["使命","を","自覚","し","誠実","に","行動","しよう"]))
    
    print(m.infer_vector(["お客様","の","感動","を","生む","高品質","の","商品","サービス","を","提供","します"]))
    print(m.infer_vector(["新たな","視点","で","次代","の","幸福","に","繋がる","仕事","を","創造","します"]))
    print(m.infer_vector(["正々堂々","と","行動","し","社会","に","信頼","される","仕事","を","します"]))
    
    print(m.infer_vector(["昨日","まで","世界","に","なかった","もの","を"]))
    print(m.infer_vector(["住まい","を","通じ","て","安心","で","豊かな","暮らし","を","実現","します"]))
    print(m.infer_vector(["一人","でも","多く","の","お客様","に","1日","でも","早く","快適な","生活","を","お届け","します"]))
   
    print(m.infer_vector(["企業","活動","を","通じ","て","社会的","価値","を","創造","する"]))
    print(m.infer_vector(["積水","を","千仭","の","谿","に","決する","スピード","を","もって","市場","を","変革","する"]))
    print(m.infer_vector(["際立つ","技術","と","品質","で","社会","から","の","信頼","を","獲得","する"]))
    