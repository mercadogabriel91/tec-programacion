package ejercicio1;

public class Main {
    public static void main(String[] args) {
        Inventario inventario = new Inventario();

        System.out.println("--- 1. Alta de productos ---");
        inventario.agregarProducto(new Producto("P001", "Arroz 1kg", 1200, 50, CategoriaProducto.ALIMENTOS));
        inventario.agregarProducto(new Producto("P002", "Dulce de leche", 5000, 15, CategoriaProducto.ALIMENTOS));
        inventario.agregarProducto(new Producto("P003", "Remera", 2800, 30, CategoriaProducto.ROPA));
        inventario.agregarProducto(new Producto("P004", "Sarten", 1800, 12, CategoriaProducto.HOGAR));
        inventario.agregarProducto(new Producto("P005", "Yerba 500g", 950, 80, CategoriaProducto.ALIMENTOS));
        inventario.agregarProducto(new Producto("P006", "Cargador USB", 3000, CategoriaProducto.ELECTRONICA)); // sin stock inicial
        inventario.agregarProducto(new Producto("P001", "Duplica2", 100, 1, CategoriaProducto.HOGAR)); // id repetido

        System.out.println("\n--- 2. Listado de los productos ---");
        inventario.listarProductos();

        System.out.println("\n--- 3. Busqueda usando un ID ---");
        Producto encontrado = inventario.buscarProductoPorId("P003");
        if (encontrado != null) {
            encontrado.mostrarInfo();
        }
        System.out.println("Buscar P999: " + inventario.buscarProductoPorId("P999"));

        System.out.println("\n--- 4. Filtrar por categoría ALIMENTOS ---");
        for (Producto p : inventario.filtrarPorCategoria(CategoriaProducto.ALIMENTOS)) {
            p.mostrarInfo();
        }

        System.out.println("\n--- 5. Eliminar P004 y listar los restantes ---");
        inventario.eliminarProducto("P004");
        inventario.listarProductos();

        System.out.println("\n--- 6. Actualizar stock de P002 ---");
        inventario.actualizarStock("P002", 40);
        inventario.buscarProductoPorId("P002").mostrarInfo();
        inventario.actualizarStock("P002", -5); // cantidad negativa invalida

        System.out.println("\n--- 7. Total de stock disponible ---");
        System.out.println("Total de unidades: " + inventario.obtenerTotalStock());

        System.out.println("\n--- 8. Producto con mayor stock ---");
        inventario.obtenerProductoConMayorStock().mostrarInfo();

        System.out.println("\n--- 9. Productos entre $1000 y $3000 ---");
        for (Producto p : inventario.filtrarProductosPorPrecio(1000, 3000)) {
            p.mostrarInfo();
        }

        System.out.println("\n--- 10. Categorías disponibles ---");
        inventario.mostrarCategoriasDisponibles();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-6/src
 */
