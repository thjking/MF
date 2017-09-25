# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:45:10 2017

@author: Acer
"""
import numpy

def matrix_factorization(R, P, Q, K, steps=20000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in xrange(steps):
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - \
                         beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - \
                         beta * Q[k][j])
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]),2)
                    for k in xrange(K):
                        e = e + (beta / 2) * (pow(P[i][k],2) + pow(Q[k][j],2))
                        
        print e,step
        if e < 1.1:
            return P,Q.T
            break

R = numpy.array([[5,3,0,1],
                [4,0,0,1],
                [1,0,0,4],
                [0,1,5,4],
                [0,1,5,4]])

N = len(R)
M = len(R[0])
K = 2
P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)

nP,nQ = matrix_factorization(R,P,Q,K)
nR = numpy.dot(nP,nQ.T)
print nR