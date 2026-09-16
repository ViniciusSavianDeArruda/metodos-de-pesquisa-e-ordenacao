package Controller;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class Util {

    public static boolean carregarArquivoEmLista(String nomeArquivo, ArrayList<Integer> lista) {
        try {
            
            System.out.println("PASTA ATUAL: " + System.getProperty("user.dir"));
            System.out.println("ARQUIVO INFORMADO: " + nomeArquivo);
            
            FileReader procurador;
            procurador = new FileReader(nomeArquivo);
            BufferedReader leitor = new BufferedReader(procurador);
            String linha;
            do {
                linha = leitor.readLine();
                if (linha != null) {
                    lista.add(Integer.parseInt(linha));
                }                
            } while (linha != null);
            leitor.close();
            return true;
        } catch (Exception e) {
             JOptionPane.showMessageDialog(
        null,
        "Erro: " + e.getClass().getName() + "\n" + e.getMessage()
         
    );
    return false;
            
        }
    }
}