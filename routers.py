from fastapi import APIRouter, Path, Query
from converter import sync_converter,async_converter
from asyncio import gather

router = APIRouter(prefix='/converter')

@router.get('/{from_currency}')
def converter(
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'),
    to_currencies:str = Query(max_length=100, regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price:float = Query(gt=0)
):
    
    to_currencies = to_currencies.split(',')
    result = []
    for currency in to_currencies:
        response = sync_converter(
            from_currency= from_currency,
            to_currency=currency,
            price=price
        )
        result.append(response)
    return result


@router.get('/async/{from_currency}')
async def route_async_converter(
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'),
    to_currencies:str = Query(max_length=100, regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price:float = Query(gt=0)
):
    
    to_currencies = to_currencies.split(',')
    corroutines = []
    for currency in to_currencies:
        coro = async_converter(
            from_currency= from_currency,
            to_currency=currency,
            price=price
        )
        corroutines.append(coro)
    result = await gather(*corroutines)
    return result
