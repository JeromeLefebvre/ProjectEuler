// Playground - noun: a place where people can play

import Cocoa
import Foundation

extension String {
    subscript (r: Range<Int>) -> String {
        get {
            return self.substringWithRange(
                Range(start: advance(self.startIndex, r.startIndex),
                    end: advance(self.startIndex, r.endIndex)))
        }
    }
}


var s = "一人"

println(s[0..1]) // 一
println(s[1..2]) // 人