# Conversor Decimal <--> Binario

Trabajo práctico integrador de Matemática 1.

Programa de consola en Python que convierte números enteros de decimal a binario y de binario a decimal,
mostrando el procedimiento paso a paso:

- **Decimal -> Binario:** divisiones sucesivas entre 2, leyendo los restos de abajo hacia arriba.
- **Binario -> Decimal:** suma de cada bit multiplicado por su potencia de 2.

Además valida la entrada y muestra un mensaje de error si el dato ingresado invalido (por ejemplo, letras, numeros con decimales o binarios con digitos distintos de 0 y 1).

## Como se usa?

### Requisitos

- Python 3.
- No requiere librerías externas ni nada extra.

### Ejecutar el programa

Desde la carpeta del proyecto:

```bash
python3 main.py
```

Al iniciar aparece el menú principal:

```
*******************************************
   CONVERSOR DECIMAL <-> BINARIO
*******************************************
 1. DE: Decimal A: Binario
 2. DE: Binario A: Decimal
 0. Salir

Elija una opción:
```

Se escribe el número de la opción y se presiona Enter. Después de cada conversión el menú vuelve a aparecer, así que se pueden hacer varias conversiones seguidas.

### Opción 1: Decimal a Binario

Pide un número entero en base 10 y muestra las divisiones sucesivas entre 2. El resultado se arma leyendo los restos de abajo hacia arriba.

Ejemplo ingresando `13`:

```
Elija una opción: 1
Ingrese un numero decimal entero: 13

Divisiones sucesivas entre 2:
          13 / 2 = 6          resto 1
           6 / 2 = 3          resto 0
           3 / 2 = 1          resto 1
           1 / 2 = 0          resto 1
  (se leen los restos de abajo hacia arriba)

Resultado: 13 (decimal) = 1101 (binario)
```

### Opción 2: Binario a Decimal

Pide un número formado solo por `0` y `1`, y muestra cuánto aporta cada bit según su posición (potencia de 2). El resultado es la suma de todos esos valores.

Ejemplo ingresando `1101`:

```
Elija una opción: 2
Ingrese un número binario: 1101

Suma de potencias de 2:
  1 x 2^3   = 8
  1 x 2^2   = 4
  0 x 2^1   = 0
  1 x 2^0   = 1
  (8 + 4 + 0 + 1) = 13

Resultado: 1101 (binario) = 13 (decimal)
```

### Opción 0: Salir

Termina el programa. También se puede salir en cualquier momento con `Ctrl + C`.

### Qué datos acepta

| Opción | Acepta | Ejemplos válidos |
|---|---|---|
| Decimal -> Binario | Números enteros, positivos o negativos | `13`, `0`, `-6`, `+7` |
| Binario -> Decimal | Solo dígitos `0` y `1`, opcionalmente con signo | `1101`, `0011`, `-110` |

Los espacios al principio y al final se ignoran. Los números negativos se convierten igual que los positivos y se les agrega el signo `-` al resultado (por ejemplo, `-6` -> `-110`).

### Mensajes de error

Si el dato ingresado no es válido, el programa muestra un error y vuelve al menú, sin cerrarse:

| Si se ingresa... | Mensaje |
|---|---|
| Letras en un decimal (`hola`) | `'hola' no es un número decimal válido. Caracteres no permitidos: a h l o` |
| Un número con decimales (`3.5` o `3,5`) | `Solo se admiten numeros enteros sin la coma o puntos decimales.` |
| Nada (Enter vacío) en un decimal | `No podes meter un input vacio.` |
| Nada (Enter vacío) en un binario | `Necesitas ingresar algún valor.` |
| Un dígito distinto de 0 y 1 en un binario (`1021`) | `'1021' no es un número binario: solo puede tener 0 y 1. Caracteres no permitidos: 2` |
| Solo un signo (`-`) | `Falta el número después del signo.` |
| Una opción que no existe en el menú (`5`) | `'5' no es una opción válida. Elija 1, 2 o 0.` |

### Estructura del proyecto

- `main.py`: el menú y la interacción con el usuario (lo que se ejecuta).
- `conversor.py`: la lógica de las conversiones y la validación de los datos ingresados.
