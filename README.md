## 알고리즘 연습 🔥🔥🔥

### python
  ### 1215 : 백준 2884 - if 문 (알림시계)
  + 출처 : https://www.acmicpc.net/problem/2884
    + 풀이
      1) 두개 값 입력 받기
      2) 두개 값 유효성 확인
      3) 45분 이전 시간 연산 (입력 분 - 45분가 음수면? 시간이 0이면?) 
      4) 출력
    + 소요시간 : 32분 
    + 기록하고 싶은 것 : 
      + Map 함수 이용해서 입력 받기
      + input() 2번 각각 입력 받으니 런타임 에러로 한참 고민. 
      ```python
      a, b = map(int, input().split())
      ```
### 1216: 백준 2588- 곱셈
  + 출처 : https://www.acmicpc.net/problem/2588
      + 풀이
        + 세자리수 2개 입력 
        + 두번째 입력값 100의 자리, 10의 자리, 1의 자리 분리
        + 각 자리수의 곱셈 결과값 출력
      + 소요시간 : 50분
      + 기록하고 싶은 것 
        + 처음 입력값을 아래로 받고 //, % 연산자를 이용해서 자리수 분리 시도함
        ```python
        a, b = map(int, input().split())
        ```
        + IDE에서는 정상 작동했지만 백준 web에서는 런타임
        + 연산을 바꿔보고 변수 선언을 없애보고 다양하게 시도
        + 결과적으로는 2번째 입력값을 string으로 받아서 글짜로 접근한 뒤에 형변환하여 성공.
    
### 1216: 백준 2753- 윤년 구하기
   + 출처 : https://www.acmicpc.net/problem/2753
        + 풀이
          + 비교 연산자 and, or 
        + 소요시간 : 3분
        + 기록하고 싶은 것
          + 간단한 연산인데 ()를 쳐주지 않아서 틀림
          + ```python
            year = int(input())
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                  print(1)
            else:
                  print(0)
            ```
### 1226: 백준 2739 구구단
   + 출처 : https://www.acmicpc.net/problem/2739
     + 풀이
       + for 반복문 사용
     * 소요시간 : 5분
     * 기록하고 싶은 것
       * 간만에 파이썬을 사용했더니 for 반복문이 기억이 나지 않음.
       * range() 함수를 사용하면 리스트 같은 객체를 만들어 사용할 수 있다.
     ``` python
      num = int(input())
      for i in range(1, 10):
      print(num, "*", i, "=", num * i)
      i = i + 1
     ```
### 1228: 백준 15552 빠른 출력
   + 출처 : https://www.acmicpc.net/problem/15552
     + 풀이 : 빠른 출력문 사용
     + 소요시간 : 4분
     + 기혹하고 싶은 것
       + ```html
         <ul>
            <li>Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. 
            BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.</li>
       
            <li>Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
            단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .
            rstrip()을 추가로 해 주는 것이 좋다.</li>
         </ul>
         ```
