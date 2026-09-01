package Ejercicio_05;

public class Main {
    public static void main() {
        NaveEspacial nave = new NaveEspacial();
        nave.setNombre("Terminus Est");
        nave.setCombustible(50);

        System.out.println("--- Estado inicial ---");
        nave.mostrarEstado();

        // intentar avanzar por sobre el limite  (30 km = 60 unidades)
        System.out.println("\n--- Intento de avance sin combustible suficiente ---");
        nave.avanzar(30);

        // intentar recargar demas
        System.out.println("\n--- Intento de recarga que supera el máximo ---");
        nave.recargarCombustible(60);

        // avance joya
        System.out.println("\n--- Avance exitoso ---");
        nave.avanzar(10);

        System.out.println("\n--- Estado final ---");
        nave.mostrarEstado();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-3/src
 */
