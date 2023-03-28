# 使用Python官方Docker映像作為基本映像
FROM python:3.8

# 設置工作目錄
WORKDIR /app

# 複製並安裝應用程式的依賴
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼到映像中
COPY . /app/

# 設置環境變量
ENV PYTHONUNBUFFERED=1

# 執行應用程式
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]