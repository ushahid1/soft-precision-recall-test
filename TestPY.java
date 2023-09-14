//package testpy;

import java.io.*;

public class TestPY {

	public static void main(String[] args) throws IOException {
		
		String st1 = "Finland";
		String st2 = "Joensuu";
		 
		
		ProcessBuilder pb = new ProcessBuilder("python3","test2.py",""+st1,""+st2);
		Process p = pb.start();
		System.out.println("Test");
		BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
		
		String line = in.readLine();
		
		while(line !=null){
			System.out.println(line);
			line = in.readLine();
		    
		}
	}

}
