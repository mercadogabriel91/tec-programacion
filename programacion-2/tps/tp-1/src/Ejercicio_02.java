package src;

public class Ejercicio_02 {
    public static String name = "Gabriel";
    public static int age = 34;
    public static double height = 1.85;
    public static boolean student = true;

    public static String is_student(boolean arg) {
        return arg ? "si" : "no";
    }

    public static void main() {
        System.out.println("Nombre: " + name + " y tengo " + age + " años de edad. Mi estatura es de: " + height + ". soy estudiante? " + is_student(student));
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-1/src
 */
