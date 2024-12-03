package test02;


public class DupliString {
	
	public String solution(String my_string) { // input으로 받은 문자열에서, 중복을 제거 (하나만 남기기) 후 반환
        String answer = "";
		
		// 문자열 길이만큼 반복문을 돌린다
		for(int i=0; i<my_string.length(); i++) {
			
			// indexOf를 통해 문자의 처음 위치가 현재 위치와 같다면 저장한다.
			if(my_string.indexOf(my_string.charAt(i))==i) { // 현재 위치가 문자열의 첫 위치라면
				
				answer += my_string.charAt(i);
			}
			
		}
		
        return answer;
    }
	
	
	
	public static void main(String[] args) {
		
		String my_string = "We are the world";
		
		// 함수 호출
		DupliString dupli_string = new DupliString();
		
		// 중복된 문자열 제거 후 반환
		String answer = dupli_string.solution(my_string);
		
		
		// 결과 확인
		System.out.println(answer);
		
	}

}
