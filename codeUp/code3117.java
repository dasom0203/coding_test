package test01;

import java.util.Scanner;
import java.util.Stack;

public class t_code3117 { // 0은 빼!
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// N 크기 만큼의 스택 공간 형성
		int N=sc.nextInt();
		Stack<Integer> stack=new Stack<Integer>();

		for(int i=0; i<N; i++) {
			// N개의 데이터를 입력 받는다
			int data = sc.nextInt();
			// 	0이 아니라면 스택에 저장
			if(data != 0) {
				stack.push(data);
			}
			else { // 0이면 데이터 제거
				stack.pop();
			}

		}

		// 스택에 남아있는 모든 데이터를 더한다.
		int total = 0;
		for(int v:stack) {
			total += v;
		}

		System.out.println(total);

	}
}
