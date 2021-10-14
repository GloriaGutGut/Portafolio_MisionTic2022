public class App {
    public static void main(String[] args) throws Exception {
        
        ProyectoTextiles estudio1 = new ProyectoTextiles(0,0,0);
        ProyectoTextiles estudio2 = new ProyectoTextiles(2,10000000,6);
                
        System.out.println(estudio1.calcInteresS());
        System.out.println(estudio1.calcInteresC());
        System.out.println(estudio1.compararIntereses());
        System.out.println(estudio2.calcInteresS());
        System.out.println(estudio2.calcInteresC());
        System.out.println(estudio2.compararIntereses());

    }
}
