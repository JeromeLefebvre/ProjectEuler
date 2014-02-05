//
//  main.m
//  ProjectEuler
//
//  Created by Jerome Lefebvre on 14-01-24.
//  Copyright (c) 2014 Jerome Lefebvre. All rights reserved.
//

#import <Foundation/Foundation.h>
#include "sequences.h"

#include "Problem1.h"
#include "Problem2.h"

int main(int argc, const char * argv[])
{
    @autoreleasepool {
        NSLog(Problem1() == 233168 ? @"Problem 1: Good" : @"Problem 1: Bad" );
        NSLog(@"%d", Problem2());
        NSLog(Problem2() == 4613732 ? @"Problem 2: Good" : @"Problem 2: Bad" );
    }
    return 0;
}

