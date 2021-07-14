"""Good stuff."""

from typing import Any, Dict, Optional

from fastapi import Depends, FastAPI, Query
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Cookie, Header
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """Item model.

    Args:
        BaseModel ([type]): [description]
    """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def root():
    """root.

    Returns:
        [type]: [description]
    """
    return {"message": "Hello World"}


@app.get("/something", response_model=Dict[str, list[Any]])
async def something_get(*,
                        user_agent: Optional[str] = Header(None),
                        cookie: Optional[str] = Cookie(None),
                        good_stuff: set[str] = Query(...,
                                                     title='asdfasdfasdf',
                                                     min_length=2,
                                                     example=[
                                                         'asdf', 'asdfasdf'],
                                                     examples={
                                                         "200": {
                                                             'summary': "Some summary",
                                                             "description": "Some description",
                                                             'value': ['asdf', 'asdf']
                                                         },
                                                         "400": {'asdf': ['aaaaa']}
                                                     },
                                                     description="some string length",
                                                     )) -> Dict[str, list]:
    """good stuff.

    Args:
        good_stuff (Optional[int], optional): [description]. Defaults to 55.

    Returns:
        Dict[str,list]: [description]
    """
    print("U", user_agent, "cok", cookie)
    print("asdfasdF", type(good_stuff))
    print("Asdfasdf", good_stuff)
    return {"message": [good_stuff]}


class CommonQueryParams:
    """Common query params used in getter calls.
    """

    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    """common parameters as a function dependency.

    Args:
        q (Optional[str], optional): [description]. Defaults to None.
        skip (int, optional): [description]. Defaults to 0.
        limit (int, optional): [description]. Defaults to 100.

    Returns:
        [type]: [description]
    """
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    """simple call using class dependency.

    Args:
        commons (CommonQueryParams, optional): [description]. Defaults to Depends(CommonQueryParams)

    Returns:
        [type]: [description]
    """
    return jsonable_encoder(commons.__dict__)


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    """simple call using functional dependency.

    Args:
        commons (dict, optional): [description]. Defaults to Depends(common_parameters).

    Returns:
        [type]: [description]
    """
    return commons
