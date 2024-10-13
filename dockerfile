# Gunakan image Python sebagai dasar
FROM python:3.8-slim

# Set working directory di dalam container
WORKDIR /app

# Install PostgreSQL development libraries (libpq-dev)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Install dependencies yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port yang digunakan oleh Flask (5000)
EXPOSE 5000

# Salin semua file aplikasi ke container
COPY . .

# Perintah untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]
