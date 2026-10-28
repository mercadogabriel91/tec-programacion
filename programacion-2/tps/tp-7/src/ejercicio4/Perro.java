package ejercicio4;

public class Perro extends Animal {

    public Perro(String nombre) {
        super(nombre);
    }

    @Override
    public void hacerSonido() {
        System.out.println(nombre + " dice: woof!!");
    }

    @Override
    public void describirAnimal() {
        System.out.println("Perro: " + nombre);
    }
}
