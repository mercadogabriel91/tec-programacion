package ejercicio13;

public class GeneradorQR {

    // dependencia de creación: el QR se crea dentro del método
    public void generar(String valor, Usuario usuario) {
        if (valor == null || valor.trim().isEmpty()) {
            System.out.println("Error: el valor del QR no puede estar vacío.");
            return;
        }
        CodigoQR codigo = new CodigoQR(valor, usuario);
        System.out.println("QR generado: " + codigo);
    }
}
