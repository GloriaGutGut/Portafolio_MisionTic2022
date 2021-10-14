//La clase Main no debe ser subida a iMaster, solo se debe utilizar para realizar
//las pruebas
public class reto2a {
/*    public static void main(String[] args) {
        Lasanas[] Lasanas1 = new Lasanas[5];
        Lasanas1[0] = new Lasanas("carne","4_porciones",22000.0);
        Lasanas1[1] = new ExtraQueso("pollo","12_porciones",25000.0, "provolone");
        Lasanas1[2] = new ExtraVegetales("camarones","12_porciones",18000.0, "champiñones");
        Lasanas1[3] = new ExtraVegetales("espinaca","4_porciones",25000.0, "calabacitas");
        Lasanas1[4] = new Lasanas();
        ValorTotal respuesta1 = new ValorTotal(Lasanas1);
        respuesta1.mostrarTotales();
        System.out.println();
    }
    public static void main(String[] args) {
        Lasanas[] Lasanas2 = new Lasanas[4];
        Lasanas2[0] = new Lasanas();
        Lasanas2[1] = new Lasanas("pollo","12_porciones",23000.0);
        Lasanas2[2] = new ExtraQueso("espinaca","4_porciones",25000.0, "suizo");
        Lasanas2[3] = new ExtraVegetales("carne","12_porciones",23000.0, "calabacitas");
        ValorTotal respuesta2 = new ValorTotal(Lasanas2);
        respuesta2.mostrarTotales();
        System.out.println();
    }
*/
}

class Lasanas {
    // Atributos
    private String sabor;
    private String tamano;
    private Double precioBase;

    // Constructores
    public Lasanas() {
        this("pollo","1_porcion",20000.0);
    }
    public Lasanas(String sabor, String tamano, Double precioBase) {
        this.sabor = sabor;
        this.tamano = tamano;
        this.precioBase = precioBase;
    }
    public Lasanas(double d) {
	}

	//getter and setter
    public String getSabor() {
        return sabor;
    }
    public void setSabor(String sabor) {
        this.sabor = sabor;
    }
    public String getTamano() {
        return tamano;
    }
    public void setTamano(String tamano) {
        this.tamano = tamano;
    }
    public Double getPrecioBase() {
        return precioBase;
    }
    public void setPrecioBase(Double precioBase) {
        this.precioBase = precioBase;
    }

    //Métodos
    public double calcularPrecio() {
        double Adiciones = 0.0;
        if(sabor.equals("espinaca")){
            Adiciones += (precioBase*0.1);
        } 
        if (sabor.equals("pollo")){
            Adiciones += (precioBase*0.2);
        }
        if (sabor.equals("carne")){  
            Adiciones += (precioBase*0.3);
        }
        if(sabor.equals("camarones")){
            Adiciones += (precioBase*0.4);
        }
        if (tamano.equals("1_porcion")){  
            Adiciones += 2000.0;
        }
        if (tamano.equals("4_porciones")){
            Adiciones += 6000.0;
        }
        if(tamano.equals("12_porciones")){
            Adiciones += 15000.0;
        }
        else {
            Adiciones += 0.0;
        }
        return precioBase + Adiciones;
    }
}

class ExtraVegetales extends Lasanas {
    // Atributos
    private String tipoVegetales;

    // Constructores
    public ExtraVegetales(String sabor, String tamano, Double precioBase, String tipoVegetales) {
        super(sabor, tamano, precioBase);
        this.tipoVegetales = tipoVegetales;
    }

    // Metodos
    @Override
    public double calcularPrecio() {
        Double AdicionesVeg =0.0;
        if(tipoVegetales.equals("calabacitas")){
            AdicionesVeg += 3000;
        }
        if (tipoVegetales.equals("champiñones")){
            AdicionesVeg += 4000;
        }
        else {
            AdicionesVeg += 0.0;
        }
        return super.calcularPrecio() + AdicionesVeg; 
    }
}

class ExtraQueso extends Lasanas {
    // Atributos
    private String tipoQueso;

    // Constructores
    public ExtraQueso(String sabor, String tamano, Double precioBase, String tipoQueso) {
        super(sabor, tamano, precioBase);
        this.tipoQueso = tipoQueso;
    }

    // Metodos
    @Override
    public double calcularPrecio() {
        Double AdicionesQ =0.0;
        if(tipoQueso.equals("provolone")){
            AdicionesQ += 5000;
        }
        if (tipoQueso.equals("suizo")){
            AdicionesQ += 6000;
        }
        else {
            AdicionesQ += 0.0;
        }
        return super.calcularPrecio() + AdicionesQ;
    }
}

class ValorTotal {
    // Atributos
    private Double valorTotalLasanas = 0.00;
    private Double valorTotalLasanasExtraQueso = 0.00;
    private Double valorTotalLasanasExtraVegetales = 0.00;
    private Double totalLasanas = 0.00;
    private Lasanas[] lasanas;

    // Constructores
    public ValorTotal(Double valorTotalLasanas, Double valorTotalLasanasExtraQueso, Double valorTotalLasanasExtraVegetales, Lasanas[] lasanas) {
        this.valorTotalLasanas = valorTotalLasanas;
        this.valorTotalLasanasExtraQueso = valorTotalLasanasExtraQueso;
        this.valorTotalLasanasExtraVegetales = valorTotalLasanasExtraVegetales;
    }
    public ValorTotal(Lasanas[] lasanas) {
        this.lasanas = lasanas;
    }

    // Métodos
    public void mostrarTotales() {
        int i = 0;
        for (i = 0; i < lasanas.length; i++){
            if (lasanas[i].getClass().getName() == "Lasanas"){
                valorTotalLasanas = valorTotalLasanas+ lasanas[i].calcularPrecio();
            }            
            if (lasanas[i].getClass().getName() == "ExtraQueso"){
                valorTotalLasanasExtraQueso += lasanas[i].calcularPrecio();
            }
            if (lasanas[i].getClass().getName() == "ExtraVegetales"){
                valorTotalLasanasExtraVegetales += lasanas[i].calcularPrecio();
            }
        totalLasanas = valorTotalLasanas + valorTotalLasanasExtraQueso+ valorTotalLasanasExtraVegetales;
        }
    
    // Cálculo totales
    System.out.println(Math.round(valorTotalLasanas));
    System.out.println(Math.round(valorTotalLasanasExtraQueso));
    System.out.println(Math.round(valorTotalLasanasExtraVegetales));
    System.out.println(Math.round(totalLasanas));
    }
}
