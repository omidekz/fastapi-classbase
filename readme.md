# FastAPI ClassBase API

## install

`pip install git+https://github.com/omidekz/fastapi-classbase`

## Usage

```py
from fastapi import FastAPI, Query
from faclsbase import API, BaseAPI
from typing import List
from pydantic import Field

app = FastAPI()


@app.get('/simple-calc')
class SumAPI(metaclass=API): # THIS CLASS IS NOT EXTENDABLE
    numbers: List[int] = Field(Query(None))

    def run(self):
        return f'={sum(self.numbers)}'

# or
@app.get('/simple-calc-deco')
@API.classic
class SumAPI2(BaseAPI): # THIS CLASS IS NOT EXTENDABLE TOO
    numbers: List[int] = Field(Query(None))
    run = lambda self: f'{=sum(self.numbers)}'
```

## inheritance

```py
from faclsbase import API, BaseAPI as _BaseAPI
from typing import ClassVar


app = ...


class BaseAPI(_BaseAPI):
    repo: ClassVar[object] = None


@app.get('...')
class XAPI(BaseAPI, metaclass=API):
    pass
```
