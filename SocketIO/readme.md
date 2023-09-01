wihout async 0.1
```bash gunicorn -k eventlet -w 1  main:app```

with async 0.2 
```uvicorn --reload main:app```

req pip 
1- 'uvicorn[standard]'
