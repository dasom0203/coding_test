package test01;

import java.util.Scanner;

public class t_code3130 { // 3130 : 소들의 헤어스타일

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 소 마리 수 저장
		int N=sc.nextInt();
		// 소들의 키를 저장할 배열 생성
		int[] datas = new int[N];
		
		// 배열에 소들의 키를 저장시킨다
		for(int i=0; i<datas.length; i++) {
			datas[i]=sc.nextInt();
		}
		
		int count = 0;
		// index 0번부터 돌며 헤어를 확인한다
		for(int i=0; i<N; i++) {
			/*
			datas[0]이랑 datas[1]랑 비교하고,
			datas[0]이랑 datas[2]랑 비교하고,
			datas[0]이랑 datas[3]랑 비교하고,
			
			datas[1]이랑 datas[2]랑...
			*/
			// 방법 1) 범위가 정해져있다. (N 마리)
			for(int j=i+1;j<N;j++) {
				if(datas[i] <= datas[j]) {
					break;
				}
				count++;
			}
			
			// 방법 2) 정확한 반복 횟수를 모른다.
//			int j=i+1;
//			while(datas[i] > datas[j] && j<N) {
//				count++;
//				j++;
//			}
			
		}
		
		// 확인 횟수 출력
		System.out.println(count);
		
		
	}
}
