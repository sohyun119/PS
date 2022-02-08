package set01;

import java.util.Arrays;
import java.util.Scanner;

public class Num1920 {
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();  scan.nextLine();
		
		int[] a = new int[n];
		for(int i=0; i<n; i++) {
			int x = scan.nextInt(); 
			a[i] = x;
		}
		Arrays.sort(a); // 이진탐색을 위해서는 무조건 정렬이 되어 있어야 한다. 
		
		int m = scan.nextInt(); scan.nextLine();
	
		for(int i=0; i<m; i++) {
			int number = scan.nextInt(); 
			System.out.println(binarySearch(a,number));
		}
		
	
		
		
	}

	private static int binarySearch(int[] a, int number) {
		int count = 0; 
		int left = 0;
		int right = a.length - 1;
		int mid;
		
		while(left<=right) {
			mid = (left + right)/2;
			if(number == a[mid]) {
				count = 1;
				break;
			}
			else if(number > a[mid]) {
				left = mid+1;
			}else {
				right = mid-1;
			}
		}
		
		return count;
	}
	
	
	

}
