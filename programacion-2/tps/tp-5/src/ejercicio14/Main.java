package ejercicio14;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Dependencia de creación: EditorVideo.exportar(String, Proyecto) ---");
        Proyecto proyecto = new Proyecto("Vlog random", 12);
        EditorVideo editor = new EditorVideo();
        editor.exportar("MP4", proyecto);
        editor.exportar("MOV", proyecto);

        System.out.println("\n--- Validación ---");
        editor.exportar("", proyecto);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
