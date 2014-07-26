
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

import Cocoa

log(5)
//upperBound = int((6*log(10) + log(4) + 1/2*log(5))/log(phi))


func problem2() -> Int {
    var sum = 0
    for i in 1...upperBound {
        let n = fibonacci(i+1)
        if n % 2 == 0 {
            sum += n
        }
    }
    return sum
//    return sum([fib(i+1) for i in range(1,upperBound+1) if fib(i+1)%2 == 0])
}

problem2()