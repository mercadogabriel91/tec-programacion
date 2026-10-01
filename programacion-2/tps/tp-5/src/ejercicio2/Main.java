package ejercicio2;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Agregación: Celular -> Bateria ---");
        Bateria bateriaOriginal = new Bateria("Bata-BT-1", 5000);
        Celular celular = new Celular("555555555555809", "Motorola", "G84", bateriaOriginal);
        System.out.println(celular);

        System.out.println("\n--- La batería existe por fuera del celular ---");
        Bateria bateriaNueva = new Bateria("LA-BATA-2", 6000);
        celular.setBateria(bateriaNueva);
        System.out.println(celular);
        System.out.println("La bateria original sigue existiendo: " + bateriaOriginal);
        celular.setBateria(null);

        System.out.println("\n--- Asociación bidireccional: Celular <-> Usuario ---");
        Usuario usuario = new Usuario("Gabriel Mercado", "55555555");
        usuario.setCelular(celular);
        System.out.println(celular);
        System.out.println(usuario);
        System.out.println("El celular apunta al mismo usuario? " + (celular.getUsuario() == usuario));
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
