package ejercicio4;

public class Vaca extends Animal {

    public Vaca(String nombre) {
        super(nombre);
    }

    @Override
    public void hacerSonido() {
        System.out.println(nombre + " dice: muu");
    }

    @Override
    public void describirAnimal() {
        System.out.println("Vaca: " + nombre);
    }
}
