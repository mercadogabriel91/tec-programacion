package ejercicio11;

public class Reproductor {

    // Dependency injection: la canción llega por parámetro y no se guarda como atributo
    public void reproducir(Cancion cancion) {
        if (cancion == null) {
            System.out.println("Error: no hay ninguna canción para reproducir.");
            return;
        }
        System.out.println("Reproduciendo: \"" + cancion.getTitulo() + "\" de " + cancion.getArtista().getNombre()
                + " (" + cancion.getArtista().getGenero() + ")");
    }
}
