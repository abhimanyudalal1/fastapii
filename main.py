from fastapi import FastAPI

app= FastAPI() #calling it

def index():
    return 'heyy'