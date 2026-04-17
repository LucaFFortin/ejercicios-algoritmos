/**
 * Funcion para calcular el triangulo de pascal.
 * Pasado un cierto level, calculara siempre y cuando level sea un numero entre 0 a 25
 * 
 * @param {number} level 
 * @returns {void}
 */
export default function pascalTriangle(level = 2) {
    if (typeof level !== "number") {
        console.log("El parametro level tiene que ser un numero")
        return
    }

    if (level <= 0) {
        console.log("El nivel ingresado es imposible de calcular")
        return
    }

    if (level > 25) {
        console.log("El nivel excede el limite de 25, la ejecucion se cancelo")
        return
    }

    const firstLevel = [1]
    const secondLevel = [1, 1]
    let prevLevel = secondLevel

    printLevel(firstLevel)
    if (level <= 1) return "1"

    printLevel(secondLevel)
    if (level <= 2) return "1 1"

    for (let i = 0; i < level - 2; i++) {
        const currLevel = calculateLevel(prevLevel)
        printLevel(currLevel)
        prevLevel = currLevel
    }
}

// imprime el nivel con numeros espaciados
function printLevel(level) {
    console.log(level.join(" ").toString())
}

// calcula en nivel segun el nivel previo
function calculateLevel(prevLevel) {
    const level = []

    for (let i = 0; i <= prevLevel.length; i++) {
        const curr = prevLevel[i] || undefined
        const prev = prevLevel[i - 1] || undefined

        // en la primera iteracion no hay anterior, asi que solo le ponemos el valor actual = 1
        if (!prev) {
            level.push(curr)

            // en la ultima iteracion no hay un valor actual, asi que solo le ponemos el valor anterior = 1
        } else if (!curr) {
            level.push(prev)

            // calculamos el valor con el numero actual y el previo.
        } else {
            const sum = curr + prev
            level.push(sum)
        }

    }

    level.push[1]
    return level
}
