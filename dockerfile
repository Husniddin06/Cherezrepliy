FROM python:3.11-slim

# OS dependencylarni o'rnatish
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt ni avval nusxalash va o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# keyin qolgan fayllarni nusxalash
COPY . .

CMD ["python", "main.py"]
