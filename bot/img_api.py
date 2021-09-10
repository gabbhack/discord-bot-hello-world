from typing import Optional

from aiohttp import ClientSession
from pydantic import BaseModel

class Image(BaseModel):
    link: str

class ImageApi:
    def __init__(self) -> None:
        self.session: Optional[ClientSession] = None
    
    async def create_session(self) -> ClientSession:
        if self.session is None or self.session.closed:
            self.session = ClientSession()
        return self.session

    async def get(self, animal: str) -> Image:
        session = await self.create_session()
        async with session.get(f"https://some-random-api.ml/img/{animal}") as resp:
            json = await resp.json()
            image = Image(**json)
            return image
