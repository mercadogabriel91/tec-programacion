package ejercicio3;

public class EmpleadoPlanta extends Empleado {
    private double sueldoBase;
    private int aniosAntiguedad;

    public EmpleadoPlanta(String nombre, double sueldoBase, int aniosAntiguedad) {
        super(nombre);
        this.sueldoBase = sueldoBase;
        this.aniosAntiguedad = aniosAntiguedad;
    }

    public int getAntiguedad() {
        return aniosAntiguedad;
    }

    // sueldo base + un 5% por cada año de antigüedad
    @Override
    public double calcularSueldo() {
        return sueldoBase + (sueldoBase * 0.05 * aniosAntiguedad);
    }

    @Override
    public String toString() {
        return "EmpleadoPlanta{nombre='" + nombre + "', sueldoBase=" + sueldoBase
                + ", aniosAntiguedad=" + aniosAntiguedad + "}";
    }
}
