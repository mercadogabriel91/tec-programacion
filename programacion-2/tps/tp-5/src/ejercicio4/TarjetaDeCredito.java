package ejercicio4;

import java.time.LocalDate;

public class TarjetaDeCredito {
    private String numero;
    private LocalDate fechaVencimiento;
    private Banco banco;
    private Cliente cliente;

    // agregación: el banco existe antes que la tarjeta y la recibe de afuera
    public TarjetaDeCredito(String numero, LocalDate fechaVencimiento, Banco banco) {
        this.numero = numero;
        this.fechaVencimiento = fechaVencimiento;
        setBanco(banco);
    }

    public String getNumero() {
        return numero;
    }

    public LocalDate getFechaVencimiento() {
        return fechaVencimiento;
    }

    public Banco getBanco() {
        return banco;
    }

    public void setBanco(Banco banco) {
        if (banco == null) {
            System.out.println("Error: la tarjeta debe estar emitida por un banco.");
            return;
        }
        this.banco = banco;
    }

    public Cliente getCliente() {
        return cliente;
    }

    // asociación bidireccional: mantiene sincronizados los dos lados
    public void setCliente(Cliente cliente) {
        if (this.cliente == cliente) {
            return;
        }
        Cliente anterior = this.cliente;
        this.cliente = cliente;
        if (anterior != null && anterior.getTarjeta() == this) {
            anterior.setTarjeta(null);
        }
        if (cliente != null) {
            cliente.setTarjeta(this);
        }
    }

    @Override
    public String toString() {
        return "TarjetaDeCredito{numero='" + numero + "', fechaVencimiento=" + fechaVencimiento + ", banco=" + banco
                + ", cliente=" + (cliente != null ? cliente.getNombre() : "sin cliente") + "}";
    }
}
