package ejercicio2;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Array de figuras (polimorfismo) ---");
        Figura[] figuras = {
                new Circulo("Círculo A", 3),
                new Rectangulo("Rectángulo B", 4, 5),
                new Circulo("Círculo C", 1.5),
                new Rectangulo("Rectángulo D", 2, 8)
        };

        for (Figura figura : figuras) {
            System.out.println(figura.getNombre() + " | área: " + String.format("%.2f", figura.calcularArea()));
        }
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-7/src
 */
