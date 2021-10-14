package vista;

import java.sql.SQLException;
import java.util.ArrayList;

import controlador.ControladorRequerimientos;
import modelo.vo.Requerimiento_1Vo;
import modelo.vo.Requerimiento_2Vo;
import modelo.vo.Requerimiento_3Vo;

public class VistaRequerimientos {
    public static final ControladorRequerimientos controlador = new ControladorRequerimientos();
    public static void requerimiento1() {
        try {
            ArrayList<Requerimiento_1Vo> resultado_requerimiento1 = controlador.consultarRequerimiento1();
            //resultado_requerimiento1.forEach(System.out::println);
            for (Requerimiento_1Vo i : resultado_requerimiento1) {
                System.out.printf("%s %d %n", i.getCiudadResidencia(), i.getPromedio());
            }
        } catch (Exception e) {
            System.out.println("Se ha producido el siguiente error:" + e.getMessage());
            e.printStackTrace();
        }
    }
    public static void requerimiento2() {
        try {
            ArrayList<Requerimiento_2Vo> resultado_requerimiento2 = controlador.consultarRequerimiento2();
            for (Requerimiento_2Vo i : resultado_requerimiento2) {
                System.out.println(i.getIdProyecto() + " " + i.getProveedor());
            }
        } catch (Exception e) {
            System.out.println("Se ha producido el siguiente error:" + e.getMessage());
            e.printStackTrace();
        }
    }
    public static void requerimiento3() {
        try {
            ArrayList<Requerimiento_3Vo> resultado_requerimiento3 = controlador.consultarRequerimiento3();
            for (Requerimiento_3Vo i : resultado_requerimiento3) {
               System.out.printf("%d %s %n", i.getIdProyecto(), i.getNombreMaterial());
            }

        } catch (Exception e) {
            System.out.println("Se ha producido el siguiente error:" + e.getMessage());
            e.printStackTrace();
        }
    }
}
