# 해당 디렉토리로 이동 후 python3 설치
sudo apt-get install python3

# python3-venv 설치
sudo apt-get install python3-venv

# 가상환경 만들기
python3 -m venv py_ms

# 가상환경 활성화
source py_ms/bin/activate

# 가상환경 비활성화
deactivate

# 가상환경 삭제
sudo rm -rf py_ms
