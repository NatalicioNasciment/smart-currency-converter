from fastapi import APIRouter
import requests

router = APIRouter()

@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies:str, price:float):
    return 'Run converter'
