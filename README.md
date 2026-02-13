1. Clone project
2. cd <project folder>

3. python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

4. ```bash
    pip install -r requirements.txt
   ```
   Or
```bash
pip install fastapi uvicorn
```

5. ````
   uvicorn main:app --host 0.0.0.0 --port 8000
   ````
