from sys import argv
import numpy
import math
import random
import argparse
import cv2
import numba
from numba import jit , cuda
from numba import njit

#@jit(parallel=True)
def get_centroids(img,k,cent):
    for i in range(k):
        y=random.randrange(len(img))
        x=random.randrange(len(img[0]))
        point=(img[y][x][0],img[y][x][1],img[y][x][2])
        cent.append(point)
    #print(numba.typeof(cent))

#@jit('void(uint8[:,:,:],int32[:,:,:])')
def pixelsPass(imgR,res):
    for y in range(len(res)):
        for x in range(len(res[0])):
            imgR[x][y]=res[y][x]

def argmindistance(pixel,cent):
    distance=[]
    for c in cent:
        distance.append(math.sqrt((c[0]-pixel[0])**2+(c[1]-pixel[1])**2+(c[2]-pixel[2])**2))
    minindex=numpy.argmin(distance)
    clusters[minindex].append(pixel)
    return minindex

#@jit(parallel=True)
#@jit('void(uint8[:,:])',parallel=True)
def getAverageRGB(arr):
    r=0
    g=0
    b=0
    counter=len(arr)
    for x in xrange(len(arr)):
        r+=arr[x][0]
        g+=arr[x][1]
        b+=arr[x][2]
    rAvg= r/counter
    gAvg= g/counter
    bAvg= b/counter
    return (rAvg,gAvg,bAvg)

def kmeans(img,k):
    h=len(img)
    w=len(img[0])
    centroids=[]
    #print(numba.typeof(img),numba.typeof(k),numba)
    get_centroids(img,k,centroids)
    oldcentroids=[[] for i in xrange(k)]
    labels=numpy.zeros((h,w))
    while not(centroids==oldcentroids):
        print(centroids,oldcentroids)
        for y in xrange(h):
            for x in xrange(w):
                #arr=numpy.array(centroids[0],centroids[1],centroids[2],)
                #print(numba.typeof(img[y][x]),numba.typeof(arr))
                labels[y][x]=argmindistance(img[y][x],centroids)
        index=0
        #print(numba.typeof(clusters))
        for cluster in clusters:
            if (len(cluster)!=0):
                oldcentroids[index]=centroids[index]
                cluster=numpy.array(cluster)
                #print(numba.typeof(cluster))
                centroids[index]=getAverageRGB(cluster)
                index+=1
    centers=numpy.array(centroids)
    labels=numpy.transpose(numpy.uint8(labels))
    res=centers[labels]
    #print(res)
    #print("\n\n\n")
    #print(img)
    #cv2.imshow('imag2',res)
    img2=numpy.copy(img)
    #print(numba.typeof(img2),numba.typeof(res))
    pixelsPass(img2,res)
    cv2.imshow('image',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("lena.png")
#print(img)
K=10
global clusters
clusters= [[] for i in range(K)]
kmeans(img,K)
