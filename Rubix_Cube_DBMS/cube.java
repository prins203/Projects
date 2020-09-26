package cube3x3;

import java.util.*;
import java.sql.*;

public class cube{
	String[][][] state = new String[6][3][3];
	cubeface front;
	cubeface back;
	cubeface top;
	cubeface bottom;
	cubeface left;
	cubeface right;
	
	public cube() {
		
		front = new cubeface("f");		// 0 ----> white
		back = new cubeface("b");			// 1 ----> yellow
		top = new cubeface("T");			// 2 ----> red
		bottom = new cubeface("B");		// 3 ----> orange
		left = new cubeface("l");			// 4 ----> blue
		right = new cubeface("r");		// 5 ----> green
		
		state = new String[][][] { left.getface(), front.getface(), right.getface(), back.getface(), top.getface(), bottom.getface()};
	}
	
	public void show() {
		System.out.println("------------" + " " + Arrays.toString(top.getrow(0))+ " " + "--------------------------------");
		System.out.println("------------" + " " + Arrays.toString(top.getrow(1))+ " " + "--------------------------------");
		System.out.println("------------" + " " + Arrays.toString(top.getrow(2))+ " " + "--------------------------------");
		System.out.println(Arrays.toString(left.getrow(0)) + " " + Arrays.toString(front.getrow(0)) + " " + Arrays.toString(right.getrow(0)) + " " + Arrays.toString(back.getrow(0)));
		System.out.println(Arrays.toString(left.getrow(1)) + " " + Arrays.toString(front.getrow(1)) + " " + Arrays.toString(right.getrow(1)) + " " + Arrays.toString(back.getrow(1)));
		System.out.println(Arrays.toString(left.getrow(2)) + " " + Arrays.toString(front.getrow(2)) + " " + Arrays.toString(right.getrow(2)) + " " + Arrays.toString(back.getrow(2)));
		System.out.println("------------" + " " + Arrays.toString(bottom.getrow(0))+ " " + "--------------------------------");
		System.out.println("------------" + " " + Arrays.toString(bottom.getrow(1))+ " " + "--------------------------------");
		System.out.println("------------" + " " + Arrays.toString(bottom.getrow(2))+ " " + "--------------------------------");
	}
	
	public void rotateleft() {    // check this to complete front rotation
		String[][] tmpstore = back.getcinvface();
		back.setcinvface(left.getface());
		left.setface(front.getface());
		front.setface(right.getface());
		right.setface(tmpstore);
		
		//
		top.rotateR();
		//
		bottom.rotateL();
	}
	
	public void rotateright() {    // --
		String[][] tmpstore = back.getcinvface();
		back.setcinvface(right.getface());
		right.setface(front.getface());
		front.setface(left.getface());
		left.setface(tmpstore);
		
		//
		top.rotateL();
		//
		bottom.rotateR();
	}
	
	public void rotateup() {    // COMPLETELY PROOF
		String[][] tmpstore = front.getface();
		front.setface(bottom.getface());
		bottom.setface(back.getrinvface());
		back.setrinvface(top.getface());
		top.setface(tmpstore);
		
		//rotate the left face
		left.rotateL();
		
		//rotate the right face
		right.rotateR();
	}
	
	public void rotatedown() {    // COMPLETELY PROOF
		String[][] tmpstore = front.getface();
		front.setface(top.getface());
		top.setface(back.getrinvface());
		back.setrinvface(bottom.getface());
		bottom.setface(tmpstore);
		
		//rotate the left face
		left.rotateR();
				
		//rotate the right face
		right.rotateL();
	}
	
	public void R(int i) {    			//PROOF
		String[] tmpstore = front.getrow(i);
		front.setrow(i, left.getrow(i));
		left.setrow(i, back.getinvrow(i));// <------------------------
		back.setinvrow(i, right.getrow(i));
		right.setrow(i, tmpstore);
		
		if(i == 0) {
			top.rotateL();
		}
		if(i == 2) {
			bottom.rotateR();
		}
	}
	
	public void L(int i) {    			// PROOF 
		String[] tmpstore = front.getrow(i);
		front.setrow(i, right.getrow(i));
		right.setrow(i, back.getinvrow(i));//<---------------------------
		back.setrow(i, left.getrow(i));
		left.setrow(i, tmpstore);
		
		if(i == 0) {
			top.rotateR();
		}
		else if(i == 2) {
			bottom.rotateL();
		}
	}
	
	public void U(int i) {    // up
		String[] tmpstore = front.getcol(i);
		front.setcol(i, bottom.getcol(i));
		bottom.setcol(i, back.getinvcol(i));
		back.setinvcol(i, top.getcol(i));
		top.setcol(i, tmpstore);
		
		if(i == 0) {
			left.rotateL();
		}
		else if(i == 2) {
			right.rotateR();
		}
	}
	
	public void D(int i) {    // down
		String[] tmpstore = front.getcol(i);
		front.setcol(i, top.getcol(i));
		top.setcol(i, back.getinvcol(i));
		back.setinvcol(i, bottom.getcol(i));
		bottom.setcol(i, tmpstore);
		
		if(i == 0) {
			left.rotateR();
		}
		else if(i == 2) {
			right.rotateL();
		}
	}
	
	
	public void FR(int i) {
		this.rotateleft();
		this.D(i);
		this.rotateright();
	}
	
	public void FL(int i) {
		this.rotateleft();
		this.U(i);
		this.rotateright();
	}
	
	public void insertCube() {
		int num = 9;
		try {
			//Get connection
			Connection myConn = DriverManager.getConnection("jdbc:mysql://localhost:3306/cube3x3", "root", "admin203");
			// create statement
			Statement myStmt = myConn.createStatement();
			//execute sql query
//			String query = "INSERT INTO `cube_table` VALUES (" + 5 + ",\"" + front.getrow(0)[0] + "\",\"" + back.getrow(0)[0] + "\",\"" + top.getrow(0)[0] + "\",\"" + bottom.getrow(0)[0] + "\",\"" + left.getrow(0)[0] + "\",\"" + right.getrow(0)[0] + "\",NULL);";
			int myRs = myStmt.executeUpdate(query);
//			myRs = myStmt.executeQuery("select `Back` from cube_table");
			//process the result set
//			while (myRs.next()) {
//				System.out.println(myRs);
//				//myRs = myStmt.executeQuery("select `Front` from cube_table");
//			}
			myRs = 0;
			
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {

		cube myCube = new cube();
		myCube.insertCube();
		Scanner scan = new Scanner(System.in);
		myCube.show();
		System.out.println("Enter A Move: ");
		String in = scan.nextLine();

		while(in != "quit"){
			//rotations
			if(in.contentEquals("ror")) {	myCube.rotateright();	}
			else if(in.contentEquals("rol")) {	myCube.rotateleft();	}
			else if(in.contentEquals("rou")) {	myCube.rotateup();	}
			else if(in.contentEquals("rod")) {	myCube.rotatedown();	}
			
			//movements
			else if(in.contentEquals("u3")) {	myCube.U(2);	}
			else if(in.contentEquals("u2")) {	myCube.U(1);	}
			else if(in.contentEquals("u1")) {	myCube.U(0);	}
			else if(in.contentEquals("d3")) {	myCube.D(2);	}
			else if(in.contentEquals("d2")) {	myCube.D(1);	}
			else if(in.contentEquals("d1")) {	myCube.D(0);	}
			else if(in.contentEquals("r3")) {	myCube.R(2);	}
			else if(in.contentEquals("r2")) {	myCube.R(1);	}
			else if(in.contentEquals("r1")) {	myCube.R(0);	}
			else if(in.contentEquals("l3")) {	myCube.L(2);	}
			else if(in.contentEquals("l2")) {	myCube.L(1);	}
			else if(in.contentEquals("l1")) {	myCube.L(0);	}
			else if(in.contentEquals("fr3")) {	myCube.FR(2);	}
			else if(in.contentEquals("fr2")) {	myCube.FR(1);	}
			else if(in.contentEquals("fr1")) {	myCube.FR(0);	}
			else if(in.contentEquals("fl3")) {	myCube.FL(2);	}
			else if(in.contentEquals("fl2")) {	myCube.FL(1);	}
			else if(in.contentEquals("fl1")) {	myCube.FL(0);	}
			
			myCube.show();
			System.out.println("Enter A Move: ");
			in = scan.next();
			
		}
		scan.close();
	}
}
