package ejercicio7;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Agregación: Vehiculo -> Motor ---");
        Motor motorOriginal = new Motor("Nafta 1.6", "MTR-44821");
        Vehiculo vehiculo = new Vehiculo("ABC123", "Peugeot 208", motorOriginal);
        System.out.println(vehiculo);

        System.out.println("\n--- Cambio de motor: el anterior sigue existiendo ---");
        Motor motorNuevo = new Motor("Nafta 1.6 THP", "MTR-90310");
        vehiculo.setMotor(motorNuevo);
        System.out.println(vehiculo);
        System.out.println("Motor retirado: " + motorOriginal);

        System.out.println("\n--- Asociación bidireccional: Vehiculo <-> Conductor ---");
        Conductor conductor = new Conductor("Gabriel Mercado", "AA-55555555");
        vehiculo.setConductor(conductor);
        System.out.println(vehiculo);
        System.out.println(conductor);
        System.out.println("El conductor apunta al mismo vehículo? " + (conductor.getVehiculo() == vehiculo));
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
