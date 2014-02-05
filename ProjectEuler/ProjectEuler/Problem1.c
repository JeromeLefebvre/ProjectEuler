//
//  Problem1.c
//  ProjectEuler
//
//  Created by Jerome Lefebvre on 14-01-24.
//  Copyright (c) 2014 Jerome Lefebvre. All rights reserved.
//

#include <stdio.h>
#include "sequences.h"

int Problem1() {
    int GOAL = 1000 - 1;
	int multiplesOf3 = 3*triangle(GOAL/3);
    int multiplesOf5 = 5*triangle(GOAL/5);
    int multiplesOf15 = 15*triangle(GOAL/15);
    return multiplesOf3 + multiplesOf5 - multiplesOf15;
}