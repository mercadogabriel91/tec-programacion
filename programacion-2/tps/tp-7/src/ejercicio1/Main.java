package ejercicio1;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Auto: herencia y mostrarInfo sobrescrito ---");
        Auto auto = new Auto("Toyota", "Hilux", 4);
        auto.mostrarInfo();

        System.out.println("\n--- Upcasting: el auto también es un Vehículo ---");
        Vehiculo vehiculo = auto;
        vehiculo.mostrarInfo();
        System.out.println(auto);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-7/src
 */
