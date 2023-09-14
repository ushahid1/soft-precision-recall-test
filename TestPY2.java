//package testpy;

import java.io.*;

public class TestPY2 {

	public static void main(String[] args) throws IOException {
		
		String st1 = "University Colleage School Research Institute";
		String st2 = "Finland University Forest Lake";
		 
		
		ProcessBuilder pb = new ProcessBuilder("python3","softPR.py",""+st1,""+st2);
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
