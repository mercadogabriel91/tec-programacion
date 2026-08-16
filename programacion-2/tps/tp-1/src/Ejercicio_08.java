package src;

public class Ejercicio_08 {
    public static void main() {
        int a = 5;
        int b = 2;
        int resultado = a / b; // Esto lo tendrias que hacer un float / double para no perder los decimales

        // Prueba de escritorio:
        // a = 5
        // b = 2
        // el resultado te da que = a / b => 5 / 2 = 2 (sin los decimales)
        // El valor final de resultado es 2, no 2.5.
        // En Java, al dividir dos int se hace division entera:
        // se descarta la parte decimal (se trunca hacia 0).
        // Para obtener 2.5 habria que usar double, por ejemplo:
        // double resultado = (double) a / b;

        // tirar el resultado en la terminal
        System.out.println("Resultado: " + resultado);
    }
}
