// Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"

let goal = 600851475143
let sqrtgoal:Double = sqrt(600851475143)

func problem3() -> Int {
    var max = 0
    for i in 1..6957 {
        if (goal % i) == 0 && i > max{
            max = i
        }
    }
    return max
}

println(problem3() == 6857)