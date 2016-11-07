#encoding=utf8
import numpy as np
#from sklearn.metrics.pairwise import cosine_similarity
from collections import OrderedDict, Counter
from operator import itemgetter
import math

def cosine_similarity(vector1, vector2):
	#print len(vector1), range(len(vector1))
	dot = np.sum([vector1[i] * vector2[i] for i in range(len(vector1))])

	sum_vector1 = 0.0
	sum_vector1 += sum_vector1 + np.sum([vector1[i]*vector1[i] for i in range(len(vector1))])
	norm_vector1 = math.sqrt(sum_vector1)

	sum_vector2 = 0.0
	sum_vector2 += sum_vector2 + np.sum([vector2[i]*vector2[i] for i in range(len(vector2))])
	norm_vector2 = math.sqrt(sum_vector2)

	return dot/(norm_vector1*norm_vector2)

def cal_distance(point1, point2):
	#distance = pow(abs(point1[0] - point2[0]),2) + pow(abs(point1[1]-point2[1]),2)
	distance = cosine_similarity(point1, point2)
	return distance

def load_data():
	points = [[float(eachpoint.split('#')[0]) , float(eachpoint.split('#')[1])] for eachpoint in open('points','r')]
	return points

def threshold(distance):
	if distance < 0.8:
		return True

def distance_point_to_point(points):
	disP2P = {}
	for idx1, point1 in enumerate(points):
		for idx2, point2 in enumerate(points):
			if idx1 < idx2:
				distance = cal_distance(point1, point2)
				disP2P[str(idx1)+'#'+str(idx2)] = distance

	disP2P = OrderedDict(sorted(disP2P.iteritems(), key=itemgetter(1)))
	return disP2P

def agglomerative_cluster(points):
	disP2P = distance_point_to_point(points) #计算点之间距离
	groups = [idx for idx in range(len(points))]

	while True:
		twopoints, distance = disP2P.popitem()
		#print twopoints, distance
		if threshold(distance):
			break
		pointA = int(twopoints.split('#')[0])
		pointB = int(twopoints.split('#')[1])
		pointAGroup = groups[pointA]
		pointBGroup = groups[pointB]

		print twopoints, distance
		if pointAGroup != pointBGroup:
			for idx in range(len(groups)):
				if groups[idx] == pointBGroup:
					groups[idx] = pointAGroup

	return groups

if __name__=='__main__':
	points = load_data() #加载数据
	groups = agglomerative_cluster(points)
	print groups
#	print cosine_similarity([1,0,-1], [-1,-1,0])

