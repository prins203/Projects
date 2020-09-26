package cube3x3;

public class cubeface {
	final int size = 3;
	String[][] face = new String[size][size];
	
/////// CONSTRUCTORS //////////////////////////////////////
	public cubeface(String[][] face) {
		this.face = face;
	}
	
	public cubeface(String color) {
		String[] arr = {color,color,color};
		this.face[0] = arr;
		this.face[1] = arr;
		this.face[2] = arr;
	}
	
/////// GETTERS //////////////////////////////////////////////
	public String[][] getface() {
		String[][] value = new String[size][size];
		for(int j = 0; j < size; j++) {
			value[j] = face[j]; 
		}
		return value;
	}
	
	public String[][] getrinvface(){
		String[][] value = new String[size][size];
		for(int j = 0; j < size; j++) {
			value[j] = face[2-j]; 
		}
		return value;
	}
	
	public String[][] getcinvface(){
		String[][] value = new String[size][size];
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < size; j++) {
				value[j][i] = face[j][2-i]; 
			}
		}
		return value;
	}
	
	public String[] getrow(int i) {
		String[] value = new String[size];
		for(int j = 0; j < size; j++) {
			value[j] = face[i][j]; 
		}
		return value;
	}
	
	public String[] getinvrow(int i) {
		String[] value = new String[size];
		for(int j = 0; j < size; j++) {
			value[j] = face[i][2-j]; 
		}
		return value;
	}
	
	public String[] getcol(int i) {
		String[] value = new String[size];
		for(int j = 0; j < size; j++) {
			value[j] = face[j][i]; 
		}
		return value;
	}
	
	public String[] getinvcol(int i) {
		String[] value = new String[size];
		for(int j = 0; j < size; j++) {
			value[j] = face[2-j][i]; 
		}
		return value;
	}
	
//////// SETTERS ////////////////////////////
	public void setface(String color1, String color2, String color3) {
		String[] arr = {color1,color2,color3};
		this.face[0] = arr;
		this.face[1] = arr;
		this.face[2] = arr;
	}
	
	public void setrinvface(String[][] other){
		for(int j = 0; j < size; j++) {
			this.face[j] = other[2-j]; 
		}
	}
	
	public void setcinvface(String[][] other){
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < size; j++) {
				face[j][2-i] = other[j][i]; 
			}
		}
	}
	
	public void setface(String[][] face) {
		this.face = face;
	}
	
	public void setface(String[] c1, String[] c2, String[] c3) {
		;
	}
	
	public void setrow(int index, String[] value){
		this.face[index] = value;
	}
	
	public void setinvrow(int index, String[] value){
		for(int j = 0; j < size; j++) {
			face[index][j] = value[2-j]; 
		}
	}
	
	public void setcol(int index, String[] value){			//PASS
		String[] r0 = this.getrow(0);
		String[] r1 = this.getrow(1);
		String[] r2 = this.getrow(2);
		
		r0[index] = value[0];
		r1[index] = value[1];
		r2[index] = value[2];
		
		this.setrow(0, r0);
		this.setrow(1, r1);
		this.setrow(2, r2);
	}
	
	public void setinvcol(int index, String[] value){		//PASS
		String[] r0 = this.getrow(0);
		String[] r1 = this.getrow(1);
		String[] r2 = this.getrow(2);
		
		r0[index] = value[2];
		r1[index] = value[1];
		r2[index] = value[0];
		
		this.setrow(0, r0);
		this.setrow(1, r1);
		this.setrow(2, r2);
	}
	
///////// Methods ////////////////////////////
	
	public void rotateL() {					//Proof
		String[] r1 = this.getinvrow(1);
		String[] r2 = this.getinvrow(2);
		String[] r0 = this.getinvrow(0);
		
		String[] nr0 = {r0[0], r1[0], r2[0]};
		String[] nr1 = {r0[1], r1[1], r2[1]};
		String[] nr2 = {r0[2], r1[2], r2[2]};
		
		this.setrow(2, nr2);
		this.setrow(1, nr1);
		this.setrow(0, nr0);
	}
	
	public void rotateR() {					//Proof
		String[] r0 = this.getrow(0);
		String[] r1 = this.getrow(1);
		String[] r2 = this.getrow(2);
		
		String[] nr0 = {r2[0], r1[0], r0[0]};
		String[] nr1 = {r2[1], r1[1], r0[1]};
		String[] nr2 = {r2[2], r1[2], r0[2]};
		
		this.setrow(2, nr2);
		this.setrow(1, nr1);
		this.setrow(0, nr0);
		
		
		
	}
	
	
	
}
