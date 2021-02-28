const shiftedDiff = (first, second) => {
    // If the params are not passed return not possible
    if (!first || !second){
        return -1
    }
  
    // If they are equal there is no rotation
    if (first === second){
        return 0
    }

    // Mirror the string to get all combinations
    const allCombinations = second + second
    const wordSize = first.length

    // Iter to find the word, if found the index is the number of the rotation
    for (let index = 1; index < wordSize; index++) {
        const currentVariation = allCombinations.substring(index, index + wordSize)
        if (currentVariation === first){
            return index
        }
    }
    
    // returns -1 in case no matches
    return -1
  }


console.log(shiftedDiff("eecoff", "coffee"))