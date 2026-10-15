package ejercicio1;

import java.util.ArrayList;

// relacione de One to Many
public class Inventario {
    private final ArrayList<Producto> productos = new ArrayList<>();

    public void agregarProducto(Producto p) {
        if (p == null) {
            System.out.println("Error: no se puede agregar un producto nulo.");
            return;
        }
        if (buscarProductoPorId(p.getId()) != null) {
            System.out.println("Error: Ese porducto ya esta en la lista, prod id: " + p.getId() + ".");
            return;
        }
        productos.add(p);
    }

    public void listarProductos() {
        if (productos.isEmpty()) {
            System.out.println("El inventario está vacío.");
            return;
        }
        for (Producto p : productos) {
            p.mostrarInfo();
        }
    }

    public Producto buscarProductoPorId(String id) {
        for (Producto p : productos) {
            if (p.getId().equalsIgnoreCase(id)) {
                return p;
            }
        }
        return null;
    }

    public void eliminarProducto(String id) {
        Producto p = buscarProductoPorId(id);
        if (p == null) {
            System.out.println("Error: no se encontró el prod con id " + id + ".");
            return;
        }
        productos.remove(p);
        System.out.println("Producto eliminado: " + p.getNombre());
    }

    public void actualizarStock(String id, int nuevaCantidad) {
        Producto p = buscarProductoPorId(id);
        if (p == null) {
            System.out.println("Error: no existe un producto con id " + id);
            return;
        }
        p.setCantidad(nuevaCantidad);
    }

    public ArrayList<Producto> filtrarPorCategoria(CategoriaProducto categoria) {
        ArrayList<Producto> resultado = new ArrayList<>();
        for (Producto p : productos) {
            if (p.getCategoria() == categoria) {
                resultado.add(p);
            }
        }
        return resultado;
    }

    public int obtenerTotalStock() {
        int total = 0;
        for (Producto p : productos) {
            total += p.getCantidad();
        }
        return total;
    }

    public Producto obtenerProductoConMayorStock() {
        if (productos.isEmpty()) {
            return null;
        }
        // el primero es el campeón inicial siguiendo lo recomendado en las buenas practicas del PDF
        Producto mayor = productos.get(0);
        for (int i = 1; i < productos.size(); i++) {
            Producto p = productos.get(i);
            if (p.getCantidad() > mayor.getCantidad()) {
                mayor = p;
            }
        }
        return mayor;
    }

    public ArrayList<Producto> filtrarProductosPorPrecio(double min, double max) {
        ArrayList<Producto> resultado = new ArrayList<>();
        for (Producto p : productos) {
            if (p.getPrecio() >= min && p.getPrecio() <= max) {
                resultado.add(p);
            }
        }
        return resultado;
    }

    public void mostrarCategoriasDisponibles() {
        for (CategoriaProducto c : CategoriaProducto.values()) {
            System.out.println(c + " -> " + c.getDescripcion());
        }
    }
}
