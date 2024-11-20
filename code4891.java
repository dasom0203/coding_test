package test01;

import java.util.Arrays;
import java.util.Scanner;

public class t_code4891 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		// 학생 수 입력
		int N=sc.nextInt();
		// 점수를 저장할 배열 생성
		int [] datas = new int[N];
		
		// 반복문을 통해 점수를 입력 받는다
		
		for(int i=0; i<datas.length; i++) {
			datas[i]=sc.nextInt();
		}
		
		// 최대 점수와 최소 점수 찾기 (api 사용)
		int max = Arrays.stream(datas).max().getAsInt();
		int min = Arrays.stream(datas).min().getAsInt();
		
		// 점수 차이 확인
		int res=max-min;
		System.out.println(res);
		
		
	}
}
