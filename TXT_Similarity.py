# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/6/15 17:08 
# ide： PyCharm
# coding: utf-8
from gensim import corpora,models,similarities
import jieba
from collections import defaultdict
#  1.读取文档
doc1 = "D:\\作业\\测试\\1.txt"
doc2 = "D:\\作业\\测试\\2.txt"
d1 = open(doc1,encoding="gb2312").read()
d2 = open(doc2,encoding="gb2312").read()
#  2.对要计算的多篇文档进行分词
data1 = jieba.cut(d1)
data2 = jieba.cut(d2)
#   3.对文档进行整理成指定格式，方便后续计算

data11 = ""
for item in data1:
    data11+=item+" "

data22 = ""
for item in data2:
    data22+=item+" "

documents = [data11,data22]
#  4.计算出词语的频率
texts = [[word for word in document.split()]
        for document in documents]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1

#  5.对可选、低频词进行过滤
texts = [[word for word in text if frequency[token]>1000]
 for text in texts]              #从右往左读

#  6.通过语料库建立词典
dictionary = corpora.Dictionary(texts)
dictionary.save("D:\\作业\\测试\\1.txt")

#  7.加载要对比的文档
doc3 = "D:\\作业\\测试\\3.txt"
d3 = open(doc3,encoding="gb2312").read()

#  8.将要对比的文档通过doc2bow转化为稀疏向量
data3 = jieba.cut(d3)
data33 = ""
for item in data3:
    data33+=item+""
new_doc = data33
new_vec = dictionary.doc2bow(new_doc.split())  #  得到稀疏向量
corpus = [dictionary.doc2bow(text) for text in texts]

#  10.通过TF-idf模型对新语料库处理，得到tfidf
tfidf = models.TfidfModel(corpus)

#  11.通过token2id得到特征数
featureNum = len(dictionary.token2id.keys())

#  12.计算稀疏矩阵相似度，从而建立索引
index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim = index[tfidf[new_vec]]
print(sim)

