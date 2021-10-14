public class App{
    public static void main(String[] args) {
        Lasanas[] Lasanas1 = new Lasanas[5];
        Lasanas1[0] = new Lasanas("carne","4_porciones",22000.0);
        Lasanas1[1] = new ExtraQueso("pollo","12_porciones",25000.0, "provolone");
        Lasanas1[2] = new ExtraVegetales("camarones","12_porciones",18000.0, "champiñones");
        Lasanas1[3] = new ExtraVegetales("espinaca","4_porciones",25000.0, "calabacitas");
        Lasanas1[4] = new Lasanas(20000.0);
        ValorTotal respuesta1 = new ValorTotal(Lasanas1);
        respuesta1.mostrarTotales();
        System.out.println();
        System.out.println("------------------------");
        Lasanas[] Lasanas2 = new Lasanas[4];
        Lasanas2[0] = new Lasanas(20000.0);
        Lasanas2[1] = new Lasanas("pollo","12_porciones",23000.0);
        Lasanas2[2] = new ExtraQueso("espinaca","4_porciones",25000.0, "suizo");
        Lasanas2[3] = new ExtraVegetales("carne","12_porciones",23000.0, "calabacitas");
        ValorTotal respuesta2 = new ValorTotal(Lasanas2);
        respuesta2.mostrarTotales();
        System.out.println();
    }
}
// 60600  -  50000  -  80700  -  191300
// 68600  -  39500  -  47900  -  156000