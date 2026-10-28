package ejercicio2;

public class Rectangulo extends Figura {
    private double base;
    private double altura;

    public Rectangulo(String nombre, double base, double altura) {
        super(nombre);
        this.base = base;
        this.altura = altura;
    }

    public double getBase() {
        return base;
    }

    public double getAltura() {
        return altura;
    }

    @Override
    public double calcularArea() {
        return base * altura;
    }

    @Override
    public String toString() {
        return "Rectangulo{nombre='" + nombre + "', base=" + base + ", altura=" + altura + "}";
    }
}
