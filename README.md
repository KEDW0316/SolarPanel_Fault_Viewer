# 코드 컨벤션

#### 1. vscode liveshare extension

프로젝트 진행 시, 문제 되는 부분이나, 의견 공유가 필요할 경우

#### 2. 프로젝트 폴더 구조

client
-public
-index.html
-src
-components
-routes
-router.js
-index.js
-App.js

#### 3. github 활용

- 이슈관리

#### 4. git branch 활용 및 workflow

- 메인 브랜치 > production, main, develop/이름
- 서브 브랜치 > feature

각 브랜치 설명

## .

> production branch

- 실제 라이브 배포 이력 관리 브랜치 (핵심 브랜치)

## .

> main branch

- 라이브 배포 전, 통합 및 테스트 브랜치

## .

> develop/이름 branch

- 다음 출시 버전을 개발하는 개인별 브랜치
- 모든 기능이 추가되고 버그가 수정되어 배포 가능한 안정적인 상태면 main 브랜치에 머지
- 평소 이 브랜치로 개발 진행
- main으로 PR날리고 머지 진행
- git 은 root directory 에서만 실행

## .

> feature branch (local 에서만)

- 새로운 기능 개발 및 버그 수정이 필요할 때마다, develop 브랜치로부터 분기한다.
- feature 브랜치는 기본적으로 공유 필요가 없기에 자기 로컬 저장소에만 관리
- branch naming : feature/login

## .

> Github Workflow

- develop 브랜치에서 feature branch 생성해서 작업
- 기능 완성하면 develop 머지 후, 깃 서버에 푸시 (origin/develop/이름 으로 push)
- develop 브랜치에서 main 브랜치로 PR
- PR 통과 후, main 브랜치에서 테스트
- 위 4줄 반복
- Live 배포시, develop 테스트 후, main 브랜치로 머지

#### 5. commit msg convention

> type

- feat : 새로운 기능 추가 , 레이아웃
- fix : 버그 수정
- docs : 문서 수정
- style: 코드 포맷팅, 세미콜락 누락, 코드 변경이 없는 경우
- refactor : 코드 리팩토링
- test : 테스트 코드
- chore: 빌드 업무, 패키지 매니저 수정

ex) client 코드수정
-feat/client

    server 코드수정

-feat/server

## .

> format

- 제목 외, 한줄에 100줄 이내
- 코드명 외, 한글, 영어 혼합 가능, 다른 사람이 이해할 수 있도록
- 본문은 '어떻게'보다 '무엇을', '왜'에 맞춰 작성하기
- ~다, ~예요. 사용금지
- 제목, 본문, 푸터에 한 줄씩 띄워 분리하기
- close #이슈번호

```
<type>: <제목> (\* 50자 이내)

<body>  (* 커밋 상세 내용)

<footer> (* 어떤 이슈에서 왔는지 설명)
```

## .

> example

```
ex)
feat: 알림 기능 추가

페이지 헤더 측, 알림 버튼 추가
알림 조회 api 호출 기능 및 미읽기 알림 표시
```

close #100

푸터가 없을 경우 - 표시

#### 4. prettier, jslint => 협의

.prettierrc 프로젝트 구조 상단에 생성 및 아래 코드 추가

```
arrowParens": "avoid",
trailingComma": "all"
tabWidth": 2,
semi": true,
singleQuote": true,
printWidth": 80,
```

#### 5. npm, yarn, => 협의

npm

#### 6. 리소스 배분 > 진행 순서의 선순위 기능 배분 => 협의

#### 7. 개발일정 산출하기 => 협의

## .

#### 8. 명명 규칙

- 예약어 사용 x

```
  ex)
  let class;
  let import;
```

- 변수, 함수 카멜케이스 사용

```
  ex)
  function getTest(){}
  let testValue;
```

- 함수명 > 앞에 동사가 먼저온다.

```
  ex)
  function setTest(){}
  const deleteUser = () => {}
```

- 줄임말 최대한 사용금지, 최대한 풀네임을 이용할 것, 명확하게

```
  ex)
  let testVal; (x)
  let testValue; (0)
```

- 상수 > 카멜케이스 사용

```
  ex)
  const totalTest = 50;
```

- Class, 컴포넌트 명 > 파스칼 케이스 사용

```
  ex)
  export default LoginModule(){
  return <></>;
  }
```

- 컴포넌트 파일명 > 파스칼 케이스 사용

```
  ex)
  LoginModule.tsx
```

- 일반 파일, 폴더명 카멜케이스 사용

```
  ex)
  commentApi.ts
```

- styled-components > 파스칼 케이스

- var 사용금지

- inline css를 사용금지

#### 9. 주석 규칙

- 일반적인 한 줄 주석 //

- 문장 주석 사용시

```
/*
 *
 */
```

- 함수, 컴포넌트 설명 주석은 jsdoc 형식 사용
  (desc, param, returns 기본적으로 포함시키기 (없으면 x))

```
/**
 * @desc Solves equations of the form a * x = b

 * @example
 * globalNS.method(5, 15);

 * @param {number} a - 분모
 * @param {number} b - 분자
 * @returns {number} - 나눗셋 결과
 */
function test(a, b) {
    return b / a;
};
```

#### 10. 라이브러리 관리

- 스타 수 적정이상과 유지보수가 잘 되는 라이브러리 사용하기
  (검증이 완료된 유틸 라이브러리는 사용해도됨)

- 라이브러리 설치 후, 사용한 다음 나중에 버전 업그레이드 시,
  팀원들에게 의견을 나누고 업그레이드 하기.

- 특정 라이브러리 설치 시, 나중에라도 팀원들에게 공유하기
