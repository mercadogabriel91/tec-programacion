package ejercicio4;

public class Animal {
    protected String nombre;

    public Animal(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void hacerSonido() {
        System.out.println(nombre + " hace un sonido.");
    }

    public void describirAnimal() {
        System.out.println("Animal: " + nombre);
    }

    @Override
    public String toString() {
        return "Animal{nombre='" + nombre + "'}";
    }
}
