package ejercicio4;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Animal> animales = new ArrayList<>();
        animales.add(new Perro("Dogeroo"));
        animales.add(new Gato("Tigur"));
        animales.add(new Vaca("Girr"));

        System.out.println("--- Sonidos por polimorfismo ---");
        for (Animal animal : animales) {
            animal.describirAnimal();
            animal.hacerSonido();
        }
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-7/src
 */
