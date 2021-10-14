public class ProyectoTextiles {
    //atributos
    private int tiempo;
    private double capital; 
    private double interes;
    private double interes1;
    private double calcInteresS;
    private double calcInteresC;
    private double compararIntereses;

    //constructor
    public ProyectoTextiles(int tiempo, double capital, double interes){
        this.tiempo = tiempo;
        this.capital = capital;
        this.interes = interes;
    }

    //metodos
    public double calcInteresS(){
        return Math.round(capital * tiempo *(interes / 100));
    }
    public double calcInteresC(){
        double interes1 = 1+(interes/100);
        return  Math.round(capital * (Math.pow(interes1,tiempo)-1));
    }
    public double compararIntereses(){
        return calcInteresC() - calcInteresS();
    }
    
}
