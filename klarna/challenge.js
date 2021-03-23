function pathsToTopRight(A, B){
    let count = 0
    if (A.x === B.x){
        return 1
    } else if (A.y === B.y) {
        return 1
    } else {
        count += pathsToTopRight({x:A.x + 1, y: A.y},B)
        count += pathsToTopRight({x:A.x, y: A.y+ 1},B)
    }

    return count
}

console.log(pathsToTopRight({ x:1 , y:1 }, { x:2, y:3 }))
console.log(pathsToTopRight({ x:1 , y:1 }, { x:3, y:3 }))