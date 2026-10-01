package ejercicio14;

public class Render {
    private String formato;
    private Proyecto proyecto;

    public Render(String formato, Proyecto proyecto) {
        this.formato = formato;
        setProyecto(proyecto);
    }

    public String getFormato() {
        return formato;
    }

    public Proyecto getProyecto() {
        return proyecto;
    }

    public void setProyecto(Proyecto proyecto) {
        if (proyecto == null) {
            System.out.println("Error: el render tiene que ser parte de un proyecto.");
            return;
        }
        this.proyecto = proyecto;
    }

    @Override
    public String toString() {
        return "Render{formato='" + formato + "', proyecto=" + proyecto + "}";
    }
}
