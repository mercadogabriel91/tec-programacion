package ejercicio12;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Asociación unidireccional: Impuesto -> 'Contribuyente' ---");
        Contribuyente contribuyente = new Contribuyente("Gabriel Mercado", "20-55555555-3");
        Impuesto impuesto = new Impuesto(85000, contribuyente);
        System.out.println(impuesto);

        System.out.println("\n--- Dependencia de uso: Calculadora.calcular(Impuesto) ---");
        Calculadora calculadora = new Calculadora();
        calculadora.calcular(impuesto);
        calculadora.calcular(null); // caso imaginario
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
