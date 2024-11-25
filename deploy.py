import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 가져오기
username = os.getenv("PYPI_USERNAME")
password = os.getenv("PYPI_PASSWORD")

# 패키지 빌드 및 배포
os.system("python setup.py sdist")
os.system(f"twine upload dist/* -u {username} -p {password}")
