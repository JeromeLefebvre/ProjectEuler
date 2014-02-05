//
//  Problem2.c
//  ProjectEuler
//
//  Created by Jerome Lefebvre on 14-01-24.
//  Copyright (c) 2014 Jerome Lefebvre. All rights reserved.
//

#include <stdio.h>
#include "sequences.h"
#include <math.h>

long Problem2(){
    long total = 0;
    int n = 0;
    int max = 5000000;
    printf("%d \n", max);
    int F = 0;
    while (F < 4000000) {
        if (F % 2 == 0) {
            total += F;
            //printf("%d \n", total);
        }
        n++;
        F = Fib(n);
    }
    return 4*total;
}