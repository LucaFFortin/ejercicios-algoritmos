import pascalTriangle from "./pascal.js"
import { test, describe, mock } from "node:test"
import assert from "node:assert"

describe("Deberia de aceptar solo numeros", async () => {
    test("Deberia de rechazar si level es texto", async () => {
        // usamos mocks para capturar las salidas por consola
        const logMocks = mock.method(console, "log", () => { })

        // usamos la funcion con un argumento de texto
        pascalTriangle("1")

        // nos fijamos que mocks haya capturado correctamente la salida y que sea la salida esperada
        assert.strictEqual(logMocks.mock.calls.length, 1)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "El parametro level tiene que ser un numero")


        // limpiamos el almacen de mocks
        logMocks.mock.restore()
    })

    test("Deberia de rechazar si level es array", async () => {
        const logMocks = mock.method(console, "log", () => { })

        pascalTriangle("1")

        assert.strictEqual(logMocks.mock.calls.length, 1)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "El parametro level tiene que ser un numero")

        logMocks.mock.restore()
    })
})

describe("Deberia cortar la ejecucion si level es menor a 0", async () => {
    test("Deberia de rechazar si level es menor que 0", async () => {
        const logMocks = mock.method(console, "log", () => { })

        pascalTriangle(-1)

        assert.strictEqual(logMocks.mock.calls.length, 1)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "El nivel ingresado es imposible de calcular")

        logMocks.mock.restore()
    })

    test("Deberia de rechazar si level es igual a 0", async () => {
        const logMocks = mock.method(console, "log", () => { })

        pascalTriangle(0)

        assert.strictEqual(logMocks.mock.calls.length, 1)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "El nivel ingresado es imposible de calcular")

        logMocks.mock.restore()
    })
})

describe("Deberia de cortar la ejecucion si level es mayor que 25", async () => {
    test("Deberia de rechazar si level es 26", async () => {
        const logMocks = mock.method(console, "log", () => { })

        pascalTriangle(26)

        assert.strictEqual(logMocks.mock.calls.length, 1)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "El nivel excede el limite de 25, la ejecucion se cancelo")

        logMocks.mock.restore()
    })
})

// caso 1, 2, funcional y 25 

describe("Deberia de funcionar bien los casos base", async () => {
    test("Deberia de funcionar si level es 1", async () => {
        const logMocks = mock.method(console, "log", () => { })

        const level = pascalTriangle(1)

        assert.strictEqual(logMocks.mock.calls.length, 1)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "1")
        
        logMocks.mock.restore()
    })

    test("Deberia de funcionar si level es 2", async () => {
        const logMocks = mock.method(console, "log", () => { })

        const level = pascalTriangle(2)

        assert.strictEqual(logMocks.mock.calls.length, 2)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "1")
        assert.strictEqual(logMocks.mock.calls[1].arguments[0], "1 1")
        
        logMocks.mock.restore()
    })
})

describe("Deberia de crear correctamente el triangulo de pascal", async () => {
    test("Deberia de crear correctamente el triangulo de 3 niveles", async () => {
        const logMocks = mock.method(console, "log", () => { })

        pascalTriangle(3)

        assert.strictEqual(logMocks.mock.calls.length, 3)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "1")
        assert.strictEqual(logMocks.mock.calls[1].arguments[0], "1 1")
        assert.strictEqual(logMocks.mock.calls[2].arguments[0], "1 2 1")

        logMocks.mock.restore()
    })

    test("Deberia de crear correctamente el triangulo de 5 niveles", async () => {
        const logMocks = mock.method(console, "log", () => { })

        pascalTriangle(5)

        assert.strictEqual(logMocks.mock.calls.length, 5)
        assert.strictEqual(logMocks.mock.calls[0].arguments[0], "1")
        assert.strictEqual(logMocks.mock.calls[1].arguments[0], "1 1")
        assert.strictEqual(logMocks.mock.calls[2].arguments[0], "1 2 1")
        assert.strictEqual(logMocks.mock.calls[3].arguments[0], "1 3 3 1")
        assert.strictEqual(logMocks.mock.calls[4].arguments[0], "1 4 6 4 1")

        logMocks.mock.restore()
    })
})