package ejercicio6;

import java.time.LocalDate;
import java.time.LocalTime;

public class Reserva {
    private LocalDate fecha;
    private LocalTime hora;
    private Cliente cliente;
    private Mesa mesa;

    // pa reserva sabe del cliente y la mesa pero no al reves
    public Reserva(LocalDate fecha, LocalTime hora, Cliente cliente, Mesa mesa) {
        this.fecha = fecha;
        this.hora = hora;
        setCliente(cliente);
        setMesa(mesa);
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public LocalTime getHora() {
        return hora;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        if (cliente == null) {
            System.out.println("Error: la reserva necesita un cliente.");
            return;
        }
        this.cliente = cliente;
    }

    public Mesa getMesa() {
        return mesa;
    }

    public void setMesa(Mesa mesa) {
        if (mesa == null) {
            System.out.println("Error: la reserva necesita una mesa.");
            return;
        }
        this.mesa = mesa;
    }

    @Override
    public String toString() {
        return "Reserva{fecha=" + fecha + ", hora=" + hora + ", cliente=" + cliente + ", mesa=" + mesa + "}";
    }
}
