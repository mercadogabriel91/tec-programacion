package ejercicio11;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Asociación unidireccional: Cancion -> Artista ---");
        Artista artista = new Artista("Soda Stereo", "Rock");
        Cancion cancion1 = new Cancion("De música ligera", artista);
        Cancion cancion2 = new Cancion("Persiana americana", artista);
        System.out.println(cancion1);
        System.out.println(cancion2);

        System.out.println("\n--- Dependencia de uso: Reproductor.reproducir(Cancion) ---");
        Reproductor reproductor = new Reproductor();
        reproductor.reproducir(cancion1);
        reproductor.reproducir(cancion2);
        reproductor.reproducir(null);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
