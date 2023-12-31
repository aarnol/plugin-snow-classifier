
FROM waggle/plugin-base:1.1.1-ml
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt
ADD https://web.lcrc.anl.gov/public/waggle/models/snow/snowclassifier.pth /app/model.pth

COPY app.py /app/
WORKDIR /app
ENTRYPOINT ["python3", "/app/app.py"]
