persons_preflist = {
    "R":["L","S","Z","D"],
    "J":["S","L","D","Z"],
    "B":["S","D","Z","L"],
    "C":["L","S","Z","D"]

}

pets_preflist = {
    "L":["R","B", "J", "C"],
    "S":["R","B","C","J"],
    "Z":["C","J","R","B"],
    "D":["R","J","C","B"]
}

def gpalgo(nPersons, nPets):
    matches = {}
    unmatchedPersons = []
    for currPerson in persons_preflist:
        matches[currPerson]=None
        unmatchedPersons.append(currPerson)
    for pet in pets_preflist:
        matches[pet]=None

    while len(unmatchedPersons)>0:

        currPerson = unmatchedPersons.pop(0)

        for pet in persons_preflist[currPerson]:
            if matches[pet] == None:
                matches[currPerson]=pet
                matches[pet]=currPerson
                break
            else:
                curPersonPrefIdx = pets_preflist[pet].index(currPerson)
                assignedPerson = matches[pet]
                assignedPersonPrefIdx = pets_preflist[pet].index(assignedPerson)
                if curPersonPrefIdx<assignedPersonPrefIdx:
                    matches[currPerson]=pet
                    matches[pet] = currPerson
                    matches[assignedPerson]=None
                    unmatchedPersons.append(assignedPerson)
                    break
                else:
                    matches[currPerson]=None

    return matches

print(gpalgo(4,4))






