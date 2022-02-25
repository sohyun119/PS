package set01;

import java.util.Scanner;
// 배열 돌리기 1, 2 둘 다 똑같이 품 (회전 수를 주기로 나눈 몫 만큼만 돌리게)
public class Num16926 {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); 
		int m = sc.nextInt();
		int r = sc.nextInt(); sc.nextLine();
		int[][] a = new int[n][m];
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				a[i][j] = sc.nextInt();	
			}
			sc.nextLine();
		}
		int nn = n;
		int mm = m;
		int min = ( n<m ? n:m );
		// 각각 돌아야 하는 경로의 수는 min/2 이다.
		for(int c=0; c<min/2; c++) {
			int p=c;
			int q=c;
			// 총 돌려야 하는 r의 주기를 생각해서 나머지 만큼만 돌림
			for(int cycle=0; cycle< r%(2*(nn-c)+2*(mm-c)-4); cycle++) {
				// 덮어 쓰면 안되므로 순서를 뒤에서 부터 씌운다.
				int temp = a[c][c];
				for(int k=0; k<(2*(nn-c)+2*(mm-c)-4); k++) {
					if(p==c && q<mm-1){
						a[p][q] = a[p][q+1];
						q++;
					}
					else if(q==mm-1 && p<nn-1) {
						a[p][q] = a[p+1][q];
						p++;
					}
					else if(p==nn-1 && q>c) {
						a[p][q] = a[p][q-1];
						q--;
					}
					else if(q==c && p>c) {
						a[p][q] = a[p-1][q];
						p--;
					}
					
				}
				a[c+1][c] = temp;
			}
			nn--;
			mm--;
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				System.out.print(a[i][j] + " ");
			}
			System.out.println();
		}
	}

}
