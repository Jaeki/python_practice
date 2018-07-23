# python_practice
git 에 code push 하는 방법

(0) git client를 설치 합니다. (git-bash)
    https://git-scm.com/downloads

(1) git-bash 에서 다음을 실행하면 code를 repository 에서 복사해 옵니다.
    git clone https://github.com/Jaeki/python_practice.git

(2) email 과 user name 을 설정 합니다. (이건 한번만 하면 됩니다.)
   git config --global user.email "jaeki.hong@gmail.com"
   git config --global user.name "Jaeki Hong"

(3) code를 수정하고 git status 를 해보면 빨간색으로 수정된 파일이 보입니다.

(4) git add '파일명' 하면 commit 할 파일이 추가 됩니다.
    git add chapter6.py

(5) commit 메시지와 함께 커밋 합니다.
    git commit -m "test message"

(6) push 합니다.
    git push -u origin master

(7) repository 에서 본인이 업데이트한 코드가 잘 들어갔는지 확인합니다.

(8) 
 자신이 작업한 내용을 모두 원복 시킬 때 
 git stash
 
