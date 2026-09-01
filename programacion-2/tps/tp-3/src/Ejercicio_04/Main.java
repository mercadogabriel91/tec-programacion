package Ejercicio_04;

public class Main {
    public static void main() {
        Gallina gallinaA = new Gallina();
        Gallina gallinaB = new Gallina();

        // Encender gallina
        gallinaA.jumpstartChicken();

        // intentar asignar edad negativa
        System.out.println("--- Prueba con edad inválida ---");
        gallinaA.setEdad(-2);
        System.out.println("Edad de gallinaA: " + gallinaA.getEdad());

        // configurar gallinas
        gallinaA.setIdGallina(1);
        gallinaA.setEdad(2);

        gallinaB.setIdGallina(2);
        gallinaB.setEdad(1);

        // simular acciones independientes
        System.out.println("\n--- Simulación de acciones ---");
        gallinaA.ponerHuevo();
        gallinaA.ponerHuevo();
        gallinaB.ponerHuevo();
        gallinaA.envejecer();

        // mostrar estado final de ambas
        System.out.println("\n--- Estado final gallinaA ---");
        gallinaA.mostrarEstado();

        System.out.println("\n--- Estado final gallinaB ---");
        gallinaB.mostrarEstado();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-3/src
 */
