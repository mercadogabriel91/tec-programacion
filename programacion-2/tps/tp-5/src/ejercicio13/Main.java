package ejercicio13;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Dependencia de creación: GeneradorQR.generar(String, Usuario) ---");
        Usuario usuario = new Usuario("Gabriel Mercado", "gabriel@algunmail.com");
        GeneradorQR generador = new GeneradorQR();
        generador.generar("https://mi-servicio-de-pago/cobro/8812", usuario);
        generador.generar("https://mi-servicio-de-pago/cobro/8813", usuario);

        System.out.println("\n--- Validación ---");
        generador.generar("   ", usuario); // Tira un error xq no puede estar vacio
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
