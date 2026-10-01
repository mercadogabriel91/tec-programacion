package ejercicio11;

public class Cancion {
    private String titulo;
    private Artista artista;

    public Cancion(String titulo, Artista artista) {
        this.titulo = titulo;
        setArtista(artista);
    }

    public String getTitulo() {
        return titulo;
    }

    public Artista getArtista() {
        return artista;
    }

    public void setArtista(Artista artista) {
        if (artista == null) {
            System.out.println("Error: la canción necesita un artista.");
            return;
        }
        this.artista = artista;
    }

    @Override
    public String toString() {
        return "Cancion{titulo='" + titulo + "', artista=" + artista + "}";
    }
}
