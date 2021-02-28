function orderWeight(strng) {
    // Create hash and array of numbers from input
    const allWeightsHash = {}
    const weights = strng.split(" ")

    // If none or one number then return the same input
    if (weights.length <= 1 ){
        return strng
    }
    
    // Change in place the numbers to weights and to each weight found populate hash
    weights.map((element, index, thisArray) => {

        // Convert to number and sum digits
        const currentWeigth =
            element
            .split('')
            .reduce((firstElement, secondElement) => +firstElement + +secondElement, 0)

        // Add to hash, if already found return 
        allWeightsHash[currentWeigth] ? 
            allWeightsHash[currentWeigth].push(+element) :
            allWeightsHash[currentWeigth] = [+element]

        // Modify the current array
        thisArray[index] = currentWeigth
    })
    
    // Sorting the array of weights
    weights.sort((first, second) => first - second)
    
    // Replacing the weights now with the old number values but in order
    weights.map((element, index, thisArray) => {
        if (allWeightsHash[element].length > 1){
            allWeightsHash[element].sort()
        }

        const currentMinElement = allWeightsHash[element][0]

        // Removes the min element from the inner array in hash
        allWeightsHash[element].splice(0, 1)

        // Modify the current array
        thisArray[index] = currentMinElement
    })

    // Converting the array into string
    return weights.join(' ')
}



console.log(orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123")) // "11 11 2000 10003 22 123 1234000 44444444 9999"