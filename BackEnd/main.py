import uvicorn
from fastapi import FastAPI
import Src.ItemAPI as ItemAPI
import Src.MatHangAPI as MatHangAPI
import Src.HoaDonBanHangAPI as HoaDonBanHangAPI
import Src.HoaDonMuaHangAPI as HoaDonMuaHangAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# app.include_router(ItemAPI.router)
app.include_router(MatHangAPI.router)
app.include_router(HoaDonBanHangAPI.router)
app.include_router(HoaDonMuaHangAPI.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# https://stackoverflow.com/questions/62856818/how-can-i-run-the-fast-api-server-using-pycharm
