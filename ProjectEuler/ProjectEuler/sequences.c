//
//  sequences.c
//  ProjectEuler
//
//  Created by Jerome Lefebvre on 14-01-24.
//  Copyright (c) 2014 Jerome Lefebvre. All rights reserved.
//

#include <stdio.h>
#include <math.h>

int triangle(int n){
    return n*(n+1)/2;
}

//phi = (1 + 5**(1/2))/2

int fib(int n){
    // The modern sequence: 0,1,1,2,3,5,8,13,21
    float phi = (1 + sqrt(5))/2;
    float psi = 1- phi;
    float fib = (pow(phi,n) - pow(psi,n))/sqrt(5);
    return (int) fib;
}

int Fib(int n){
    // The project Euler fib sequence
    return fib(n+2);
}