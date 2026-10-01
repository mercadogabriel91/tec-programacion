package ejercicio14;

public class EditorVideo {

    // dependencia de creación: el render se crea dentro del method
    public void exportar(String formato, Proyecto proyecto) {
        if (formato == null || formato.trim().isEmpty()) {
            System.out.println("Error: el formato de exportación no puede estar vacío.");
            return;
        }
        Render render = new Render(formato, proyecto);
        System.out.println("Exportación finalizada: " + render);
    }
}
