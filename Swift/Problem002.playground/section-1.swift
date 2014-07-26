// Playground - noun: a place where people can play

import Cocoa

let sqrt5: Double = sqrt(5)
let phi = (1 + sqrt5)/2 // 1.61803398874989


let upperBound = Int((6*log(10) + log(4) + 1/2*log(5))/log(phi))

func memoize<T:Hashable, U>(body: ((T)->U, T) -> U) -> (T) -> U {
    var memo = Dictionary<T, U>()
    var result: ((T) -> U)!
    
    result = { x in
        if let q = memo[x] { return q }
        let r = body(result, x)
        memo[x] = r
        return r
    }
    return result
}
// Works for n < 94
let fibonacci = memoize { fibonacci, n in n < 2  ? n: fibonacci(n-1) + fibonacci(n-2) }

func problem2() -> Int {
    var sum = 0
    for i in 1...upperBound {
        let n = fibonacci(i+1)
        if n % 2 == 0 {
            sum += n
        }
    }
    return sum
}

println(problem2() == 4613732)