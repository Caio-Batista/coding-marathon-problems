function findRoutes(routes) {
    // Init the auxiliar hashes 
    const countriesCountHash = {}
    const mapRoutes = {}
  
    // Enumarate routes to find the ending point
    // And also to parse the array of routes into an object
    // Start and end are 1
    routes.map(route => {
      const [departure, arrival] = route 
  
      countriesCountHash[arrival] ? 
          ++countriesCountHash[arrival] :
          countriesCountHash[arrival] = 1
  
      countriesCountHash[departure] ? 
          ++countriesCountHash[departure] :
          countriesCountHash[departure] = 1
  
      mapRoutes[departure] = arrival
    })

    // Find the departure and final destination
    const [departure, finalArrival] = findStartingPosition(routes, countriesCountHash)

    // Path starts with the departure
    const completePath = [departure]

    // While not the end country move over
    // to the next route and add the path
    let currentCountry = mapRoutes[departure]
    while (currentCountry !== finalArrival){
      completePath.push(currentCountry)
      currentCountry = mapRoutes[currentCountry]
    }
  
    // Path ends with the final arrival
    completePath.push(finalArrival)

    // Join the path back to a string 
    return completePath.join(', ')

}

// Auxiliar function to find the start and end path
function findStartingPosition(routes, countriesCountHash){
    let start = ''
    let end = ''

    // Iterate over the keys
    // If it only appears once and appears in the
    // Routes departure, it is the start of the path
    // Else we have the end
    Object.keys(countriesCountHash).forEach(element => {
        if (countriesCountHash[element] === 1){
            if(routes.some(route=>route[0] === element)){
                start = element
            } else {
                end = element
            }
        } 
    })

    return [start, end]

}

console.log(findRoutes([["MNL", "TAG"], ["CEB", "TAC"], ["TAG", "CEB"], ["TAC", "BOR"]]))

console.log(findRoutes([
    ["Chicago", "Winnipeg"],
    ["Halifax", "Montreal"],
    ["Montreal", "Toronto"],
    ["Toronto", "Chicago"],
    ["Winnipeg", "Seattle"]
]))

console.log(findRoutes([
    ["Chicago", "Winnipeg"],
    ["Halifax", "Montreal"],
    ["Montreal", "Toronto"],
    ["Toronto", "Chicago"],
    ["Winnipeg", "Seattle"]
]))